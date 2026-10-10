# Handoff — 후속 작업 안내

## 파일 구조

- manuscript_full.md: 전체 통합 원고 (편집용 정본)
- chapters/01.md ~ chapters/08.md: 장별 원고 (정본)
- pages/: 위키독스 GitHub 연동용 페이지 (00~94 순서, chapters/ 내용과 동일)
- assets/: cover.png, plan-matrix.png, dashboard-spec.png, motion-storyboard.png, SOURCES.md
- references.md: 원문 출처 상세 기록
- qa_report.md: 검증 결과
- README.md, TOC.md: 위키독스 연동용
- tools/build.py: manuscript_full.md와 pages/ 재조립 스크립트
- tools/make_images.py: 이미지 재생성 스크립트
- 2026-10-10_topic2_sources.md, 2026-10-10_topic2_curriculum.md: 근거 파일 (유지)

## 원고 수정 방법

1. chapters/의 해당 장 파일을 고칩니다.
2. tools/build.py를 실행하면 pages/와 manuscript_full.md가 다시 조립됩니다.
3. 이미지를 바꾸려면 tools/make_images.py를 수정 후 실행하세요.

## 최신 정보 갱신 지점

기능과 요금제는 빠르게 바뀝니다. 아래 날짜가 지난 뒤에는 공식 도움말에서 다시 확인하고 본문을 고치세요.

- 2026-10-15: Docs·Slides·Design 자동 활성화 예정일 (2장, 준비물 장의 표)
- 2026-12-14: 독립 Claude Design 사이트 유지 종료일 (5장)
- Dashboards·Motion 베타 범위: 정식 출시되면 2·6·7장의 "베타" 표기와 플랜 표를 고치세요
- 갱신할 파일: chapters/02.md, 06.md, 07.md, pages/03-prep.md, assets/plan-matrix.png

## 위키독스 업로드 담당자에게

- 이 저장소의 README.md, TOC.md, pages/, assets/ 구조로 위키독스 GitHub 연동 책을 만드세요.
- 책 제목: Claude로 문서·슬라이드·대시보드 만들기
- 저장소 이름: claude-artifacts-practice
- 목차 수: 17개
- qa_report.md의 미확인 항목(위키독스 붙여넣기 검수, 사람의 사실·저작권 확인)을 출판 전에 처리하세요.
