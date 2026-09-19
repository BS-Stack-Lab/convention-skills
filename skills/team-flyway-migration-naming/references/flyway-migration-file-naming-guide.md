# Flyway 마이그레이션 파일명 가이드

## 파일명 규칙

모든 Versioned SQL Migration은 아래 형식을 사용한다.

```text
V<yyyyMMddHHmmss>__<snake_case_description>.sql
```

| 구성 요소 | 규칙 | 예시 |
| --- | --- | --- |
| Prefix | 대문자 `V` | `V` |
| Version | KST(Asia/Seoul) 기준 14자리 시각 `yyyyMMddHHmmss` | `20260920143015` |
| Separator | 밑줄 두 개 `__` | `__` |
| Description | 변경 의도가 드러나는 영문 소문자 `snake_case` | `create_users_table` |
| Suffix | 소문자 `.sql` | `.sql` |

Flyway Versioned Migration은 버전 순서대로 한 번만 적용된다. Version은 고유해야 하며, 타임스탬프는 병렬 개발 시 충돌을 줄인다.

## 예시

```text
V20260920143015__create_users_table.sql
V20260920143102__add_status_to_orders.sql
V20260920143218__add_index_to_users_email.sql
V20260920143341__backfill_user_nicknames.sql
V20260920143405__drop_legacy_tokens_table.sql
```

Description은 동사와 대상을 사용한다.

| 변경 | 권장 Description |
| --- | --- |
| 테이블 생성 | `create_payments_table` |
| 컬럼 추가 | `add_deleted_at_to_users` |
| 인덱스 추가 | `add_index_to_orders_created_at` |
| 데이터 보정 | `backfill_order_statuses` |
| 제약 조건 추가 | `add_fk_to_order_items_order` |
| 제거 | `drop_legacy_refresh_tokens_table` |

## 허용하지 않는 형식

```text
v20260920143015__create_users_table.sql
V20260920143015_create_users_table.sql
V20260920143015__CreateUsersTable.sql
V20260920143015__create-users-table.sql
V20260920143015__사용자_테이블_생성.sql
V20260920__create_users_table.sql
V1__create_users_table.sql
```

## 작성 및 변경 규칙

1. 프로젝트에 설정된 Flyway location에서 기존 파일과 Version을 확인한다.
2. KST 기준 현재 시각으로 Version을 생성한다.
3. Version이 중복되면 아직 적용되지 않은 새 파일만 더 늦은 고유 시각으로 생성한다.
4. 한 파일에는 하나의 논리적 DB 변경 목적만 둔다.
5. 테이블·컬럼·Description은 팀 DB 규칙에 따라 `snake_case`를 사용한다.
6. 이미 영구 환경에 적용된 Migration은 수정·삭제·이름 변경하지 않는다. 필요한 보정은 새 Versioned Migration으로 추가한다.
7. MySQL DDL은 자동 롤백되지 않을 수 있으므로 작고 복구 가능한 변경으로 나누고, 위험한 변경은 배포·복구 방법을 PR에 남긴다.
8. SQL 파일에는 비밀번호, 토큰, 개인정보, 운영 데이터를 직접 넣지 않는다.

## 검토 항목

- [ ] `V<yyyyMMddHHmmss>__<snake_case_description>.sql` 형식인가?
- [ ] 대문자 `V`, 14자리 KST Version, 정확히 두 개의 밑줄을 사용했는가?
- [ ] Version이 기존 파일과 중복되지 않는가?
- [ ] Description이 영문 소문자 `snake_case`이며 변경 목적을 설명하는가?
- [ ] 적용된 Migration을 수정하지 않았는가?
- [ ] 위험 변경의 검증·배포·복구 방법을 남겼는가?

## 근거

- [Flyway Versioned Migrations](https://documentation.red-gate.com/fd/versioned-migrations-273973333.html)
- [Flyway SQL Migration Separator](https://documentation.red-gate.com/flyway/reference/configuration/flyway-namespace/flyway-sql-migration-separator-setting)
