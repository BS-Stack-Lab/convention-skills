---
name: team-frontend-conventions
description: React와 TypeScript 프론트엔드 코드를 구현하거나 리뷰할 때 팀의 코드·API 통신·보안·테스트·커밋 규칙을 적용한다.
---

# 프론트엔드 컨벤션

React와 TypeScript 작업, 프론트엔드 코드 리뷰, 프론트엔드 관련 문서·PR 작성에 사용한다.

## 코드 스타일과 네이밍

- Prettier는 공백 2칸, 세미콜론, 작은따옴표, trailing comma, `printWidth: 100`, `bracketSameLine: false`를 사용한다.
- 폴더, 일반 파일, 변수, 함수, 서버 응답 데이터는 `camelCase`를 사용한다.
- React 컴포넌트와 컴포넌트 파일, Interface와 Type은 `PascalCase`를 사용한다.
- Hook은 `use` 접두사와 `PascalCase`를 사용한다. Props 타입은 `<컴포넌트명>Props`로 작성한다.
- Boolean 값은 `is`, `has`, `should`로 시작한다. 상수는 `UPPER_SNAKE_CASE`를 사용한다.
- ESLint, React, React Hooks, TypeScript 규칙을 따른다. 미사용 변수·import는 오류로 처리하고, `console.log`는 경고로 처리한다.
- Hook은 컴포넌트 최상위에서 호출하고 의존성 배열 규칙을 준수한다.

## API 통신과 환경 변수

- REST 자원은 복수형 경로를 사용하고 HTTP 메서드 역할을 준수한다.
- 백엔드의 `success`, `data`, `error` 응답 구조를 기준으로 API 타입을 정의한다.
- HTTP 상태 코드와 Custom Code를 함께 처리하고, 사용자에게는 행동을 안내하는 메시지로 변환한다.
- API 계약 변경 시 화면 영향 범위를 PR에 기록하고, 프론트 변경과 계약 변경은 별도 커밋으로 관리한다.
- 환경 변수는 `VITE_`와 `UPPER_SNAKE_CASE`를 사용한다. `VITE_` 값은 브라우저 번들에 포함될 수 있으므로 비밀값을 넣지 않는다.
- 환경 변수의 추가·삭제·의미 변경 시 `.env.example`과 실행 문서를 같은 PR에서 갱신한다.
- 실제 API Key, 토큰, 인증 정보, 내부 URL은 Git, PR 본문, 스크린샷에 포함하지 않는다.

## 검증

- 포맷, lint, 단위·컴포넌트 테스트, E2E, 빌드 중 변경에 필요한 가장 좁은 검증부터 실행한다.
- 포맷터·린트 규칙 변경은 대량 코드 수정과 별도 PR·커밋으로 분리한다.
- 사용자 흐름, API 계약, 인증·권한, 환경 변수 변경은 테스트 또는 재현 가능한 수동 검증 결과를 PR에 남긴다.
- 실행하지 못한 검사는 미실행 사유와 대체 검증 방법을 사실대로 기록한다.

## Git과 PR

- 한 브랜치와 한 커밋은 하나의 작업 목적에 집중한다.
- 커밋은 `<type>(<domain>)!: <설명>` 형식을 사용한다. 제목은 50자 이내, 헤더는 72자 이내, 끝 마침표 없이 작성한다.
- UI, 사용자 흐름, API 계약, 보안·성능 영향은 PR에 영향 범위와 검증 근거를 남긴다.
- PR을 작성·수정·리뷰할 때는 반드시 `team-pr-authoring` 스킬을 함께 사용한다.
