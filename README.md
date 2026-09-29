# complex-navigation-ux-research

Nơi lưu toàn bộ tài liệu nghiên cứu UX về **navigation nhiều cấp của AI CRM All-in-One**. Sidebar hiện có 14 nhóm cấp 1 và 144 chức năng cấp 2. Repo là nơi tập trung để tra cứu study, kết quả, hướng dẫn và phương pháp cho những ai muốn đóng góp và hiểu rõ hơn về người dùng.

> **Câu hỏi nghiên cứu chính:** Làm thế nào để tổ chức một hệ thống có số lượng chức năng lớn và nhiều lớp sao cho người dùng tìm đúng tính năng nhanh, hiểu rõ cấu trúc và giảm navigation effort?

## Repo này có gì

Cấu trúc theo 4 repo mẫu:

| Repo mẫu | Lấy gì | Ở đâu trong repo này |
|---|---|---|
| [jupyterlab/ux-research](https://github.com/jupyterlab/ux-research) | Trang chủ repo, *Research types*, *The research process*, mỗi study một thư mục, research plan + final report, peer review, *Guidelines for Sharing* | `README.md`, `docs/`, `studies/`, `templates/research-summary-template.docx` |
| [18F/ux-guide](https://github.com/18F/ux-guide/tree/main/_pages/research) | Template trong `_pages/resources/`: research plan, interview guide, interview checklist, debrief guide, usability test guide, participant agreement, rolling issues log, usability test quality heuristics | `templates/` |
| [uxagencies/ux-project-templates](https://github.com/uxagencies/ux-project-templates) | `ux-research-plan-template.md` (11 mục), `CHEATSHEET.md` | `templates/research-plan-template.docx`, `docs/method-cheatsheet.docx` |
| [treetest-research/information-architecture-validation](https://github.com/treetest-research/information-architecture-validation) | `analysis/` gồm `data/raw/` + dữ liệu đã xử lý (respondents / results / tree) + `scripts/` đánh số 1-x → 2-x → 3-x; thông điệp và bảng câu hỏi tree test | `analysis/`, `templates/tree-test-protocol-template.docx` |

```text
.
├── README.md                              Trang chủ (file này)
├── docs/                                  Lý thuyết & phương pháp
│   ├── research-types.docx                Các loại nghiên cứu (JupyterLab) — áp dụng cho dự án
│   ├── research-process.docx              Problem statement → giả định → giả thuyết H01–H08 (JupyterLab)
│   ├── method-cheatsheet.docx             Chọn phương pháp & cỡ mẫu (uxagencies)
│   └── literature/
│       └── ux_navigation_research_dataset.md   Tổng quan tài liệu + schema (đọc được bằng Python)
├── templates/                             Template trống — sao chép khi tạo study mới
│   ├── research-plan-template.docx        uxagencies 11 mục + 18F
│   ├── participant-screener-template.docx JupyterLab + 18F
│   ├── participant-agreement-template.docx  18F
│   ├── interview-guide-template.docx      18F
│   ├── interview-checklist.docx           18F
│   ├── interview-debrief-template.docx    18F
│   ├── usability-test-guide-template.docx 18F
│   ├── usability-test-quality-heuristics.docx  18F
│   ├── rolling-issues-log-template.docx   18F
│   ├── tree-test-protocol-template.docx   treetest-research
│   ├── research-summary-template.docx     JupyterLab — Guidelines for Sharing
│   └── final-report-template.docx         18F + JupyterLab + uxagencies
├── studies/                               Mỗi study một thư mục (JupyterLab)
│   ├── 00_program/                        research-summary.docx (tóm tắt 2 trang gửi quản lý) · research-plan.docx · participant-agreement.docx
│   ├── 01_navigation-audit/               heuristic-evaluation-report.docx · evidence/sidebar-screenshots/
│   ├── 02_user-interviews/                research-plan.docx · participant-screener.docx · interview-guide.docx
│   ├── 03_card-sort/                      research-plan.docx (kèm bộ 50 card)
│   ├── 04_tree-test/                      research-plan.docx · tree-test-protocol.docx
│   ├── 05_usability-test/                 research-plan.docx · usability-test-guide.docx · rolling-issues-log.docx
│   └── 06_ab-test/                        research-plan.docx
├── design/                                Artifact thiết kế
│   ├── ia-candidates.docx                 Phương án IA A · B · C · D
│   ├── solution-proposal.docx             Đề xuất giải pháp 3 tầng
│   ├── navigation-architecture-proposal.docx  Kiến trúc Ứng dụng › Phân hệ › Chức năng + dẫn chứng (v0.2)
│   └── ui-design-proposal.docx            Đặc tả UI: rail, sidebar, 3 biến thể, thành phần, màu, mobile
└── analysis/                              Dữ liệu & script (treetest-research) — xem analysis/README.md
    ├── data/  (raw/ · navigation_inventory.csv · tree_test_*.csv · trees/ …)
    ├── scripts/  (1-1_ … 3-1_)
    └── results/
```

Tài liệu nghiên cứu ở dạng **Word (.docx)**. Chỉ hai README và file dataset là Markdown: GitHub hiển thị README trực tiếp, còn dataset được script Python đọc.

## Mockup

Canvas bấm thử được (riêng tư — chia sẻ qua menu Share): https://claude.ai/artifact/2QwR1VDtHVV9Bnipx9bzie — 3 biến thể sidebar D1/D2/D3, bộ thành phần UI, tìm kiếm Ctrl K, 3 màn hình mobile, phương án A và B. **Không cho participant xem trước khi test.**

## Trạng thái các study

| Study | Loại (JupyterLab) | Trạng thái | Tài liệu chính |
|---|---|---|---|
| 00 Kế hoạch tổng | — | ✅ v0.2 | `studies/00_program/research-plan.docx` |
| 01 Navigation audit | Nền tảng | ✅ Sơ bộ (chưa có analytics) | `studies/01_navigation-audit/heuristic-evaluation-report.docx` |
| 02 Phỏng vấn | Mô tả | ⏳ Sẵn sàng tuyển | `studies/02_user-interviews/` |
| 03 Card sort | Tạo sinh | ⏳ Bộ card v0.1 | `studies/03_card-sort/research-plan.docx` |
| 04 Tree test | Đánh giá | ⏳ Task + đích đúng sẵn sàng | `studies/04_tree-test/` |
| 05 Usability test | Đánh giá | ⏳ Guide sẵn sàng | `studies/05_usability-test/` |
| 06 A/B test | Đánh giá | 📝 Phác thảo | `studies/06_ab-test/research-plan.docx` |

## Phát hiện sơ bộ (Study 01)

Theo *Guidelines for Sharing* của JupyterLab. Đây là **nhận định của reviewer**, chưa phải dữ liệu người dùng.

- Luồng tự động nằm trong *Landing & Phễu*, không nằm trong nhóm *AI & Tự động hoá*.
- *Báo cáo & Hiệu suất* (22 mục) trộn báo cáo, OKR/KPI và kế toán.
- 5 cặp nhãn trùng tên y hệt; nhiều khái niệm (lead, hoa hồng, phòng ban) nằm ở nhiều nhóm.
- Sidebar giống nhau cho mọi vai trò.

**Liên kết:** research plan tổng (`studies/00_program/research-plan.docx`) · báo cáo (`studies/01_navigation-audit/heuristic-evaluation-report.docx`) · đề xuất (`design/solution-proposal.docx`).

**Bước tiếp theo:** lấy analytics 90 ngày · kiểm tra nghĩa 7 mục mơ hồ trong sản phẩm · tuyển participant cho Study 02.

## Hướng dẫn đóng góp (theo JupyterLab)

### Tạo study mới

1. Tạo thư mục `studies/0x_<tên-study>/`.
2. Sao chép `templates/research-plan-template.docx` thành `research-plan.docx` và điền đủ 11 mục.
3. Thêm screener, script / guide từ `templates/`.
4. Sau khi phân tích: gửi research summary (`templates/research-summary-template.docx`) và viết final report (`templates/final-report-template.docx`).

### Peer review

Theo quy trình của JupyterLab, ba loại tài liệu **bắt buộc peer review**:

- Participant screener
- Test plan (research plan và tài liệu đi kèm: script, khảo sát, card sort…)
- Final report

Review không đồng bộ, qua comment trong Word hoặc pull request. Khi đóng một góp ý, ghi lý do để khép lại vấn đề. Chủ tài liệu quyết định áp dụng góp ý nào. Mỗi tài liệu có bảng *Peer review* ở cuối.

### Chia sẻ kết quả

Khi chạy xong một study, researcher chịu trách nhiệm lan toả insight:

- Tóm tắt ngắn những gì đã làm.
- 3–4 gạch đầu dòng insight chính, câu thật ngắn.
- Link tới research plan, báo cáo, issue nghiên cứu và các việc cần làm đang theo dõi.
- Mục *Bước tiếp theo*, mỗi dòng là link tới một issue có thể hành động.

### Dữ liệu participant

Repo chỉ chứa `participant_id` (P001…). Bảng đối chiếu tên ↔ ID, bản ghi hình và thoả thuận đã ký lưu ngoài repo (18F: privacy).

## Chạy phân tích

Xem `analysis/README.md`.

```bash
cd analysis
pip install -r requirements.txt
python scripts/1-1_inventory-audit.py
python scripts/1-2_build-ia-candidates.py
```
