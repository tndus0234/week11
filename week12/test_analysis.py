import pandas as pd

from analysis import 정제, 반별평균


scores_df = pd.read_csv("scores_2026.csv", encoding="utf-8")
mini_df = pd.read_csv("mini.csv", encoding="utf-8")

cleaned_scores_df = 정제(scores_df)
cleaned_mini_df = 정제(mini_df)


def test_scores_2026_has_100_cleaned_rows():
    assert len(cleaned_scores_df) == 100


def test_cleaned_classes_are_1반_and_2반():
    assert set(cleaned_scores_df["반"].unique()) == {"1반", "2반"}


def test_class_score_sums_equal_total_score_sum():
    class_score_sum = cleaned_scores_df.groupby("반")["점수"].sum().sum()
    total_score_sum = cleaned_scores_df["점수"].sum()
    assert class_score_sum == total_score_sum


def test_mini_class_1_average_is_80():
    assert 반별평균(cleaned_mini_df)["1반"] == 80.0