## 컨벤션 룰

### 1. 코드 컨벤션 (Prettier & ESLint)

**네이밍 규칙**

| 항목 | 케이스 규칙 |
| --- | --- |
| 폴더명, 일반 파일명, 변수 및 함수명, 서버 응답 데이터 | `camelCase` |
| React 컴포넌트명 및 컴포넌트 파일명 | `PascalCase` |
| React Hook | `use` + `PascalCase` |
| Interface / Type | `PascalCase` |
| Props 타입 | 컴포넌트명 + `Props` |
| Boolean 변수 | `is`, `has`, `should` 접두사 |
| 상수 | `UPPER_SNAKE_CASE` |
| 환경 변수 | `VITE_` + `UPPER_SNAKE_CASE` |

예시:

```
components/
├── common/
│   └── Button.tsx
features/
└── orderHistory/
    ├── OrderList.tsx
    ├── orderApi.ts
    ├── orderTypes.ts
    └── useOrderList.ts
```

```
interface UserProfileProps {
  userId: number;
  onClick: () => void;
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

const isLoading = true;
const getUserData = async () => {};
```

**Prettier**

| 옵션 | 값 | 설명 |
| --- | --- | --- |
| trailingComma | `all` | 마지막 요소 뒤에 쉼표를 추가합니다. |
| tabWidth | `2` | 들여쓰기는 공백 2칸을 사용합니다. |
| semi | `true` | 문장 끝에 세미콜론을 사용합니다. |
| singleQuote | `true` | 문자열에 작은따옴표를 사용합니다. |
| bracketSpacing | `true` | 객체 중괄호 내부에 공백을 둡니다. |
| jsxBracketSameLine | `false` | JSX 닫는 꺾쇠괄호를 다음 줄에 배치합니다. |
| printWidth | `100` | 한 줄 최대 길이는 100자로 제한합니다. |

> 최신 Prettier에서는 `jsxBracketSameLine` 대신 `bracketSameLine` 옵션을 사용합니다.
> 

**ESLint**

| 항목 | 설정 내용 |
| --- | --- |
| 기본 설정 | ESLint 권장 규칙과 React 권장 규칙을 적용합니다. |
| TypeScript 설정 | `typescript-eslint` 권장 규칙을 적용합니다. |
| 글로벌 환경 | Browser, ES2021 환경을 사용합니다. |
| 무시 폴더 | `node_modules`, `dist`, `coverage`는 검사에서 제외합니다. |
| 플러그인 | `react`, `react-hooks`, `react-refresh`, `@typescript-eslint`를 사용합니다. |
| 커스텀 룰 | 미사용 변수·import는 오류로 처리하고, `console.log`는 경고로 처리합니다. |
| Hooks 규칙 | Hook은 컴포넌트 최상위에서만 호출하며, 의존성 배열을 준수합니다. |
| Props 검증 | TypeScript 타입을 사용하므로 `react/prop-types` 규칙은 비활성화합니다. |

### 2. 깃 브랜치 전략

#### 브랜치 전략

| 기본 브랜치 | 설명 |
| --- | --- |
| main | 운영 배포용 |
| dev | 개발 통합용 |

| 작업 브랜치 | 설명 |
| --- | --- |
| feature/기능명 | 단일 기능 개발 (예: feature/order-create) |
| fix/버그명 | 버그 수정 |
- 하나의 브랜치는 하나의 이슈 또는 작업 목적만 담당합니다.
- 작업 브랜치는 최신 `dev` 브랜치를 기준으로 생성합니다.
- 작업 완료 후 PR을 통해 `dev` 브랜치에 병합합니다.

### 3. API 및 데이터 통신 규칙

#### REST API 사용

- 자원은 복수형 명사 경로를 사용한다. 예: `/api/v1/users`, `/api/v1/music-records`
- HTTP 메서드의 역할을 준수한다.
    - 조회: `GET`
    - 생성: `POST`
    - 전체 수정: `PUT`
    - 부분 수정: `PATCH`
    - 삭제: `DELETE`

#### 응답과 오류 처리

백엔드의 표준 응답 형식을 기준으로 API 타입을 정의한다.

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

- HTTP 상태 코드와 백엔드의 Custom Code를 함께 처리한다.
- 화면에 노출할 메시지는 사용자 행동을 안내할 수 있게 변환한다.
- API 계약 변경이 있으면 프론트 화면 변경과 별도 커밋으로 관리하고 PR에 영향 범위를 기록한다.

