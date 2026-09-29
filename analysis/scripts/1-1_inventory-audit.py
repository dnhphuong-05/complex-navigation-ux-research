"""Navigation audit — tính các chỉ số cấu trúc từ data/navigation_inventory.csv.

Chạy:  python scripts/1-1_inventory-audit.py   (chạy trong thư mục analysis/)
Output: results/inventory_audit.md
"""
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "data" / "navigation_inventory.csv"
OUT = ROOT / "results" / "inventory_audit.md"

FLAG_MEANING = {
    "DUP": "Trùng tên y hệt với một mục khác",
    "NEAR": "Gần nghĩa / chồng nghĩa với mục khác (semantic overlap)",
    "MIX": "Label tiếng Anh hoặc trộn Anh–Việt",
    "MISPLACED": "Nội dung có vẻ không khớp với nhóm cha",
    "CONFIG": "Mục cấu hình nằm trong module nghiệp vụ",
    "PERSONAL": "Mục cá nhân ('của tôi', hồ sơ)",
    "SAME_AS_PARENT": "Trùng tên với chính nhóm cha",
}


def load() -> pd.DataFrame:
    df = pd.read_csv(INVENTORY, dtype=str, keep_default_na=False)
    df["flags"] = df["audit_flags"].apply(lambda s: [f for f in s.split(";") if f])
    return df


def structure(df: pd.DataFrame) -> dict:
    children = df[df["current_l2"] != ""]
    per_l1 = children.groupby("current_l1", sort=False).size()
    return {
        "l1_count": df["current_l1"].nunique(),
        "l1_with_children": len(per_l1),
        "child_count": len(children),
        "total_destinations": len(df),
        "max_depth": 2 if (df["current_l3"] == "").all() else 3,
        "per_l1": per_l1,
    }


def main() -> None:
    df = load()
    s = structure(df)
    per_l1 = s["per_l1"]

    dup = (
        df[df["feature_name"].str.casefold().duplicated(keep=False)]
        .groupby("feature_name")["current_l1"]
        .apply(lambda xs: ", ".join(xs))
    )
    flags = df.explode("flags").dropna(subset=["flags"])
    flag_counts = flags["flags"].value_counts()
    flags_by_l1 = pd.crosstab(flags["current_l1"], flags["flags"]).reindex(per_l1.index).fillna(0).astype(int)
    lang = df["label_lang"].value_counts()

    lines = [
        "# Inventory audit — kết quả tự động",
        "",
        f"Nguồn: `{INVENTORY.relative_to(ROOT).as_posix()}` (chép tay từ ảnh chụp sidebar, không phải dữ liệu người dùng).",
        "",
        "## Cấu trúc",
        "",
        f"- Số mục cấp 1 (L1): **{s['l1_count']}** (trong đó {s['l1_with_children']} nhóm có mục con)",
        f"- Số mục cấp 2 (L2): **{s['child_count']}**",
        f"- Tổng destination: **{s['total_destinations']}**",
        f"- Độ sâu tối đa: **{s['max_depth']}**",
        f"- Mục con / nhóm: min {per_l1.min()}, median {per_l1.median():g}, max {per_l1.max()} ({per_l1.idxmax()})",
        "",
        "| L1 | Số mục con | " + " | ".join(flags_by_l1.columns) + " |",
        "|---|---:|" + "---:|" * len(flags_by_l1.columns),
    ]
    for l1, n in per_l1.items():
        row = " | ".join(str(v) for v in flags_by_l1.loc[l1])
        lines.append(f"| {l1} | {n} | {row} |")

    lines += ["", "## Nhãn trùng tên y hệt", "", "| Label | Xuất hiện ở |", "|---|---|"]
    lines += [f"| {name} | {where} |" for name, where in dup.items()]

    lines += ["", "## Tần suất audit flag", "", "| Flag | Ý nghĩa | Số mục |", "|---|---|---:|"]
    lines += [f"| {f} | {FLAG_MEANING.get(f, '')} | {n} |" for f, n in flag_counts.items()]

    lines += ["", "## Ngôn ngữ label", "", "| Ngôn ngữ | Số mục |", "|---|---:|"]
    lines += [f"| {k} | {v} |" for k, v in lang.items()]
    lines.append("")

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
