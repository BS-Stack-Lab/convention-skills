# 팀 Codex 스킬 설치

이 폴더를 각자의 맥으로 받은 뒤 아래 명령을 실행합니다.

```bash
bash install.sh
```

스크립트는 세 스킬을 `~/.codex/skills`에 설치합니다.

- `team-backend-conventions`
- `team-frontend-conventions`
- `team-frontend-code-style`
- `team-frontend-api-integration`
- `team-frontend-git-workflow`
- `team-frontend-quality-gates`
- `team-frontend-review-governance`
- `team-pr-authoring`

설치 후 Codex를 재시작하거나 새 task를 엽니다. `team-pr-authoring`은 자동 호출을 허용하도록 설정되어 있어, 첫 요청에 PR, Pull Request, PR 설명, PR 템플릿, PR 리뷰가 포함되면 Codex가 먼저 적용합니다. 필요할 때는 `$team-backend-conventions`, `$team-frontend-conventions`, `$team-pr-authoring`으로 명시 호출할 수 있습니다.

스킬을 업데이트할 때는 이 패키지의 최신 버전을 받은 뒤 같은 명령을 다시 실행합니다.
