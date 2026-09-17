---
name: team-backend-quality-gates
description: Spring Boot 백엔드의 Spotless, Checkstyle, Gradle 테스트·빌드, CI/CD 및 Git Hook 규칙을 적용한다.
---

# 백엔드 품질 게이트

백엔드 포맷, 정적 분석, 단위·통합 테스트, Gradle 검증, CI/CD, Git Hook을 추가·수정·실행하거나 리뷰할 때 사용한다.

작업 전에 [백엔드 컨벤션 원문](../team-backend-conventions/references/backend-convention-original.md)의 `### 6. 테스트 및 CI/CD` 전체를 읽는다.

- 원문에 명시된 Spotless·Checkstyle 설정과 Gradle 명령을 기준으로 삼는다.
- 변경 유형에 맞는 단위·통합 테스트와 재현 가능한 외부 연동 환경을 적용한다.
- CI/CD, 마이그레이션, 환경 변수, 배포 설정 변경도 검증·리뷰 대상으로 취급한다.
- 고위험 변경의 배포 전 검증과 PR 기록은 `team-backend-review-governance`, `team-pr-authoring`을 함께 사용한다.