#### 환경 변수

- `.env.example`에는 변수명, 용도, 필수 여부, 개발용 예시값을 기록한다. 예시값에는 실제 운영 정보나 비밀값을 넣지 않는다.
- 실제 API Key, 토큰, 인증 정보, 내부 URL은 Git·PR 본문·스크린샷에 포함하지 않는다. 필요한 비밀값은 CI/CD Secret 또는 배포 환경에서 주입한다.
- Vite에서 브라우저에 노출해도 되는 값만 `VITE_` 접두사를 사용한다. `VITE_` 변수는 번들에 포함될 수 있으므로 비밀값을 두지 않는다.
- 환경 변수의 추가·삭제·의미 변경 시 `.env.example`과 실행 문서를 같은 PR에서 갱신한다.

### 4. 커밋 메시지

#### 커밋 메시지 형식

```
<type>[도메인][!]: <설명>

<본문 (선택 사항)>

<꼬리말 (#이슈번호)>
```

**커밋 메시지는** 
`<type>[도메인][!]: <설명>
<본문 (선택 사항)>
<꼬리말 (#이슈번호)>` 
**형식을 따르며, 아래의 규칙을 따릅니다.**

#### **커밋 메시지 규칙**

- 제목은 영어 `lower-case` 또는 자연스러운 한국어 문장형으로 작성합니다.
- 제목 끝에 마침표(`.`)를 사용하지 않습니다.
- 이슈 번호는 꼬리말에 `참조: #123` 형식으로 작성한다.
- 도메인은 선택 사항이며, 도메인 영역을 괄호 안에 작성한다.
- 호환성이 깨지는 변경은 유형 또는 범위 뒤에 `!`를 붙이거나, `호환성 변경:` 꼬리말로 작성한다.
- 본문과 꼬리말은 제목 다음 빈 줄로 구분한다.
- 제목은 최소 5자 이상 최대 50자 이내로 작성합니다.
- 전체 헤더는 72자를 초과하지 않습니다.
- 본문에는 변경 이유와 필요한 배경을 작성한다.
- API 계약, DB, 외부 연동, 보안·성능 영향이 있으면 본문에 배경과 호환성 정보를 남긴다.
- 마이그레이션, 파일 이동, 포맷 변경은 기능 커밋과 분리한다.
- 하나의 커밋에는 하나의 목적만 포함합니다.

| 타입 | 설명 |
| --- | --- |
| feat | 화면, 컴포넌트, 사용자 기능 추가 |
| fix | 버그 수정 (UI, 상태 관리, 사용자 흐름 오류 수정) |
| docs | README, API 명세, 문서 수정 |
| refactor | 기능 변경 없이 코드 구조 개선 |
| chore | 코드 동작과 무관한 설정 및 기타 작업 |
| content | 정적 데이터, 메시지 등 콘텐츠 수정 |
| style | CSS, 포맷, 디자인 수정 |
| test | 단위 테스트·통합 테스트 추가 또는 수정 |
| build | Vite, npm, 의존성 설정 변경 |
| perf | DB 조회, 캐시, 배치, 서버 처리 성능 개선 |
| deploy | CI/CD, 서버 환경, 배포 설정 변경 |

#### **도메인**

| 도메인 | Scope |
| --- | --- |
| 사용자·인증 | `user`, `auth` |
| 지도·위치 | `map`, `location` |
| 음악 기록 | `music-record` |
| AI 음악 추천·챗봇 | `ai-recommendation`, `chatbot` |
| 채팅·소셜 | `chat`, `social` |
| 공유·외부 연동 | `share`, `integration` |

예시:

```
fix(music-record): 동일한 음악 기록 중복 저장 방지

음악 저장 응답 전 버튼이 다시 활성화되어 같은 기록이 중복 요청될 수
있던 문제를 수정한다.

참조: #123
```

```
feat(auth): 소셜 로그인 기능 추가
```

```
docs(frontend): 로컬 실행 환경 설정 문서화

참조: #12
```

### 5. 테스트 및 CI/CD

#### 포맷팅 및 정적 분석

- React + TypeScript 프로젝트는 `Prettier`를 포맷터로, `ESLint`를 정적 분석기로 사용한다.
- 아래 npm 스크립트와 설정은 `package.json`, `eslint.config.*`, `.prettierrc`에서 버전 관리한다. 아직 도입하지 않은 프로젝트에서는 도입 PR을 먼저 만든다.
- 포맷터 또는 린트 규칙 변경은 코드 대량 변경과 분리하여 별도 PR·커밋으로 관리한다.

