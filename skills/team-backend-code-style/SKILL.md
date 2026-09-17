---
name: team-backend-code-style
description: Spring Boot·Java 백엔드의 EditorConfig, 네이밍, Checkstyle, 패키지와 import 규칙을 적용한다.
---

# 백엔드 코드 스타일

Spring Boot·Java 코드, Gradle 모듈 이름, 패키지 구조, 포맷 또는 Checkstyle 설정을 구현하거나 리뷰할 때 사용한다.

작업 전에 [백엔드 컨벤션 원문](../team-backend-conventions/references/backend-convention-original.md)의 `### 1. 코드 스타일 가이드`와 `### 2. CheckStyle 설정` 전체를 읽는다.

- 원문의 EditorConfig 값, 네이밍 표, Checkstyle 표를 그대로 적용한다.
- Controller·Service 등의 기술 계층보다 도메인 중심 패키지 구성을 우선한다.
- 포맷·정적 분석 설정을 바꾸는 작업은 대량 코드 변경과 분리한다. 검증 명령과 CI 적용은 `team-backend-quality-gates`를 함께 사용한다.
