## 컨벤션 룰

### 1. 코드 스타일 가이드

> Spring Boot + Java 기준으로 작성합니다.
> 
1. EditorConfig 설정

| 설정 항목 | 값 | 설명 |
| --- | --- | --- |
| charset | utf-8 | 모든 소스 파일은 UTF-8 인코딩을 사용합니다. |
| end_of_line | lf | 운영체제와 관계없이 줄바꿈은 LF로 통일합니다. |
| indent_style | space | 탭 대신 공백을 사용합니다. |
| indent_size | 4 | Java 코드 들여쓰기는 공백 4칸을 사용합니다. |
| insert_final_newline | true | 모든 파일 마지막에는 개행을 추가합니다. |
| trim_trailing_whitespace | true | 줄 끝의 불필요한 공백을 제거합니다. |
| max_line_length | 120 | 한 줄 최대 길이는 120자입니다. |

#### 네이밍 규칙

| 대상 | 규칙 | 예시 |
| --- | --- | --- |
| 프로젝트/모듈명 | `kebab-case` | `meomuneum-backend` |
| Gradle Group | 역도메인 형식 | `com.muse` |
| Artifact | `kebab-case` | `meomuneum-api` |
| Java 클래스 | 명사형 `PascalCase` | `MemberController` |
| 구현 클래스 | `Impl` 접미사 | `MemberServiceImpl` |
| Controller | `Controller` 접미사 | `MemberController` |
| Service | `Service` 접미사 | `MemberService` |
| Repository | `Repository` 접미사 | `MemberRepository` |
| DTO | `Request`, `Response` 접미사 | `MemberCreateRequest` |
| Entity | 단수형 명사 `PascalCase` | `Member`, `OrderItem` |
| 메서드/변수 | `camelCase` | `findUserById`, `createdAt` |
| 상수 | `UPPER_SNAKE_CASE` | `MAX_PAGE_SIZE` |
| 설정 속성 | `kebab-case` | `spring.datasource.url` |
| DB 테이블/컬럼 | `snake_case` | `order_items`, `created_at` |
| REST API 경로 | 복수형 명사 `kebab-case` | `/api/v1/order-items` |

### 2. CheckStyle 설정

| 항목 | 규칙 |
| --- | --- |
| 클래스명 | 명사 또는 명사구의 `PascalCase`를 사용합니다. 예: `UserService`, `OrderController` |
| 변수명 및 메서드명 | `camelCase`를 사용합니다. 메서드는 동사로 시작합니다. 예: `findUserById`, `createOrder` |
| 상수명 | `UPPER_SNAKE_CASE`를 사용합니다. 예: `MAX_LOGIN_ATTEMPTS` |
| 패키지명 | 모두 소문자를 사용하며 도메인 단위로 구성합니다. 예: `com.muse.meomuneum.user` |
| 탭 사용 | 탭 문자를 사용하지 않고 공백 4칸을 사용합니다. |
| 줄 바꿈 | 120자를 초과하면 의미 있는 단위로 줄을 나눕니다. |
| 최대 라인 길이 | 주석을 포함하여 120자를 초과하지 않습니다. URL·불가피한 문자열은 예외로 합니다. |
| 제어문 블록 `{}` | `if`, `for`, `while` 등 모든 제어문에 중괄호를 사용합니다. |
| 연산자 배치 | 연산자는 줄의 시작이 아닌 이전 줄 끝에 배치합니다. |
| import 순서 | Java 표준 → 외부 라이브러리 → 프로젝트 내부 순서로 작성합니다. 각 그룹은 한 줄로 구분하며 와일드카드 import는 사용하지 않습니다. |
| 주석 스타일 | 코드 동작을 반복 설명하지 않고, 의도·배경·제약사항을 설명합니다. 오래된 주석은 수정 또는 제거합니다. |

패키지는 Controller, Service 등 기술 계층보다 `user`, `order`, `payment` 등의 도메인 중심으로 구성합니다.

```
com.muse.meomuneum
├── user
│   ├── UserController.java
│   ├── UserService.java
│   ├── UserRepository.java
│   ├── User.java
│   ├── UserCreateRequest.java
│   └── UserResponse.java
├── order
└── global
    ├── config
    ├── exception
    └── response
```

### 3. API 및 데이터 규칙

#### REST API

- 자원은 복수형 명사와 kebab-case 경로를 사용한다.
    - `/api/v1/users`
    - `/api/v1/order-items`
- HTTP 메서드의 역할을 준수한다.
    - 조회: `GET`
    - 생성: `POST`
    - 전체 수정: `PUT`
    - 부분 수정: `PATCH`
    - 삭제: `DELETE`

