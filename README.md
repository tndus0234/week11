# (프로그램 이름을 적으세요)

<!-- 예) 성적 CSV 검증기 -->

<!--
  README 여섯 항목 양식입니다. (실습 PPT 28쪽 · 학습지 ⑤와 같은 순서)
  1. 이 파일의 이름을 README.md 로 바꾼 뒤 아래 칸을 채웁니다.
  2. <!-- 로 시작하는 설명은 다 채운 뒤 지웁니다.
  3. 명령은 직접 실행해 보고, 실제로 나온 결과만 적습니다.
  4. 공개 저장소이므로 학번·연락처는 적지 않습니다. (학번은 학습지에만)
  5. 각 칸의 내용은 설명이 끝나는 줄 아래 빈 줄에 적습니다. (설명 안에 쓰면 GitHub에 보이지 않습니다)

  판정 기준: 처음 보는 사람이 이 문서만 보고 실행과 테스트를 할 수 있는가.
  (게시 후 새 폴더에 clone해 이 문서대로 직접 실행해 봅니다)
-->

## ① 무엇을 하나요 (What · 현재 상태)

<!--
  기능 한 문장 + 지금 되는 것 / 안 되는 것.
  예) 성적 CSV를 읽어 유효한 점수 목록과 제외한 행의 기록을 돌려줍니다.
      평균·학점 계산은 아직 하지 않습니다.
-->CSV 파일에서 학생 이름과 점수를 읽어 올바른 데이터와 잘못된 데이터를 구분하는 프로그램입니다.

## ② 왜 만들었나요 (Why)

<!--
  코드만 보고는 알 수 없는, 내가 직접 쓰는 칸입니다. 두세 문장.
  예) 실제 성적 파일에는 빈 칸·범위 밖 점수·글자 점수가 섞여 있어,
      그대로 읽으면 프로그램이 멈추거나 잘못된 값이 들어가기 때문입니다.
-->CSV 파일에 잘못된 점수가 포함되어 있으면 데이터를 처리할 때 오류가 발생할 수 있습니다. 따라서 유효한 점수와 잘못된 데이터를 구분하고, 제외된 이유까지 확인하기 위해 만들었습니다.

## ③ 어떻게 쓰나요 (How)

<!-- 복사해서 그대로 실행할 수 있게. 저장소 폴더의 터미널 기준. -->Python이 설치된 환경에서 다음 명령어를 순서대로 실행합니다

```
python --version
python -m pip install --user -U pytest~=7.0 pytest-cov
set PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
python load_scores.py scores.csv
```

<!-- set 줄: 강의실 PC처럼 옛 Anaconda가 깔린 PC에서 pytest 플러그인 오류를 막습니다.
     새 터미널을 열 때마다 pytest 전에 한 번 입력합니다. -->

예상 결과: 읽은 줄 5개 건너뛴 줄 5개

## ④ 어떻게 테스트하나요

```
python -m pytest test_load_scores.py -q
```

실제 결과:12 passed 

<!-- 예) 12 passed (기본 11개 + weird.csv 보강 1개)
     예) test_bug_A.py·test_bug_B.py는 find_max 버그를 찾아 2개씩 실패 -->- 12 passed 실패 0개 커버리지 80%

<!-- AI 실험 파일(test_bug_A.py, test_bug_B.py, 선택: test_ai_draft.py)은 비교용 원본입니다.
     일부 실패할 수 있으며, 그 이유를 한 줄로 적어 두세요. -->

## ⑤ 파일 구성

| 파일 | 하는 일 |
| --- | --- |
| load_scores.py | (예: CSV를 읽어 (kept, skipped)를 돌려주는 함수) |
| scores.csv · empty.csv · weird.csv |  |
| test_load_scores.py |  |
| test_ai_draft.py (선택 실험을 했다면) |  |
| bug3_logic.py · test_bug_A.py · test_bug_B.py |  |

## ⑥ 만든 사람과 AI 사용

- 만든 사람 : tndus0234
- 사용한 AI 도구·모델 :VS Code Copilot Chat / Copilot Fusion
- AI에게 도움받은 부분 :find_max 함수의 pytest 테스트 코드 생성
- 내가 직접 판단·확인한 부분 :명세에 따른 기대값 결정, 테스트 실행 결과 비교, 오류 분석, 커버리지 측정

## 라이선스

MIT License (LICENSE 파일 참고)
