---
name: team-backend-feature-task-issue-authoring
description: 백엔드 기능 부모 이슈와 하위 테스크 이슈를 작성·수정·검토할 때 API·도메인·DB·보안·테스트·분리 기준을 적용한다.
---

# 백엔드 기능·테스크 이슈 작성

`[BE][FEATURE]` 부모 이슈와 그에 연결되는 `[BE][TASK]` 하위 테스크 이슈를 작성·수정·검토할 때 사용한다. 백엔드 기능 부모는 백엔드가 제공할 사용자·시스템 결과와 범위를 소유하고, 테스크는 그 범위가 독립 구현·리뷰·완료 단위일 때만 만든다.

작성 전에 [백엔드 기능·테스크 이슈 가이드](references/backend-feature-task-issue-guide.md)를 읽는다. 기능 이슈와 하위 이슈의 관계 규칙은 `team-development-issue-authoring`의 [기능·테스크 이슈 구조 가이드](../team-development-issue-authoring/references/feature-task-issue-structure-guide.md)를 따른다.

- 부모 제목은 `[BE][FEATURE]`, 테스크 제목은 `[BE][TASK]`로 시작하며, `team-work-item-title-conventions`의 명사형으로 전달할 시스템 결과를 쓴다.
- 테스크를 만들기 전에 가이드의 분리 기준을 판정한다. 부모 본문의 API·도메인·DB·테스트 항목을 그대로 테스크로 복제하지 않는다.
- API 계약, 도메인 규칙, 영속 데이터, 권한·보안, 외부 연동 중 실제로 바뀌는 것만 범위와 완료 조건에 적는다. 알 수 없는 사항은 추정하지 않고 `결정 필요`로 남긴다.
- 테이블·컬럼·인덱스·제약 조건·관계 또는 DDL 변경이 있으면 `team-flyway-migration-naming`을 추가로 적용하고, 새 Versioned Migration이 필요한지를 명시한다.
- 프론트엔드가 연동할 API가 바뀌면 요청·응답 호환성, 오류 코드, 문서 갱신 필요 여부와 선후 관계를 적는다.
- 단위·통합 테스트와 실패 경로를 완료 조건에 포함한다. 실행하지 않은 검증 결과를 완료된 것처럼 쓰지 않는다.
- 이슈를 GitHub에 실제 생성·수정하거나 담당자·라벨·관계를 바꾸는 일은 사용자가 명시적으로 요청한 경우에만 한다.
