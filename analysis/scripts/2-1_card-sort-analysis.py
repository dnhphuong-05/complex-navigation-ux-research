"""Card sort analysis — co-occurrence, hierarchical clustering, so sánh theo role.

Input:  data/card_sort_results.csv (long format: participant_id, role, card_id, card_label, group_label)
Chạy:   python scripts/2-1_card-sort-analysis.py   (chạy trong thư mục analysis/)
Output: results/card_sort_similarity.csv, results/card_sort_dendrogram.png,
        results/card_sort_similarity_<role>.csv

Cluster chỉ là bằng chứng về mental model — KHÔNG copy thẳng thành menu cuối.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from scipy.spatial.distance import squareform

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "card_sort_results.csv"
RESULTS = ROOT / "results"


def similarity(df: pd.DataFrame) -> pd.DataFrame:
    """% participant đặt 2 card vào cùng nhóm."""
    labels = sorted(df["card_label"].unique())
    sim = pd.DataFrame(0.0, index=labels, columns=labels)
    participants = df["participant_id"].unique()
    for _, p in df.groupby("participant_id"):
        for _, grp in p.groupby("group_label"):
            cards = grp["card_label"].tolist()
            sim.loc[cards, cards] += 1
    return sim / len(participants)


def plot_dendrogram(sim: pd.DataFrame, path: Path) -> None:
    dist = 1 - sim.to_numpy()
    for i in range(len(dist)):
        dist[i, i] = 0
    z = linkage(squareform(dist, checks=False), method="average")
    fig, ax = plt.subplots(figsize=(8, max(4, len(sim) * 0.25)))
    dendrogram(z, labels=sim.index.tolist(), orientation="right", ax=ax)
    ax.set_xlabel("Khoảng cách (1 − tỉ lệ cùng nhóm)")
    fig.tight_layout()
    fig.savefig(path, dpi=150)
    plt.close(fig)


def main() -> None:
    df = pd.read_csv(DATA).dropna(subset=["group_label"])
    if df.empty:
        print(f"{DATA.relative_to(ROOT)} chưa có dữ liệu — hãy nhập kết quả card sort trước.")
        return
    RESULTS.mkdir(exist_ok=True)

    sim = similarity(df)
    sim.round(3).to_csv(RESULTS / "card_sort_similarity.csv", encoding="utf-8")
    plot_dendrogram(sim, RESULTS / "card_sort_dendrogram.png")

    for role, part in df.groupby("role"):
        similarity(part).round(3).to_csv(RESULTS / f"card_sort_similarity_{role}.csv", encoding="utf-8")

    # Các cặp card mà mental model chia rẽ nhất (gần 50%) — ứng viên cho cross-link hoặc đổi label
    pairs = sim.where(lambda m: pd.DataFrame(
        [[i < j for j in range(len(m))] for i in range(len(m))], index=m.index, columns=m.columns
    )).stack()
    contested = pairs[(pairs >= 0.35) & (pairs <= 0.65)].sort_values(ascending=False)
    print("Cặp card gây tranh cãi (35–65% cùng nhóm):")
    print(contested.head(20).to_string())


if __name__ == "__main__":
    main()
