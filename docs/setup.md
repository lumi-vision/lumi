# 개발 환경

## 기본 환경

- Python 3.10 이상
- Git
- 팀원 본인의 GitHub 계정과 저장소 Write 권한

PowerShell에서 저장소 루트로 이동한 뒤 실행합니다.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe scripts/check_setup.py
```

가상환경 활성화 없이 위 경로로 Python을 직접 실행할 수 있습니다.
현재 requirements.txt에는 외부 의존성이 없습니다.
영상 처리나 학습 모듈을 통합할 때 실제 사용 패키지와 확인한 버전을 기록합니다.

## 설정

configs/example.json은 향후 영상 처리 경로를 정하기 위한 예시입니다.
저장소 루트 기준 상대 경로를 사용합니다.
이 설정을 소비하는 영상 처리 실행기는 아직 없습니다.
점검 명령은 설정에 필요한 키가 있는지만 확인하며 입력 영상이나 모델을 내려받지 않습니다.

## 코드 작성 위치

Python 코드는 src/lumi/ 아래 파일에 작성합니다.
scripts/check_setup.py는 환경 점검용 실행 파일입니다.
터미널 명령을 Python 소스 안에 붙여 넣지 않습니다.
