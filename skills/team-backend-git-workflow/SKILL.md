---
name: team-backend-git-workflow
description: 백엔드 작업의 브랜치 전략, 커밋 메시지 형식, 도메인 Scope와 호환성 변경 표기를 적용한다.
---

# 백엔드 Git·커밋 규칙

백엔드 브랜치 생성, 커밋 작성, 이력 정리 또는 Breaking Change 기록에 사용한다.

작업 전에 [백엔드 컨벤션 원문](../team-backend-conventions/references/backend-convention-original.md)의 `### 4. Git 및 버전 관리`와 `### 5. 커밋 메시지 컨벤션` 전체를 읽는다.

- 원문의 기본·작업 브랜치와 한 브랜치/한 목적 원칙을 따른다.
- 커밋 메시지 형식, 타입, 도메인 Scope, 본문·꼬리말, 길이 제한을 원문대로 적용한다.
- 커밋 제목은 `team-work-item-title-conventions`의 명사형 제목 규칙을 우선 적용한다.
- API 계약, DB, 외부 연동, 보안·성능 또는 호환성 변경은 원문의 Breaking Change 표기와 분리 원칙을 따른다.
