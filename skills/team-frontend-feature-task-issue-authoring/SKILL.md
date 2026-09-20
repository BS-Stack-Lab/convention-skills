---
name: team-frontend-feature-task-issue-authoring
description: 프론트엔드 기능 부모 이슈와 하위 테스크 이슈를 작성·수정·검토할 때 화면·상태·접근성·API 연동·테스트·분리 기준을 적용한다.
---

# 프론트엔드 기능·테스크 이슈 작성

`[FE][FEATURE]` 부모 이슈와 그에 연결되는 `[FE][TASK]` 하위 테스크 이슈를 작성·수정·검토할 때 사용한다. 프론트엔드 기능 부모는 프론트엔드가 제공할 사용자 결과와 범위를 소유하고, 테스크는 그 범위가 독립 구현·리뷰·완료 단위일 때만 만든다.

작성 전에 [프론트엔드 기능·테스크 이슈 가이드](references/frontend-feature-task-issue-guide.md)를 읽는다. 기능 이슈와 하위 이슈의 관계 규칙은 `team-development-issue-authoring`의 [기능·테스크 이슈 구조 가이드](../team-development-issue-authoring/references/feature-task-issue-structure-guide.md)를 따른다.

- 부모 제목은 `[FE][FEATURE]`, 테스크 제목은 `[FE][TASK]`로 시작하며, `team-work-item-title-conventions`의 명사형으로 사용자가 보거나 수행할 결과를 쓴다.
- 테스크를 만들기 전에 가이드의 분리 기준을 판정한다. 부모 본문의 화면·상태·연동·테스트 항목을 그대로 테스크로 복제하지 않는다.
- 화면·사용자 흐름·상태·입력 검증·접근성·반응형·오류 처리·API 연동 중 실제로 바뀌는 것만 범위와 완료 조건에 적는다. 알 수 없는 사항은 `결정 필요`로 남긴다.
- 백엔드 API가 필요하면 계약, 오류 상태, Mock 가능 여부, 선행 백엔드 이슈를 적는다. API 계약을 추정해 고정하지 않는다.
- 정상·로딩·빈 상태·오류·권한 없음 등 해당하는 사용자 상태와 단위·통합·E2E 테스트를 완료 조건에 포함한다.
- 이슈를 GitHub에 실제 생성·수정하거나 담당자·라벨·관계를 바꾸는 일은 사용자가 명시적으로 요청한 경우에만 한다.