#### 표준 응답 형식

성공·실패 응답의 최상위 구조를 일관되게 유지한다.

```
{
  "success": true,
  "data": {},
  "error": null
}
```

#### 오류와 문서화

- HTTP 상태 코드(`200`, `400`, `401`, `404`, `500`)를 명확히 사용한다.
- 상세 오류는 Custom Code와 메시지로 제공한다.
- API 변경 시 Swagger, OpenAPI 또는 Postman 문서를 함께 갱신한다.
- 응답 필드 삭제·필수화·의미 변경은 Breaking Change 여부를 검토하고, 프론트엔드와 배포 순서를 합의한다.

### 환경 변수와 비밀 정보

- `.env.example`에는 변수명, 용도, 필수 여부, 개발용 예시값을 기록한다. 예시값에는 실제 운영 정보나 비밀값을 넣지 않는다.
- 실제 비밀키, DB 비밀번호, 토큰, 운영 URL은 저장소에 올리지 않는다.
- 로그에도 인증 정보와 개인정보가 남지 않도록 한다.

### 4. Git 및 버전 관리

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

### 5. 커밋 메시지 컨벤션

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
| feat | 새로운 API 또는 비즈니스 기능 추가 |
| fix | 버그 수정 |
| docs | README, API 명세, 문서 수정 |
| refactor | 기능 변경 없이 코드 구조 개선 |
| chore | 코드 동작과 무관한 설정 및 기타 작업 |
| content | 정적 데이터, 메시지 등 콘텐츠 수정 |
| style | 공백, 포맷팅 등 코드 스타일 수정 |
| test | 단위 테스트·통합 테스트 추가 또는 수정 |
| build | Gradle, 의존성, 빌드 설정 변경 |
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
feat(payment): 결제 승인 재시도 정책 추가

일시적인 결제사 5xx 응답과 타임아웃에 한해 최대 3회 재시도한다.
멱등 키를 검증해 재시도 과정의 중복 승인을 방지한다.

기존 결제 API 응답 형식은 유지한다.
참조: #456
```

```
docs(api): 오류 응답 규격 문서화

참조: #12
```

```
feat(api)!: 주문 생성 요청 필드 변경

