---
name: team-flyway-migration-naming
description: Flyway Versioned SQL Migration 파일을 만들거나 이름을 제안·변경·검토할 때 팀의 타임스탬프 및 snake_case 규칙을 적용한다.
---

# Flyway 마이그레이션 파일명

Flyway Versioned Migration의 생성, 이름 변경, 리뷰 또는 파일명 문의에 사용한다. 일반 DB 설계나 Flyway 설정 설명만 요청했고 마이그레이션 파일이 없으면 이름을 임의로 만들지 않는다.

파일을 새로 만들거나 이름을 제안·변경하기 전에는 [Flyway 마이그레이션 파일명 가이드](references/flyway-migration-file-naming-guide.md)를 전체 읽는다.

## 새 파일명 생성

- 사용자가 명령어·타임스탬프·정확한 파일명을 지정하지 않아도, 변경 목적이 명확하면 이 스킬을 적용해 이름을 생성한다.
- 파일명은 반드시 `V<yyyyMMddHHmmss>__<snake_case_description>.sql` 형식으로 작성한다.
- Description은 한 개의 논리적 DB 변경을 나타내는 영문 소문자 `snake_case`로 정한다. `create_users_table`, `add_status_to_orders`처럼 동사와 대상을 사용한다.
- 현재 KST(Asia/Seoul) 시각의 정확한 Version은 `scripts/generate_migration_name.py`로 생성한다. 사용자가 이 명령을 실행하게 하지 말고, 작업 중인 Codex가 실행·적용한다.
- 작업 대상 저장소에 기존 Flyway Migration 파일이 있으면 새 Version이 중복되지 않는지 확인한다. 중복이면 더 늦은 고유 시각으로 다시 생성한다.
- 이미 스테이징·운영 등 영구 환경에 적용된 Versioned Migration은 이름이나 내용을 바꾸지 않는다. 수정은 새 Migration으로 진행한다.

## 출력과 변경 경계

- 사용자가 파일명만 요청하면 생성한 파일명과 선택한 Description만 간결히 제공한다.
- 파일 생성·이름 변경을 요청하면 대상 프로젝트의 Flyway location과 기존 Migration을 먼저 확인한 뒤, 한 개의 논리적 변경에 한 파일을 만든다.
- 대규모 데이터 변경, 삭제·타입 변경, 긴 잠금, MySQL DDL처럼 위험이 있는 변경은 배포 순서와 복구 방법을 별도로 확인한다.
- Flyway 설정만 다루는 요청에서는 파일을 생성하지 않는다. 파일명 검증을 설정할 때만 `validateMigrationNaming` 활성화 여부를 확인한다.
