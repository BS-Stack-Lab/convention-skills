# Convention Skills

팀 공용 Codex 스킬 패키지입니다.

- `team-backend-conventions`: 백엔드 세부 컨벤션 스킬 라우터와 원문 보관
- `team-backend-code-style`: EditorConfig·네이밍·Checkstyle·패키지·import 규칙
- `team-backend-api-integration`: REST API·공통 응답·API 문서·환경 변수·비밀 정보
- `team-backend-git-workflow`: 브랜치·커밋·도메인 Scope·Breaking Change 규칙
- `team-backend-quality-gates`: Spotless·Checkstyle·테스트·Gradle·CI/CD·Git Hook
- `team-backend-review-governance`: PR·리뷰·병합·배포·롤백·마스킹 규칙
- `team-frontend-conventions`: 프론트엔드 세부 컨벤션 스킬 라우터와 원문 보관
- `team-frontend-code-style`: React·TypeScript 코드 스타일
- `team-frontend-api-integration`: API 통신·환경 변수·보안 정보
- `team-frontend-git-workflow`: 브랜치·커밋 규칙
- `team-frontend-quality-gates`: 포맷·린트·테스트·CI/CD·Git Hook
- `team-frontend-review-governance`: PR·리뷰·병합·배포 운영
- `team-pr-authoring`: PR 요청 시 자동 적용되는 일반·고위험 PR 작성 가이드

## 훅 포함 설치

Codex 데스크톱 앱의 플러그인 화면에서 아래 GitHub 저장소를 마켓플레이스로 가져온 뒤
`Convention Skills`를 설치합니다.

- 저장소: `https://github.com/BS-Stack-Lab/convention-skills`
- 경로: 비워 둠
- 브랜치: `main`

설치 중 표시되는 훅 정의를 검토하고 신뢰해야 자동 라우팅이 실행됩니다. 이후 새 task를
열면 사용자 요청이 제출될 때 백엔드·프론트엔드·PR 관련 키워드를 판별해 필요한 스킬만
Codex 컨텍스트에 안내합니다. 훅은 코드를 수정하거나 명령을 차단하지 않습니다.

## 스킬만 설치

훅 없이 스킬만 사용할 때는 아래 방법을 사용합니다.

```bash
git clone https://github.com/BS-Stack-Lab/convention-skills.git
cd convention-skills
bash install.sh
```

`bash install.sh`은 스킬만 설치하며, 자동 라우팅 훅은 설치하지 않습니다. 상세 설치 방법은 [INSTALL.md](INSTALL.md)를 참고하세요.
