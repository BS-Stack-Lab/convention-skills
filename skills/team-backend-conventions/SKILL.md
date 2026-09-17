---
name: team-backend-conventions
description: Spring Boot와 Java 백엔드 코드를 구현하거나 리뷰할 때 팀의 코드·API·보안·테스트·커밋 규칙을 적용한다.
---

# 백엔드 컨벤션

Spring Boot와 Java 작업, 백엔드 코드 리뷰, 백엔드 관련 문서·PR 작성에 사용한다.

## 코드 구조와 스타일

- UTF-8, LF, 공백 4칸, 마지막 줄 개행, 후행 공백 제거를 사용한다.
- 주석을 포함해 한 줄은 120자 이내로 유지한다. URL과 불가피한 문자열은 예외로 한다.
- 클래스와 Entity는 단수형 `PascalCase`, 메서드·변수는 동사형 `camelCase`, 상수는 `UPPER_SNAKE_CASE`를 사용한다.
- Controller, Service, Repository, Request, Response의 접미사를 일관되게 사용한다. 구현체는 필요한 경우에만 `Impl` 접미사를 사용한다.
- 패키지는 기술 계층보다 `user`, `order`, `payment` 같은 도메인 중심으로 구성한다. 공통 코드는 `global` 아래에 둔다.
- 모든 제어문에 중괄호를 사용한다. 연산자는 이전 줄 끝에 둔다.
- import는 `java`, `javax`, `jakarta`, 외부 라이브러리, 프로젝트 내부 순으로 정렬하고, 그룹 사이를 한 줄 비운다. 와일드카드 import는 사용하지 않는다.
- 주석은 코드의 반복 설명 대신 의도, 배경, 제약을 설명한다.

## API·데이터·보안

- REST 경로는 복수형 `kebab-case`를 사용한다. 예: `/api/v1/order-items`.
- HTTP 메서드의 역할을 준수한다. 조회는 GET, 생성은 POST, 전체 수정은 PUT, 부분 수정은 PATCH, 삭제는 DELETE다.
- 응답의 최상위 구조는 `success`, `data`, `error`를 일관되게 유지한다.
- 상태 코드와 Custom Code를 명확히 사용한다. API 계약 변경 시 OpenAPI·Swagger·Postman 문서를 함께 갱신한다.
- 응답 필드 삭제·필수화·의미 변경은 Breaking Change 여부, 프론트엔드 호환성, 배포 순서를 검토한다.
- `.env.example`에는 변수명, 용도, 필수 여부, 개발용 예시를 기록한다. 실제 비밀키, DB 비밀번호, 토큰, 운영 URL, 개인정보는 저장소·로그·PR 증빙에 넣지 않는다.

## 검증

- Spotless와 Checkstyle이 도입된 프로젝트에서는 관련 검사를 실행한다. 규칙 도입·변경은 대량 코드 수정과 별도 PR·커밋으로 분리한다.
- 주요 비즈니스 로직에는 단위 테스트를 작성한다.
- API 계약, DB, 배치, 외부 연동 변경에는 통합 테스트를 추가하거나 보완한다. 외부 연동은 Mock 서버, Docker, Testcontainers처럼 재현 가능한 환경을 우선한다.
- 인증·권한, 개인정보, 데이터 정합성, DB 마이그레이션, 외부 연동 변경에는 통합 테스트와 배포 전 검증 절차를 PR에 남긴다.
- 버그 수정 시 재발 방지 테스트를 우선 검토한다.

## Git과 PR

- 한 브랜치와 한 커밋은 하나의 작업 목적에 집중한다. 기능 커밋과 마이그레이션·파일 이동·포맷 변경은 분리한다.
- 커밋은 `<type>(<domain>)!: <설명>` 형식을 사용한다. 제목은 50자 이내, 헤더는 72자 이내, 끝 마침표 없이 작성한다.
- API, DB, 외부 연동, 보안·성능 영향은 커밋 본문과 PR에 배경 및 호환성 정보를 남긴다.
- PR을 작성·수정·리뷰할 때는 반드시 `team-pr-authoring` 스킬을 함께 사용한다.
