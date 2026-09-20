---
name: team-backend-conventions
description: Spring Boot·Java 백엔드 작업의 팀 컨벤션을 적용할 때, 세부 규칙 스킬과 원문 기준을 선택한다.
---

# 백엔드 컨벤션 라우터

Spring Boot 또는 Java 백엔드의 구현, 수정, 리뷰, 설정 변경을 시작할 때 사용한다.

원문 기준은 [백엔드 컨벤션 원문](references/backend-convention-original.md)이다. 이 파일은 팀이 제공한 내용을 원문 그대로 보관한 기준 문서이므로, 세부 규칙이 필요할 때 해당 절 전체를 먼저 읽는다.

작업 범위에 따라 아래 스킬을 함께 적용한다.

- Java 코드, 패키지, import, Checkstyle, EditorConfig: `team-backend-code-style`
- REST API, 공통 응답, API 문서, 환경 변수와 비밀 정보: `team-backend-api-integration`
- 브랜치, 커밋, Breaking Change 표기: `team-backend-git-workflow`
- Spotless, Checkstyle, 테스트, Gradle 검증, CI/CD, Git Hook: `team-backend-quality-gates`
- PR, 코드 리뷰, 병합, 배포·롤백, 민감 정보 마스킹: `team-backend-review-governance`
- 영속 테이블·컬럼·인덱스·제약 조건·관계 또는 SQL DDL 변경: `team-flyway-migration-naming`

백엔드 작업 중 사용자가 Flyway를 언급하지 않았더라도, 영속 모델이나 DB 스키마 변경이 필요하다고 판단되면 `team-flyway-migration-naming`을 불러온다. 적용된 Migration은 수정하지 않고 새 Versioned Migration으로 진행한다.

PR 작성·수정·리뷰에는 `team-pr-authoring`도 반드시 적용한다.
