---
name: team-backend-review-governance
description: 백엔드 PR, 코드 리뷰, 병합, 배포·롤백, API·DB 영향과 민감 정보 마스킹 규칙을 적용한다.
---

# 백엔드 PR·리뷰·배포 운영

백엔드 PR, 코드 리뷰, 병합 조건, 배포 또는 롤백 계획을 작성하거나 검토할 때 사용한다.

작업 전에 [백엔드 컨벤션 원문](../team-backend-conventions/references/backend-convention-original.md)의 `### 7. PR 및 코드 리뷰`와 `### 8. 추가 규칙` 전체를 읽는다.

- 기본 PR과 복잡하거나 위험한 변경의 상세 작성 형식은 반드시 `team-pr-authoring`의 원문 가이드와 템플릿을 사용한다.
- 직접 push 금지, 최소 승인 수, API 문서, 테스트·빌드, 하위 호환성, Feature Flag·롤백 기록 등 원문의 병합·배포 규칙을 따른다.
- PR 본문·로그·스크린샷에서 개인정보, 토큰, 운영 설정값을 마스킹한다.