**Prettier**

| 옵션 | 값 | 설명 |
| --- | --- | --- |
| `trailingComma` | `all` | 마지막 요소 뒤에 쉼표를 추가합니다. |
| `tabWidth` | `2` | 들여쓰기는 공백 2칸을 사용합니다. |
| `semi` | `true` | 문장 끝에 세미콜론을 사용합니다. |
| `singleQuote` | `true` | 문자열에 작은따옴표를 사용합니다. |
| `bracketSpacing` | `true` | 객체 중괄호 내부에 공백을 둡니다. |
| `bracketSameLine` | `false` | JSX 닫는 꺾쇠괄호를 다음 줄에 배치합니다. |
| `printWidth` | `100` | 한 줄 최대 길이는 100자로 제한합니다. |

> 최신 Prettier에서는 `jsxBracketSameLine` 대신 `bracketSameLine` 옵션을 사용합니다.
> 

**ESLint**

| 항목 | 설정 | 설명 |
| --- | --- | --- |
| 기본 설정 | ESLint·React 권장 규칙 | `eslint:recommended`, React 권장 규칙을 적용합니다. |
| TypeScript 설정 | `typescript-eslint` 권장 규칙 | TypeScript 문법과 타입 관련 규칙을 적용합니다. |
| 글로벌 환경 | Browser, ES2021 | 브라우저와 ES2021 환경의 전역 객체를 사용합니다. |
| 무시 폴더 | `node_modules`, `dist`, `coverage` | 의존성, 빌드 산출물, 테스트 결과는 검사에서 제외합니다. |
| 플러그인 | `react`, `react-hooks`, `react-refresh`, `@typescript-eslint` | React 컴포넌트·Hook·Fast Refresh·TypeScript 규칙을 적용합니다. |
| 미사용 항목 | 오류 | 미사용 변수와 import는 `@typescript-eslint/no-unused-vars`로 오류 처리합니다. |
| Console | 경고 | `console.log`는 경고로 처리합니다. 운영 로그가 필요한 경우 표준 로깅 도구를 사용합니다. |
| Hooks 규칙 | 오류 | Hook은 컴포넌트 최상위에서만 호출하며, 의존성 배열을 준수합니다. |
| Props 검증 | 비활성화 | TypeScript 타입을 사용하므로 `react/prop-types` 규칙은 비활성화합니다. |

**권장 npm 스크립트**

```json
{
  "scripts": {
    "format": "prettier --write .",
    "format:check": "prettier --check .",
    "lint": "eslint .",
    "lint:fix": "eslint . --fix",
    "lint:staged": "lint-staged",
    "test": "vitest run",
    "test:watch": "vitest",
    "test:coverage": "vitest run --coverage",
    "test:e2e": "playwright test",
    "build": "tsc -b && vite build"
  }
}
```

`format`은 코드를 자동으로 정리하고, `format:check`는 포맷 위반만 검사한다. `lint`는 경고와 오류를 표시하고, `test`는 단위·컴포넌트 테스트, `test:e2e`는 사용자 흐름 테스트를 실행한다.

`pre-commit`에서 스테이징된 파일만 처리하려면 다음 `lint-staged` 설정을 사용한다.

```json
{
  "lint-staged": {
    "*.{js,jsx,ts,tsx}": ["prettier --write", "eslint --fix"],
    "*.{json,css,scss,md}": "prettier --write"
  }
}
```

**테스트 도구**

| 테스트 유형 | 도구·명령 | 적용 대상 |
| --- | --- | --- |
| 단위·컴포넌트 | Vitest, React Testing Library / `npm run test` | 상태 전환, 입력 검증, 오류 처리, UI 컴포넌트 |
| 커버리지 | Vitest Coverage / `npm run test:coverage` | 테스트 누락 영역 확인. 커버리지 수치만을 목표로 테스트를 작성하지 않습니다. |
| E2E | Playwright / `npm run test:e2e` | 인증, 음악 기록, AI 추천·챗봇, 채팅·소셜, 공유·외부 연동의 주요 사용자 흐름 |

#### 테스트 규칙

