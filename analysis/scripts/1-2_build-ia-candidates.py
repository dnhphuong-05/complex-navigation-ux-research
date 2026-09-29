"""Định nghĩa IA candidate A/B/C và xuất cây cho tree test.

Candidate A/B/C/D dùng CÙNG tập 145 destination trong data/navigation_inventory.csv
(dataset §5: "2–3 IA structures with different breadth/depth but same destination set").
Script dừng với lỗi nếu có destination bị thiếu hoặc lặp.

Chạy:   python scripts/1-2_build-ia-candidates.py   (chạy trong thư mục analysis/)
Output: data/ia_candidates.csv            feature_id → path ở A, B, C, D
        data/trees/{A,B,C,D}.txt            cây thụt lề (import được vào Treejack/UXtweak)
        data/trees/tree_{A,B,C,D}.csv       cây dạng bảng: mỗi dòng một destination, cột level_1..3
        data/tree_test_expected_paths.csv  đích đúng của từng task (từ data/tree_test_tasks.csv)
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "data" / "navigation_inventory.csv"
OUT_CSV = ROOT / "data" / "ia_candidates.csv"
TREES = ROOT / "data" / "trees"
TASKS = ROOT / "data" / "tree_test_tasks.csv"
OUT_EXPECTED = ROOT / "data" / "tree_test_expected_paths.csv"

# Node = (label, feature_id) cho lá; (label, [children]) cho nhóm.
# Nhãn trong B/C là bản nháp — cập nhật theo card sort trước khi tree test.

B_KHACH_HANG = [
    ("Tổng quan khách hàng", "F001"),
    ("Liên hệ", "F002"),
    ("Nhập liên hệ", "F008"),
    ("Doanh nghiệp", "F003"),
    ("Khách tiềm năng (Lead)", "F004"),
    ("Bảng kanban khách hàng", "F005"),
    ("Danh sách khách hàng", "F012"),
    ("Sức khoẻ khách hàng", "F011"),
    ("Cảnh báo khách hàng", "F013"),
    ("Gộp dữ liệu trùng", "F009"),
]
B_THUONG_VU = [
    ("Cơ hội bán", "F014"),
    ("Bảng kanban thương vụ", "F016"),
    ("Danh sách thương vụ", "F017"),
    ("Thắng / Thua", "F021"),
    ("Lý do thất bại", "F029"),
    ("Báo cáo phễu bán hàng", "F015"),
]
B_BAO_GIA = [("Báo giá", "F038"), ("Yêu cầu chờ duyệt", "F028")]
B_DU_BAO = [
    ("Dự báo doanh số", "F019"),
    ("Mô phỏng doanh số (what-if)", "F020"),
    ("Chỉ tiêu (hạn ngạch)", "F022"),
]
B_HOA_HONG = [("Kế hoạch hoa hồng", "F024"), ("Chi trả hoa hồng nhân viên", "F025")]
MY_ITEMS = [
    ("Việc cần làm của tôi", "F010"),
    ("Chỉ tiêu của tôi", "F023"),
    ("Hoa hồng của tôi", "F026"),
]
SAN_PHAM = [
    ("Sản phẩm", "F030"),
    ("Danh mục sản phẩm", "F031"),
    ("Bảng giá", "F032"),
    ("Chiết khấu", "F033"),
    ("Combo", "F035"),
    ("Tồn kho", "F034"),
    ("Đơn hàng", "F036"),
    ("Báo cáo đơn hàng", "F037"),
]
THU_TIEN = [
    ("Hoá đơn", "F039"),
    ("Thanh toán", "F041"),
    ("Giao dịch SePay", "F044"),
    ("Công nợ theo tuổi nợ", "F040"),
    ("Đối soát", "F042"),
]
HOP_DONG = [("Chữ ký điện tử", "F046")]
KE_TOAN = [
    ("Tổng quan tài chính", "F085"),
    ("Báo cáo lãi lỗ (P&L)", "F086"),
    ("Bảng cân đối", "F087"),
    ("Lưu chuyển tiền tệ", "F088"),
    ("Hệ thống tài khoản kế toán", "F089"),
    ("Bút toán", "F090"),
    ("Ngân sách", "F091"),
    ("Trung tâm chi phí", "F092"),
]
EMAIL = [
    ("Tổng quan email", "F047"),
    ("Chiến dịch email", "F053"),
    ("Chuỗi email", "F051"),
    ("Mẫu email", "F054"),
    ("Người đăng ký", "F048"),
    ("Danh sách email", "F049"),
    ("Phân khúc", "F056"),
    ("Biểu mẫu", "F057"),
    ("Báo cáo email", "F050"),
]
LANDING = [
    ("Sơ đồ phễu marketing", "F058"),
    ("Trang đích", "F059"),
    ("Mã QR", "F060"),
    ("Link UTM", "F061"),
]
LEAD_MKT = [
    ("Chấm điểm lead", "F065"),
    ("Phân công lead", "F066"),
    ("Nguồn lead", "F127"),
    ("Hành trình khách hàng", "F124"),
    ("Nguồn & hành trình", "F125"),
    ("Quy tắc ghi nhận chuyển đổi", "F128"),
]
AFFILIATE = [
    ("Tổng quan affiliate", "F095"),
    ("Đại lý", "F096"),
    ("Link giới thiệu", "F097"),
    ("Chuyển đổi affiliate", "F098"),
    ("Chi trả hoa hồng đại lý", "F099"),
]
HOI_THOAI = [("Hộp thư", "F067"), ("SMS", "F069"), ("Zalo ZNS", "F071")]
BAO_CAO = [
    ("Trang chủ báo cáo", "F073"),
    ("Bảng điều khiển", "F074"),
    ("Tổng quan hiệu suất", "F094"),
    ("Báo cáo", "F075"),
    ("Mẫu báo cáo", "F076"),
    ("Lịch gửi báo cáo", "F077"),
    ("Xuất dữ liệu", "F078"),
    ("Mô phỏng what-if", "F080"),
]
MUC_TIEU = [
    ("KPI Tree", "F079"),
    ("OKR", "F082"),
    ("Cây liên kết mục tiêu", "F083"),
    ("Check-ins", "F084"),
    ("Hiệu suất phòng ban & team", "F081"),
    ("Đánh giá độ trưởng thành", "F093"),
]
TU_DONG = [("Luồng tự động", "F062"), ("Mẫu luồng", "F063"), ("Lịch sử chạy luồng", "F064")]
TRO_LY_AI = [
    ("Trợ lý AI", "F101"),
    ("Lịch sử trò chuyện", "F102"),
    ("Kho kiến thức", "F108"),
    ("Tìm tài liệu", "F109"),
    ("Checklists", "F110"),
]
CANH_BAO = [("Cảnh báo hệ thống", "F105"), ("Thông báo", "F107")]
TO_CHUC = [
    ("Nhân sự", "F130"),
    ("Sơ đồ tổ chức", "F131"),
    ("Phòng ban", "F132"),
    ("Vị trí / chức danh", "F133"),
    ("Dự án nội bộ", "F134"),
    ("Gantt portfolio", "F135"),
    ("ROI dự án", "F136"),
]
CAI_DAT_SECTIONS = [
    ("Người dùng & bảo mật", [
        ("Đội nhóm", "F139"),
        ("Vai trò", "F141"),
        ("Phân quyền", "F142"),
        ("Bảo mật", "F138"),
        ("Nhật ký kiểm toán", "F143"),
        ("Quản trị toàn hệ thống", "F144"),
    ]),
    ("Cấu hình dữ liệu", [
        ("Trường tuỳ chỉnh", "F006"),
        ("Thẻ", "F007"),
        ("Pipeline bán hàng", "F018"),
        ("Quy trình phê duyệt", "F027"),
    ]),
    ("Kênh gửi", [
        ("Tài khoản email", "F052"),
        ("Biến email", "F055"),
        ("Tài khoản SMS", "F070"),
        ("Zalo OA", "F072"),
        ("Quy tắc hộp thư", "F068"),
    ]),
    ("Thanh toán", [("Cài đặt thanh toán", "F045"), ("Tài khoản SePay", "F043")]),
    ("Affiliate", [("Cài đặt affiliate", "F100")]),
    ("AI", [
        ("Cấu hình AI", "F104"),
        ("Kết nối AI", "F112"),
        ("Mức dùng AI", "F103"),
        ("Quy tắc cảnh báo", "F106"),
    ]),
    ("Tích hợp", [
        ("Google", "F116"),
        ("Google Analytics", "F117"),
        ("Google Sheets", "F118"),
        ("Đồng bộ Sheet", "F119"),
        ("WEDU sync", "F120"),
        ("Kênh kết nối", "F122"),
        ("Webhook", "F129"),
        ("Webhook đẩy ra", "F126"),
        ("Nhật ký đồng bộ", "F121"),
        ("Website & app theo dõi", "F123"),
    ]),
    ("Nhà phát triển", [
        ("API & MCP", "F111"),
        ("MCP", "F113"),
        ("API docs", "F114"),
        ("CLI", "F115"),
    ]),
]

# Candidate B — Regroup theo domain: 11 nhóm + Trợ giúp, section header trong nhóm lớn,
# cấu hình gom về Cài đặt, nhãn trùng được phân biệt.
CANDIDATE_B = [
    ("Tổng quan", "F000"),
    ("Khách hàng", B_KHACH_HANG + [MY_ITEMS[0]]),
    ("Bán hàng", [
        ("Thương vụ", B_THUONG_VU),
        ("Báo giá & phê duyệt", B_BAO_GIA),
        ("Dự báo & chỉ tiêu", B_DU_BAO + [MY_ITEMS[1]]),
        ("Hoa hồng nhân viên", B_HOA_HONG + [MY_ITEMS[2]]),
    ]),
    ("Sản phẩm & Đơn hàng", SAN_PHAM),
    ("Tài chính", [("Thu tiền", THU_TIEN), ("Hợp đồng", HOP_DONG), ("Kế toán", KE_TOAN)]),
    ("Marketing", [
        ("Email", EMAIL),
        ("Landing & phễu marketing", LANDING),
        ("Khách tiềm năng", LEAD_MKT),
        ("Affiliate", AFFILIATE),
    ]),
    ("Hội thoại", HOI_THOAI),
    ("Báo cáo & Mục tiêu", [("Báo cáo", BAO_CAO), ("Mục tiêu & KPI", MUC_TIEU)]),
    ("Tự động hoá & AI", [
        ("Tự động hoá", TU_DONG),
        ("Trợ lý AI", TRO_LY_AI),
        ("Cảnh báo & thông báo", CANH_BAO),
    ]),
    ("Tổ chức", TO_CHUC),
    ("Cài đặt", [("Tài khoản của tôi", [("Hồ sơ", "F140")])] + CAI_DAT_SECTIONS),
    ("Trợ giúp", "F137"),
]

# Candidate C — Global (không gian làm việc) + contextual sidebar + "Của tôi".
# Trong UI, section là header không click được; trong tree test được mô hình hoá như node.
CANDIDATE_C = [
    ("Tổng quan", "F000"),
    ("Của tôi", MY_ITEMS + [("Hồ sơ", "F140")]),
    ("Bán hàng", [
        ("Khách hàng", B_KHACH_HANG),
        ("Thương vụ", B_THUONG_VU),
        ("Báo giá & phê duyệt", B_BAO_GIA),
        ("Dự báo & chỉ tiêu", B_DU_BAO),
        ("Hoa hồng nhân viên", B_HOA_HONG),
        ("Sản phẩm & đơn hàng", SAN_PHAM),
    ]),
    ("Marketing", [
        ("Email", EMAIL),
        ("Landing & phễu marketing", LANDING),
        ("Khách tiềm năng", LEAD_MKT),
        ("Affiliate", AFFILIATE),
        ("Hội thoại", HOI_THOAI),
    ]),
    ("Tài chính", [("Thu tiền", THU_TIEN), ("Hợp đồng", HOP_DONG), ("Kế toán", KE_TOAN)]),
    ("Vận hành", [
        ("Báo cáo", BAO_CAO),
        ("Mục tiêu & KPI", MUC_TIEU),
        ("Tự động hoá", TU_DONG),
        ("Trợ lý AI", TRO_LY_AI),
        ("Cảnh báo & thông báo", CANH_BAO),
        ("Tổ chức", TO_CHUC),
    ]),
    ("Cài đặt", CAI_DAT_SECTIONS),
    ("Trợ giúp", "F137"),
]

# Candidate D — Kiến trúc nhiều tầng theo ứng dụng (suite): tầng 0 thanh công cụ toàn cục,
# tầng 1 ứng dụng (CRM, Marketing, ERP, HRM…), tầng 2 phân hệ, tầng 3 chức năng.
# Lập luận và dẫn chứng: design/navigation-architecture-proposal.docx.
D_QUAN_TRI = [
    (name, [("Kho kiến thức AI", "F108") if fid == "F106" else (label, fid) for label, fid in items])
    if name == "AI" else (name, items)
    for name, items in CAI_DAT_SECTIONS
]
CANDIDATE_D = [
    # Tầng 1 — ứng dụng nghiệp vụ
    ("Trang chủ", [("Tổng quan", "F000"), ("Của tôi", MY_ITEMS)]),
    ("Bán hàng (CRM)", [
        ("Khách hàng", B_KHACH_HANG),
        ("Thương vụ", B_THUONG_VU),
        ("Báo giá & phê duyệt", B_BAO_GIA),
        ("Dự báo & chỉ tiêu", B_DU_BAO),
        ("Hoa hồng nhân viên", B_HOA_HONG),
        ("Hội thoại", HOI_THOAI),
    ]),
    ("Marketing", [
        ("Email", EMAIL),
        ("Landing & phễu marketing", LANDING),
        ("Khách tiềm năng", LEAD_MKT),
        ("Affiliate", AFFILIATE),
    ]),
    ("Đơn hàng & Tài chính (ERP)", [
        ("Sản phẩm & kho", [f for f in SAN_PHAM if f[1] not in ("F036", "F037")]),
        ("Đơn hàng", [f for f in SAN_PHAM if f[1] in ("F036", "F037")]),
        ("Thu tiền", THU_TIEN),
        ("Hợp đồng", HOP_DONG),
        ("Kế toán", KE_TOAN),
    ]),
    ("Nhân sự (HRM)", [
        ("Tổ chức", TO_CHUC[:4]),
        ("Dự án nội bộ", TO_CHUC[4:]),
        ("Quy trình", [("Checklists", "F110")]),
    ]),
    ("Báo cáo & Mục tiêu", [("Báo cáo", BAO_CAO), ("Mục tiêu & KPI", MUC_TIEU)]),
    # Tầng 1 — ứng dụng nền tảng
    ("Tự động hoá", [("Luồng", TU_DONG), ("Quy tắc", [("Quy tắc cảnh báo", "F106")])]),
    ("Quản trị", D_QUAN_TRI),
    # Tầng 0 — thanh công cụ toàn cục (mô hình hoá như node cấp 1 trong tree test)
    ("Trợ lý AI", [("Trò chuyện", "F101"), ("Lịch sử trò chuyện", "F102"), ("Tìm tài liệu", "F109")]),
    ("Thông báo", [("Thông báo", "F107"), ("Cảnh báo hệ thống", "F105")]),
    ("Tài khoản", [("Hồ sơ", "F140")]),
    ("Trợ giúp", "F137"),
]


def candidate_a(inv: pd.DataFrame) -> list:
    """Cây hiện tại, dựng lại từ inventory."""
    tree = []
    for l1, grp in inv.groupby("current_l1", sort=False):
        if (grp["current_l2"] == "").all():
            tree.append((l1, grp["feature_id"].iloc[0]))
        else:
            tree.append((l1, list(zip(grp["feature_name"], grp["feature_id"]))))
    return tree


def walk(tree: list, prefix: tuple = ()):
    for label, child in tree:
        path = prefix + (label,)
        if isinstance(child, str):
            yield child, path
        else:
            yield from walk(child, path)


def indented(tree: list, depth: int = 0):
    for label, child in tree:
        yield "\t" * depth + label
        if not isinstance(child, str):
            yield from indented(child, depth + 1)


def main() -> None:
    inv = pd.read_csv(INVENTORY, dtype=str, keep_default_na=False)
    ids = set(inv["feature_id"])
    candidates = {"A": candidate_a(inv), "B": CANDIDATE_B, "C": CANDIDATE_C, "D": CANDIDATE_D}

    out = inv[["feature_id", "feature_name"]].copy()
    TREES.mkdir(parents=True, exist_ok=True)
    for name, tree in candidates.items():
        leaves = list(walk(tree))
        found = [fid for fid, _ in leaves]
        missing, extra = ids - set(found), set(found) - ids
        dupes = {f for f in found if found.count(f) > 1}
        if missing or extra or dupes:
            raise SystemExit(f"Candidate {name}: missing={sorted(missing)} extra={sorted(extra)} dup={sorted(dupes)}")
        paths = {fid: " > ".join(p) for fid, p in leaves}
        depths = [len(p) for _, p in leaves]
        out[f"{name}_path"] = out["feature_id"].map(paths)
        (TREES / f"{name}.txt").write_text("\n".join(indented(tree)) + "\n", encoding="utf-8")
        # Định dạng tree.csv của treetest-research: mỗi dòng một destination, mỗi cột một cấp.
        pd.DataFrame(
            [{"feature_id": fid, **{f"level_{k + 1}": (p[k] if k < len(p) else "") for k in range(3)}} for fid, p in leaves]
        ).to_csv(TREES / f"tree_{name}.csv", index=False, encoding="utf-8")
        print(f"{name}: {len(tree)} mục cấp 1, {len(leaves)} destination, depth max {max(depths)}, "
              f"depth trung bình {sum(depths) / len(depths):.2f}")

    out.to_csv(OUT_CSV, index=False, encoding="utf-8")
    print(f"Wrote {OUT_CSV.relative_to(ROOT)} và {TREES.relative_to(ROOT)}/")
    expected_paths(out.set_index("feature_id"), list(candidates))


def expected_paths(paths: pd.DataFrame, variants: list[str]) -> None:
    """Đích đúng / chấp nhận được của mỗi tree-test task trên từng candidate."""
    tasks = pd.read_csv(TASKS, dtype=str, keep_default_na=False)
    rows = []
    for t in tasks.itertuples():
        for kind, col in (("correct", t.correct_feature_ids), ("acceptable", t.acceptable_feature_ids)):
            for fid in filter(None, col.split(";")):
                rows.append({"task_id": t.task_id, "kind": kind, "feature_id": fid,
                             **{f"{v}_path": paths.loc[fid, f"{v}_path"] for v in variants}})
    pd.DataFrame(rows).to_csv(OUT_EXPECTED, index=False, encoding="utf-8")
    print(f"Wrote {OUT_EXPECTED.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
