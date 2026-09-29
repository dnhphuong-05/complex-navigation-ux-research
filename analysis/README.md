# analysis/

Dữ liệu và script phân tích. Cấu trúc theo [treetest-research/information-architecture-validation](https://github.com/treetest-research/information-architecture-validation): export gốc nằm trong `data/raw/`, dữ liệu đã xử lý ở `data/`, script đánh số theo thứ tự chạy trong `scripts/`.

## Nội dung

* [Dataset](#dataset)
* [Scripts](#scripts)
* [Environment](#environment)
* [Quy ước](#quy-ước)

## Dataset

| File | Nội dung | Tương ứng treetest | Trạng thái |
|---|---|---|---|
| `data/raw/<study>/` | Export gốc từ công cụ (card sort, tree test, usability, A/B, analytics). Không chỉnh sửa. | `data/raw/` | Trống |
| `data/navigation_inventory.csv` | 145 destination của sidebar hiện tại + audit flag | — | Đã điền cấu trúc; thiếu usage |
| `data/trees/tree_{A,B,C,D}.csv` | Cây IA: mỗi dòng một destination, cột `level_1`–`level_3` | `data/tree.csv` | Sinh tự động |
| `data/trees/{A,B,C,D}.txt` | Cây thụt lề bằng tab, import vào Treejack / UXtweak | — | Sinh tự động |
| `data/ia_candidates.csv` | Path của mỗi destination trên A/B/C/D | — | Sinh tự động |
| `data/tree_test_tasks.csv` | 12 task tree test + đích đúng (feature_id) | — | Bản nháp v0.1 |
| `data/tree_test_expected_paths.csv` | Đích đúng của mỗi task trên A/B/C/D | — | Sinh tự động |
| `data/tree_test_respondents.csv` | Thông tin participant tree test (bảng câu hỏi đầu/cuối) | `data/respondents.csv` | Chỉ có header |
| `data/tree_test_results.csv` | Mỗi dòng một participant × task: path, metric, câu hỏi sau task | `data/results.csv` | Chỉ có header |
| `data/card_sort_results.csv` | Card sort dạng long format | — | Chỉ có header |
| `data/usability_test_results.csv` | Mỗi dòng một participant × task | — | Chỉ có header |
| `data/ab_test_events.csv` | Sự kiện A/B | — | Chỉ có header |

### Mở rộng so với schema trong dataset

Schema gốc nằm ở `docs/literature/ux_navigation_research_dataset.md` §6–§11.

**`navigation_inventory.csv`** thêm các cột:

| Cột | Ý nghĩa |
|---|---|
| `l1_order`, `l2_order` | Thứ tự hiển thị trên sidebar |
| `label_lang` | `vi` / `en` / `mixed` |
| `audit_flags` | Phân cách bằng `;`: `DUP`, `NEAR`, `MIX`, `MISPLACED`, `CONFIG`, `PERSONAL`, `SAME_AS_PARENT` |
| `related_feature_ids` | Các mục chồng nghĩa / trùng tên, phân cách bằng `;` |

`role_primary`, `usage_frequency`, `business_criticality`, `search_rate`, `click_rate`, `avg_time_to_feature` **để trống có chủ đích**: chờ analytics, không suy đoán. `audit_flags` là đánh giá của reviewer, không phải dữ liệu người dùng.

**`tree_test_results.csv`** thêm `experience_level` và `task_ease_score` (câu hỏi sau task "Task này dễ hoàn thành" của treetest). **`tree_test_respondents.csv`** theo bảng câu hỏi trong `studies/04_tree-test/tree-test-protocol.docx`.

**`usability_test_results.csv`** thêm `presentation_order` (`A-first` / `new-first`), `issue_type` (`IA` / `label` / `interaction`), `sidebar_scrolled` (0/1) và `section_toggles` (số lần mở/đóng phân hệ); `prototype_variant` nhận `A`, `D1`, `D2`, `D3`.

## Scripts

Đánh số theo treetest: `1-x` chuẩn bị & tính toán → `2-x` phân tích khám phá → `3-x` kiểm định.

| Script | Việc | Output |
|---|---|---|
| `scripts/1-1_inventory-audit.py` | Chỉ số cấu trúc, tần suất audit flag, nhãn trùng | `results/inventory_audit.md` |
| `scripts/1-2_build-ia-candidates.py` | Định nghĩa cây A/B/C/D, kiểm tra đủ 145 destination, xuất cây và đích đúng | `data/trees/`, `data/ia_candidates.csv`, `data/tree_test_expected_paths.csv` |
| `scripts/2-1_card-sort-analysis.py` | Similarity matrix, dendrogram, cặp card tranh cãi, so sánh theo vai trò | `results/card_sort_*` |
| `scripts/3-1_tree-test-analysis.py` | Tổng hợp theo variant / task / vai trò, khoảng tin cậy Wilson, first-click matrix | `results/tree_test_summary.md` |

Kiểm định chính thức (mixed-effects model) sẽ thêm thành `3-2_tree-test-stats.R`, giống cách treetest dùng R cho kiểm định.

## Environment

Python 3.10+. Chạy trong thư mục `analysis/`:

```bash
python -m venv .venv
.venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python scripts/1-1_inventory-audit.py
python scripts/1-2_build-ia-candidates.py
python scripts/2-1_card-sort-analysis.py
python scripts/3-1_tree-test-analysis.py
```

Trên Windows, nếu console báo lỗi encoding, đặt `PYTHONIOENCODING=utf-8`.

## Quy ước

- UTF-8, dấu phẩy, dòng đầu là header.
- Binary: `0` / `1`; không áp dụng thì để trống.
- Thời gian tính bằng giây, số thập phân dùng dấu chấm.
- `path` trong tree test: các node phân cách bằng ` > `.
- Không commit thông tin định danh participant; chỉ dùng `participant_id`.
