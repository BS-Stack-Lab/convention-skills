# 팀 Codex 스킬 설치

## 권장: 훅 포함 플러그인 설치

각자의 맥에서 Codex 데스크톱 앱을 열고 플러그인 화면에서 마켓플레이스를 가져옵니다.

- 저장소: `https://github.com/BS-Stack-Lab/convention-skills`
- 경로: 비워 둠
- 브랜치: `main`

그다음 `Convention Skills`를 설치하고, 표시되는 훅 정의를 검토해 신뢰합니다. 새 task를
열면 `UserPromptSubmit` 훅이 백엔드·프론트엔드·PR 관련 요청을 판별해 필요한 스킬을
Codex에 안내합니다. 이 훅은 안내 전용이며 파일을 변경하거나 도구 실행을 허용·차단하지
않습니다.

## 스킬만 설치

이 폴더를 각자의 맥으로 받은 뒤 아래 명령을 실행합니다.

```bash
bash install.sh
```

스크립트는 아래 스킬을 `~/.codex/skills`에 설치합니다. 이 방식에는 훅이 포함되지
않습니다.

- `team-backend-conventions`
- `team-backend-code-style`
- `team-backend-api-integration`
- `team-backend-git-workflow`
- `team-backend-quality-gates`
- `team-backend-review-governance`
- `team-frontend-conventions`
- `team-frontend-code-style`
- `team-frontend-api-integration`
- `team-frontend-git-workflow`
- `team-frontend-quality-gates`
- `team-frontend-review-governance`
- `team-pr-authoring`

설치 후 Codex를 재시작하거나 새 task를 엽니다. `team-pr-authoring`은 자동 호출을 허용하도록 설정되어 있어, 첫 요청에 PR, Pull Request, PR 설명, PR 템플릿, PR 리뷰가 포함되면 Codex가 먼저 적용합니다. 필요할 때는 `$team-backend-conventions`, `$team-frontend-conventions`, `$team-pr-authoring`으로 명시 호출할 수 있습니다.

스킬을 업데이트할 때는 이 패키지의 최신 버전을 받은 뒤 같은 명령을 다시 실행합니다.
