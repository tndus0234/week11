
import pandas as pd

def 정제(df):
    # 원본 데이터 복사
    정제_df = df.copy()
    print("시작:", len(정제_df), "행")

    # 1단계: 빈칸 제거
    정제_df = 정제_df.dropna(subset=["점수"])
    print("점수 결측 행 삭제 후:", len(정제_df), "행")

    # 2단계: 중복 제거
    정제_df = 정제_df.drop_duplicates()
    print("중복 행 삭제 후:", len(정제_df), "행")

    # 3단계: 공백 제거
    정제_df["반"] = 정제_df["반"].str.strip()
    정제_df["과목"] = 정제_df["과목"].str.strip()
    print("공백 제거 후:", len(정제_df), "행")

    # 4단계: 0~100 사이의 정수만 남기기
    유효한_점수 = 정제_df["점수"].between(0, 100) & (정제_df["점수"] % 1 == 0)
    정제_df = 정제_df[유효한_점수]
    print("점수 범위 적용 후:", len(정제_df), "행")

    return 정제_df


df = 정제(pd.read_csv("scores_2026.csv"))

print("반:", sorted(df["반"].unique()))
print("과목:", sorted(df["과목"].unique()))

수학_df = df[df["과목"] == "수학"]
print("수학 남은 행 수:", len(수학_df))

반1_90점이상_df = df[(df["반"] == "1반") & (df["점수"] >= 90)]
print("1반에서 90점 이상:", len(반1_90점이상_df))




반별_평균 = df.groupby("반")["점수"].mean()
print(반별_평균)

과목_반별_평균 = df.groupby(["과목", "반"])["점수"].mean()
print(과목_반별_평균)


def 반별평균(df):
    반별_통계 = df.groupby("반")["점수"].agg(
        ["count", "mean", "median", "max"]
    ).round(2)
    반별_통계.columns = ["개수", "평균", "중앙값", "최댓값"]
    print(반별_통계)
    return 반별_통계["평균"]


반별평균(df)




print("그룹 합계:", df.groupby("반")["점수"].sum().sum())
print("전체 합계:", df["점수"].sum())

print("그룹 개수:", df.groupby("반")["점수"].count().sum())
print("전체 개수:", len(df))


print("1반 수학 점수:")
print(df[(df["반"] == "1반") & (df["과목"] == "수학")]["점수"])

미니 = 정제(pd.read_csv("mini.csv"))

print("미니 데이터 반별 평균:")
print(반별평균(미니))