호환성 변경: `orderName` 필드를 `name`으로 변경한다.
```

### 6. 테스트 및 CI/CD

#### 포맷팅 및 정적 분석

- Java/Spring Boot 프로젝트는 `Spotless`를 포맷터로, `Checkstyle`을 코드 스타일 검사기로 사용한다.
- 아래 Gradle 태스크는 두 플러그인을 `build.gradle`에 적용한 뒤 사용한다. 아직 적용하지 않은 프로젝트에서는 도입 PR을 먼저 만든다.
- 잠재 버그·복잡도·취약점 분석이 필요한 프로젝트는 `PMD`, `Error Prone`, `SonarQube`를 추가할 수 있다. 도입한 도구의 검사는 CI 필수 단계에 연결한다.
- 포맷터 또는 정적 분석 규칙 변경은 코드 대량 변경과 분리하여 별도 PR·커밋으로 관리한다.

**Spotless**

| 항목 | 설정 | 설명 |
| --- | --- | --- |
| Formatter | Eclipse JDT Formatter | `config/eclipse-java-formatter.xml`을 단일 기준으로 사용합니다. IDE도 같은 설정 파일을 적용합니다. |
| 들여쓰기 | 공백 4칸 | `.editorconfig` 및 Formatter 설정과 동일하게 적용합니다. |
| 최대 줄 길이 | `120` | 가독성을 위해 한 줄 최대 길이를 120자로 제한합니다. 긴 문자열·URL·주석은 예외로 둘 수 있습니다. |
| import 순서 | `java` → `javax` → `jakarta` → `org` → `com` | import를 정렬하고 그룹 사이에는 빈 줄 하나를 둡니다. |
| 미사용 import | 자동 제거 | `removeUnusedImports()`로 사용하지 않는 import를 제거합니다. |
| 검사 대상 | `src/main/java`, `src/test/java` | 운영 코드와 테스트 코드를 같은 포맷 규칙으로 정리합니다. |
| 제외 대상 | `build`, 생성 코드 | 빌드 산출물과 자동 생성 코드는 포맷·검사에서 제외합니다. |
| 줄 끝·파일 끝 | 공백 제거, 마지막 줄바꿈 | `trimTrailingWhitespace()`, `endWithNewline()`을 적용합니다. |

**Checkstyle**

| 항목 | 설정 | 설명 |
| --- | --- | --- |
| 기준 파일 | `config/checkstyle/checkstyle.xml` | 팀의 규칙 파일을 저장소에서 버전 관리합니다. |
| 네이밍 | Java 표준 네이밍 | 패키지는 소문자, 클래스·인터페이스는 PascalCase, 메서드·변수는 camelCase를 사용합니다. |
| import 규칙 | 와일드카드 import 금지 | `*` import, 중복 import, 정렬되지 않은 import는 오류로 처리합니다. |
| 줄 길이 | `120`자 | Formatter와 같은 줄 길이 기준을 사용합니다. |
| 공백·중괄호 | 필수 공백과 중괄호 사용 | 제어문·연산자 주변 공백, 중괄호 누락 등 가독성을 해치는 형식을 오류로 처리합니다. |
| 금지 코드 | `System.out`, `System.err`, `printStackTrace()` 금지 | 로그는 프로젝트의 표준 Logger를 사용하고, 예외는 예외 처리 정책에 따라 전달하거나 처리합니다. |
| 테스트 코드 | 운영 코드와 동일한 기본 규칙 | 테스트 가독성을 위해 `MagicNumber`, Javadoc 등은 필요한 경우 일부 완화할 수 있습니다. |

```bash
cd backend
./gradlew spotlessCheck --no-daemon
./gradlew checkstyleMain checkstyleTest --no-daemon
```

#### 테스트 규칙

- 주요 비즈니스 로직의 단위 테스트를 작성한다.
- API 계약, DB 접근, 배치, 외부 연동 변경 시 통합 테스트를 작성하거나 기존 테스트를 보완한다.
- 외부 시스템 연동은 Mock 서버, Docker, Testcontainers 등 재현 가능한 테스트 환경을 우선 사용한다.
- 인증·권한, 음악 기록 저장·수정·삭제, AI 추천·챗봇, 채팅·소셜, 공유·외부 연동, 개인정보, DB 마이그레이션, 데이터 정합성, 배치 변경은 통합 테스트와 배포 전 검증 절차를 반드시 PR에 남긴다.
- 버그 수정 시 재발 방지를 위한 테스트 추가를 우선 검토한다.

#### 로컬 검증

```bash
cd backend
./gradlew spotlessCheck checkstyleMain checkstyleTest --no-daemon
./gradlew test --no-daemon
./gradlew bootJar --no-daemon
```

`spotlessCheck`와 `checkstyleMain`·`checkstyleTest`는 포맷·코드 규칙을 검증한다. `./gradlew test`는 프로젝트에 연결된 단위·통합 테스트를 실행한다. 별도 `integrationTest` 태스크를 사용하는 프로젝트는 해당 태스크도 실행한다. `./gradlew bootJar`는 배포 가능한 JAR 패키징 가능 여부를 검증하며, 테스트를 대체하지 않는다.

#### CI/CD 규칙

- 모든 PR에서 `Spotless`, `Checkstyle`, `./gradlew test --no-daemon`, `./gradlew bootJar --no-daemon`을 실행하고 모두 성공해야 병합할 수 있다.
- CI의 깨끗한 실행 환경이 필요할 때만 다음처럼 `clean`을 포함한다. 로컬 `pre-push`에서 매번 `clean`을 실행해 캐시를 지우지는 않는다.

```bash
cd backend
./gradlew clean spotlessCheck checkstyleMain checkstyleTest test --no-daemon
./gradlew bootJar --no-daemon
```

- 일반 PR은 빠른 단위 테스트와 패키징 검증을 우선 수행한다. `main` 병합, 운영 배포, 또는 위험 변경은 단위 테스트와 통합 테스트를 모두 통과해야 한다.
- CI/CD 설정, 배포 스크립트, 마이그레이션, 환경 변수 정의 변경도 일반 코드와 동일하게 PR 리뷰와 검증 대상에 포함한다.
- 배포는 검증된 JAR 또는 컨테이너 산출물로 수행한다. DB 마이그레이션·외부 연동·운영 설정 변경은 배포 순서, 상태 확인, 롤백 방법을 PR에 기록한다.

#### Git Hooks

- `pre-commit`: `./gradlew spotlessApply`로 포맷을 정리하고 `./gradlew checkstyleMain --no-daemon`으로 기본 코드 규칙을 검사한다.
- `pre-push`: `./gradlew spotlessCheck checkstyleMain checkstyleTest test --no-daemon`으로 정적 분석과 빠른 기본 테스트를 수행한다. 전체 통합 테스트와 깨끗한 빌드 검증은 CI에서 수행한다.

### 7. PR 및 코드 리뷰

#### 기본 PR 작성 가이드

#### 복잡하거나 위험한 변경에 대한 PR 작성 가이드

### 8. 추가 규칙

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
