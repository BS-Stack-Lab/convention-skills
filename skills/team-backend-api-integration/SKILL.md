---
name: team-backend-api-integration
description: Spring Boot 백엔드의 REST API, 공통 응답, 오류, API 문서, 환경 변수와 비밀 정보 규칙을 적용한다.
---

# 백엔드 API·데이터·보안 규칙

REST API, DTO·응답, API 계약, OpenAPI·Swagger, 설정 값, 외부 연동 또는 비밀 정보를 다룰 때 사용한다.

작업 전에 [백엔드 컨벤션 원문](../team-backend-conventions/references/backend-convention-original.md)의 `### 3. API 및 데이터 규칙` 및 `### 8. 추가 규칙` 중 API·응답·보안 관련 항목 전체를 읽는다.

- REST 경로, HTTP 메서드, 성공·실패 공통 응답과 오류 처리의 원문 규칙을 따른다.
- API 계약을 변경하면 문서를 갱신하고 하위 호환성, 프론트엔드 영향, 배포 순서를 검토한다.
- 실제 비밀값·운영 정보·개인정보를 저장소, 로그, PR 증빙에 남기지 않는다.
- API·DB 변경의 테스트·배포 계획은 `team-backend-quality-gates`, `team-backend-review-governance`, `team-pr-authoring`을 함께 적용한다.
