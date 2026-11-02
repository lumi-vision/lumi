# LUMI Vision

영상에서 눈부심과 시각적 피로를 유발할 수 있는 영역을 찾아 마스크를 만들고, 해당 영역을 부분 감광하는 프로젝트입니다.

## 현재 상태

이 저장소는 **팀 협업을 위한 기본 구조**입니다. 영상 입력, 영역 탐지, 마스크 생성, 부분 감광, 모델 학습은 아직 이 저장소에 구현되지 않았습니다.
준비 상태 점검 명령만 실행할 수 있습니다. 별도 로컬 플레이어의 기능과 실험 결과를 이 저장소의 구현 또는 검증 결과로 해석하지 않습니다.

## 시작하기

Python 3.10 이상을 준비하세요. 다음은 **PowerShell에서 실행할 명령**입니다.

```powershell
git clone https://github.com/lumi-vision/lumi.git
cd lumi
python -m venv .venv
.\.venv\Scripts\python.exe scripts/check_setup.py
```

이미 내려받았다면 해당 저장소 폴더에서 마지막 두 명령을 실행하세요.
현재 점검은 Python 표준 라이브러리만 사용하며 추가 패키지 설치가 필요 없습니다.
점검 성공은 폴더·설정 준비가 됐다는 의미이며 영상 처리 성공을 뜻하지 않습니다.

## 폴더 안내

| 위치 | 역할 |
| --- | --- |
| src/lumi/ | 향후 공용 영상 처리·모델 코드 |
| configs/ | 공유 가능한 실험 설정 예시 |
| scripts/ | 준비 상태 점검 등 보조 실행 파일 |
| tests/ | 향후 탐지·마스크·감광 동작 검증 |
| experiments/ | 재현 가능한 실험 기록 |
| docs/ | 개발 환경·협업·기존 코드 통합 안내 |
| data/ | 로컬 입력 데이터; 실제 파일은 Git 제외 |
| models/ | 로컬 모델 가중치; 실제 파일은 Git 제외 |
| outputs/ | 로컬 출력 영상·마스크; 실제 파일은 Git 제외 |

## 작업 흐름

개인 실험 저장소에서 아이디어를 검증하고, 채택할 변경은 이 저장소의 새 브랜치로 옮겨 PR을 만듭니다.
작성자 외 팀원 1명의 승인을 받은 뒤 main에 병합합니다. 개인 실험 저장소의 코드가 공용 저장소에 자동 반영되지는 않습니다.

- [협업 방법](CONTRIBUTING.md)
- [개발 환경](docs/setup.md)
- [기존 플레이어 통합 계획](docs/integration.md)
- [실험 기록 양식](experiments/TEMPLATE.md)
- [데이터·모델 관리](docs/storage.md)

## 팀

| 계정 | 실험 공간 |
| --- | --- |
| Kim-GwanUk | [개인 저장소](https://github.com/lumi-vision/lumi-lab-kim-gwanuk) |
| rockrovks | [개인 저장소](https://github.com/lumi-vision/lumi-lab-rockrovks) |
| ryujungho2-collab | [개인 저장소](https://github.com/lumi-vision/lumi-lab-ryujungho2-collab) |
| hamsungdo | [개인 저장소](https://github.com/lumi-vision/lumi-lab-hamsungdo) |

역할과 코드 라이선스는 아직 팀에서 결정하지 않았습니다.
