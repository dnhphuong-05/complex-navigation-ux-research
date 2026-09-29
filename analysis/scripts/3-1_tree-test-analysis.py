"""Tree test analysis — tổng hợp findability theo IA variant, task và role.

Input:  data/tree_test_results.csv (schema: xem analysis/README.md)
Chạy:   python scripts/3-1_tree-test-analysis.py   (chạy trong thư mục analysis/)
Output: results/tree_test_summary.md

Lưu ý: mỗi participant làm nhiều task nên các dòng KHÔNG độc lập.
Khoảng tin cậy Wilson ở đây chỉ mang tính mô tả; kiểm định chính thức xem
studies/04_tree-test/research-plan.docx, mục 9 (mixed-effects logistic model).
"""
from math import sqrt
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "tree_test_results.csv"
OUT = ROOT / "results" / "tree_test_summary.md"

BINARY = ["task_success", "direct_success", "first_click_correct"]


def wilson(successes: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return float("nan"), float("nan")
    p = successes / n
    denom = 1 + z**2 / n
    centre = (p + z**2 / (2 * n)) / denom
    half = z * sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return centre - half, centre + half


def rate_with_ci(series: pd.Series) -> str:
    s = series.dropna().astype(int)
    if s.empty:
        return "–"
    lo, hi = wilson(int(s.sum()), len(s))
    return f"{s.mean():.0%} [{lo:.0%}–{hi:.0%}]"


def summarise(df: pd.DataFrame, by: list[str]) -> pd.DataFrame:
    g = df.groupby(by)
    out = pd.DataFrame({"n": g.size(), "participants": g["participant_id"].nunique()})
    for col in BINARY:
        out[col] = g[col].apply(rate_with_ci)
    out["median_time_sec"] = g["time_to_feature_sec"].median().round(1)
    out["mean_wrong_turns"] = g["wrong_turns"].mean().round(2)
    out["mean_backtracks"] = g["backtracks"].mean().round(2)
    out["median_confidence"] = g["confidence_score"].median()
    return out.reset_index()


def to_markdown(table: pd.DataFrame) -> str:
    cols = [str(c) for c in table.columns]
    rows = ["| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
    rows += ["| " + " | ".join(str(v) for v in r) + " |" for r in table.itertuples(index=False)]
    return "\n".join(rows)


def first_click_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Task × L1 được click đầu tiên — chỉ ra nhãn nào 'hút' click sai."""
    return pd.crosstab([df["ia_variant"], df["task_id"]], df["first_level_clicked"])


def main() -> None:
    df = pd.read_csv(DATA)
    df = df.dropna(subset=["task_success"])
    if df.empty:
        print(f"{DATA.relative_to(ROOT)} chưa có dữ liệu — hãy nhập kết quả tree test trước.")
        return

    sections = [
        ("Theo IA variant", summarise(df, ["ia_variant"])),
        ("Theo variant × task", summarise(df, ["ia_variant", "task_id"])),
        ("Theo variant × role", summarise(df, ["ia_variant", "role"])),
        ("First-click matrix (task × L1 click đầu)", first_click_matrix(df).reset_index()),
    ]
    lines = ["# Tree test summary", "", "Tỉ lệ hiển thị kèm khoảng tin cậy Wilson 95% (mô tả).", ""]
    for title, table in sections:
        lines += [f"## {title}", "", to_markdown(table), ""]

    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