- 주요 사용자 흐름, 상태 전환, 입력 검증, 오류 처리에는 단위 또는 컴포넌트 테스트를 작성한다.
- 인증·권한, 음악 기록 생성·수정·삭제, AI 추천·챗봇, 채팅·소셜, 공유·외부 연동, 개인정보, 공통 API 클라이언트 변경에는 E2E 또는 통합 테스트를 추가한다. 전체 E2E를 모든 PR에 강제하지 않고, 변경 위험과 사용자 영향에 따라 대상 시나리오를 선택한다.
- 브라우저·기기 호환성이 중요한 화면은 지원 범위에서 수동 또는 자동화 테스트를 수행한다.
- 버그 수정 시 재현 테스트 또는 회귀 방지 테스트 추가를 우선 검토한다. 자동화하기 어려운 경우에는 PR에 수동 테스트 환경·절차·결과를 남긴다.

### 로컬 검증

```bash
cd frontend
npm run format:check
npm run lint
npm run test
npm run build
```

`npm run format:check`는 포맷 규칙을, `npm run lint`는 코드 규칙·정적 오류를, `npm run test`는 단위·컴포넌트 테스트를, `npm run build`는 프로덕션 번들 생성 가능 여부를 검증한다. `npm run build`만으로 사용자 흐름이 검증되지는 않는다.

### CI/CD 규칙

- 모든 PR에서 `npm ci`로 의존성을 고정 버전으로 설치한 뒤 `npm run format:check`, `npm run lint`, `npm run test`, `npm run build`를 실행한다. 네 검증이 모두 성공해야 병합할 수 있다.
- 포맷 검사·린트·테스트는 가능한 한 병렬로 실행해 빠른 피드백을 제공하되, 빌드 산출물 생성과 배포는 필수 검증 성공 후에만 수행한다.
- E2E·실기기·통합 테스트는 위험 변경 PR, `main` 병합 전, 또는 배포 후보에서 수행한다. 실패 시 원인과 재실행 결과를 PR 또는 CI 결과에 남긴다.
- CI/CD 설정, 환경 변수 정의, 배포 스크립트 변경도 일반 코드와 동일하게 PR 리뷰와 검증 대상에 포함한다.
- 배포는 검증된 빌드 산출물로 수행하며, UI·사용자 흐름 변경은 배포 전후 확인 방법과 롤백 또는 Feature Flag 여부를 PR에 기록한다.

### Git Hooks

- `pre-commit`: `npm run lint:staged`로 Prettier 포맷팅과 ESLint 수정을 스테이징된 파일에만 적용한다.
- `pre-push`: `npm run format:check`, `npm run lint`, `npm run test`로 포맷·정적 분석·빠른 기본 테스트를 수행한다. 전체 E2E·실기기 테스트는 CI에서 수행한다.

### 6. PR 및 코드 리뷰

#### 기본 PR 작성 가이드

#### 복잡하거나 위험한 변경에 대한 PR 작성 가이드

### 7. 추가 규칙

- `main`, `develop` 브랜치에는 직접 push하지 않고 PR을 통해 병합합니다.
- 최소 1명 이상의 코드 리뷰 및 Approve 후 병합합니다.
- API 변경 시 Swagger/OpenAPI 문서를 함께 갱신합니다.
- API 응답 필드는 `camelCase`, DB 테이블 및 컬럼은 `snake_case`를 사용합니다.
- 성공·실패 응답은 프로젝트의 공통 응답 형식을 따릅니다.
- 주요 비즈니스 로직은 단위 테스트를 작성하고, API 변경 시 통합 테스트를 보완합니다.
- API·DB 변경은 프론트엔드 영향과 하위 호환성을 함께 검토한다.
- 배포 전 확인 지표, Feature Flag, 롤백 방법이 있으면 PR에 남긴다.
- PR 병합 전 아래 명령어를 실행하여 테스트와 빌드 성공을 확인합니다.

```
./gradlew clean test --no-daemon
./gradlew bootJar --no-daemon
```

- DB 비밀번호, JWT Secret, 외부 API Key 등 민감 정보는 환경 변수로 관리하며 Git에 커밋하지 않습니다.
- `.env.example` 또는 설정 예시 파일에 필요한 환경 변수 목록만 공유합니다.
- 개인정보, 토큰, 운영 설정값은 PR 본문·로그·스크린샷에서 마스킹한다.

이 컨벤션을 준수하여 팀의 코드 품질을 유지하고 원활한 협업을 진행한다.
