# 기존 플레이어 통합 계획

## 현재 분리된 상태

관리자의 로컬 D:\루미에는 app.py, auto_roi.py, processing.py 등의 별도 플레이어 코드가 있습니다.
2026-11-02에 해당 폴더의 README와 파일 목록을 확인했습니다.
이 기본 구조 PR에서는 그 코드를 복사하거나 실행하지 않았으며, 설명된 기능과 결과를 재검증하지 않았습니다.

## 제안하는 통합 위치

| 기존 파일 | 향후 위치 후보 | 통합 전에 할 일 |
| --- | --- | --- |
| app.py | src/lumi/player/ | UI 의존성과 실행 진입점 확인 |
| auto_roi.py | src/lumi/processing/ | 탐지·마스크·감광 책임과 입출력 분리 검토 |
| processing.py | src/lumi/video/ | 영상 검사·FFmpeg 경로 처리 확인 |
| test_auto_roi.py, test_player.py | tests/ | 임시 파일·샘플 데이터·실행 환경 확인 |
| assets/ | 별도 assets/ | 사용할 파일과 배포 가능 범위 확인 |

위 경로는 제안이며 아직 모듈을 구현한 상태가 아닙니다.
.venv, cache, outputs, evaluation, backups와 실행 바이너리를 통째로 복사하지 않습니다.
원본은 보존하고 작은 PR 단위로 통합합니다.

## 첫 기능 통합의 확인 항목

짧은 동일 영상으로 입력 정보, 대상 영역 마스크, 부분 감광 결과를 기록합니다.
ROI 밖 변화, 장면 전환, 움직임에 따른 잔상, 실행 실패 처리를 확인합니다.
검증한 영상·구간·환경과 미확인 조건을 experiments/ 기록에 남깁니다.
