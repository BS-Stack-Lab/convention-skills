# Convention Skills

팀 공용 Codex 스킬 패키지입니다.

- `team-backend-conventions`: 백엔드 세부 컨벤션 스킬 라우터와 원문 보관
- `team-backend-code-style`: EditorConfig·네이밍·Checkstyle·패키지·import 규칙
- `team-backend-api-integration`: REST API·공통 응답·API 문서·환경 변수·비밀 정보
- `team-backend-git-workflow`: 브랜치·커밋·도메인 Scope·Breaking Change 규칙
- `team-backend-quality-gates`: Spotless·Checkstyle·테스트·Gradle·CI/CD·Git Hook
- `team-backend-review-governance`: PR·리뷰·병합·배포·롤백·마스킹 규칙
- `team-flyway-migration-naming`: Flyway Versioned Migration 파일명 생성·검토 규칙
- `team-convention-autoload`: 모든 요청에서 관련 컨벤션 스킬을 자동 선택하는 라우터
- `team-frontend-conventions`: 프론트엔드 세부 컨벤션 스킬 라우터와 원문 보관
- `team-frontend-code-style`: React·TypeScript 코드 스타일
- `team-frontend-api-integration`: API 통신·환경 변수·보안 정보
- `team-frontend-git-workflow`: 브랜치·커밋 규칙
- `team-frontend-quality-gates`: 포맷·린트·테스트·CI/CD·Git Hook
- `team-frontend-review-governance`: PR·리뷰·병합·배포 운영
- `team-development-issue-authoring`: 백엔드·프론트엔드 기능 부모와 하위 테스크 분리 기준
- `team-backend-feature-task-issue-authoring`: `[BE][FEATURE]`·`[BE][TASK]`의 API·도메인·DB·테스트 기준
- `team-frontend-feature-task-issue-authoring`: `[FE][FEATURE]`·`[FE][TASK]`의 화면·상태·연동·테스트 기준
- `team-incident-issue-authoring`: 발생한 버그·장애·사용자 문의 대응 이슈 기준
- `team-work-item-title-conventions`: 이슈·PR·커밋의 명사형 제목 규칙
- `team-pr-authoring`: PR 요청 시 자동 적용되는 일반·고위험 PR 작성 가이드

## 훅 포함 설치

Codex 데스크톱 앱의 플러그인 화면에서 아래 GitHub 저장소를 마켓플레이스로 가져온 뒤
`Convention Skills`를 설치합니다.

- 저장소: `https://github.com/BS-Stack-Lab/convention-skills`
- 경로: 비워 둠
- 브랜치: `main`

설치 중 표시되는 훅 정의를 검토하고 신뢰해야 자동 라우팅이 실행됩니다. 이후 새 task를
열면 모든 사용자 요청에 자동 라우터를 적용합니다. 자동 라우터는 저장소와 실제 작업 범위를
확인해 백엔드·프론트엔드·PR·이슈·Flyway 하위 스킬을 필요한 시점에 선택합니다. 기능 이슈는
영역이 지정되지 않았거나 양쪽 영향이 있으면 `[BE][FEATURE]`와 `[FE][FEATURE]` 초안을
각각 작성하고, 독립 작업으로 분리할 근거가 있는 경우에만 하위 테스크를 제안하도록 안내합니다. 훅은 코드를
수정하거나 명령을 차단하지 않습니다.

## 스킬만 설치

훅 없이 스킬만 사용할 때는 아래 방법을 사용합니다.

```bash
git clone https://github.com/BS-Stack-Lab/convention-skills.git
cd convention-skills
bash install.sh
```

`bash install.sh`은 스킬만 설치하며, 자동 라우팅 훅은 설치하지 않습니다. 상세 설치 방법은 [INSTALL.md](INSTALL.md)를 참고하세요.
