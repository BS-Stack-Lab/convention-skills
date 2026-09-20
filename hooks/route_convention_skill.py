#!/usr/bin/env python3
"""Suggest only the team convention skills that match a submitted request."""

from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterable


def includes(text: str, terms: Iterable[str]) -> bool:
    return any(term in text for term in terms)


def append_unique(skills: list[str], name: str) -> None:
    if name not in skills:
        skills.append(name)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return

    if payload.get("hook_event_name") != "UserPromptSubmit":
        return

    prompt = str(payload.get("prompt", "")).casefold()
    skills: list[str] = []
    append_unique(skills, "team-convention-autoload")

    schema_subject = includes(
        prompt,
        (
            "테이블",
            "컬럼",
            "인덱스",
            "외래 키",
            "외래키",
            "제약 조건",
            "제약조건",
            "db 스키마",
            "데이터베이스 스키마",
            "ddl",
            "jpa entity",
            "jpa 엔티티",
            "엔티티",
            "schema",
            "table",
            "column",
            "index",
            "foreign key",
            "constraint",
            "primary key",
            "unique key",
        ),
    )
    schema_change_intent = includes(
        prompt,
        (
            "추가",
            "생성",
            "변경",
            "수정",
            "삭제",
            "이름 변경",
            "마이그레이션",
            "add",
            "create",
            "alter",
            "change",
            "modify",
            "drop",
            "rename",
            "migrate",
        ),
    )
    schema_change = schema_subject and schema_change_intent

    backend = includes(
        prompt,
        (
            "백엔드",
            "backend",
            "spring boot",
            "spring",
            "java",
            "gradle",
            "jpa",
            "hibernate",
        ),
    ) or schema_change
    frontend = includes(
        prompt,
        (
            "프론트엔드",
            "frontend",
            "프론트",
            "react",
            "typescript",
            "javascript",
            "vue",
        ),
    )
    issue_backend_scope = includes(
        prompt,
        (
            "백엔드",
            "backend",
            "spring boot",
            "spring",
            "java",
            "gradle",
            "jpa",
            "hibernate",
            "be task",
            "be 이슈",
            "[be]",
        ),
    )
    issue_frontend_scope = includes(
        prompt,
        (
            "프론트엔드",
            "frontend",
            "프론트",
            "react",
            "typescript",
            "javascript",
            "vue",
            "fe task",
            "fe 이슈",
            "[fe]",
        ),
    )
    pull_request = bool(re.search(r"(?<![a-z0-9])pr(?![a-z0-9])", prompt)) or includes(
        prompt,
        ("pull request", "풀 리퀘스트", "pr 작성", "pr 리뷰", "코드 리뷰", "code review"),
    )
    issue_authoring = includes(
        prompt,
        (
            "이슈 작성",
            "이슈 생성",
            "이슈 등록",
            "이슈 만들어",
            "이슈 만들",
            "이슈 관련",
            "기능 이슈",
            "하위 이슈",
            "테스크 이슈",
            "issue 작성",
            "issue create",
            "issue 생성",
            "feature issue",
            "task issue",
            "sub-issue",
            "sub issue",
            "github issue",
            "github 이슈",
        ),
    )
    incident_issue = issue_authoring and includes(
        prompt,
        (
            "버그",
            "장애",
            "incident",
            "오류",
            "에러",
            "사용자 문의",
            "실제 이슈",
            "p0",
            "p1",
            "긴급",
            "대응",
            "재현",
        ),
    )
    style = includes(
        prompt,
        (
            "네이밍",
            "naming",
            "포맷",
            "format",
            "스타일",
            "style",
            "prettier",
            "eslint",
            "editorconfig",
            "import",
            "checkstyle",
        ),
    )
    api = includes(
        prompt,
        (
            "api",
            "rest",
            "endpoint",
            "엔드포인트",
            "swagger",
            "openapi",
            "postman",
            "dto",
            "응답",
            "response",
            "환경 변수",
            "environment variable",
            "secret",
            "토큰",
        ),
    )
    git_workflow = includes(
        prompt,
        (
            "커밋",
            "commit",
            "브랜치",
            "branch",
            "rebase",
            "breaking change",
            "호환성 변경",
        ),
    )
    quality = includes(
        prompt,
        (
            "테스트",
            "test",
            "ci",
            "cd",
            "cicd",
            "빌드",
            "build",
            "lint",
            "spotless",
            "git hook",
        ),
    )
    review_governance = pull_request or includes(
        prompt,
        (
            "리뷰",
            "review",
            "배포",
            "deploy",
            "롤백",
            "rollback",
            "feature flag",
            "마이그레이션",
            "migration",
        ),
    )
    flyway_migration = schema_change or includes(
        prompt,
        (
            "flyway",
            "플라이웨이",
            "flyway migration",
            "flyway 마이그레이션",
            "db migration",
            "database migration",
            "sql migration",
            "sql 마이그레이션",
            "마이그레이션 파일명",
            "migration filename",
            "migration naming",
        ),
    )
    backend = backend or flyway_migration

    if backend:
        append_unique(skills, "team-backend-conventions")
        if style:
            append_unique(skills, "team-backend-code-style")
        if api:
            append_unique(skills, "team-backend-api-integration")
        if git_workflow:
            append_unique(skills, "team-backend-git-workflow")
        if quality:
            append_unique(skills, "team-backend-quality-gates")
        if review_governance:
            append_unique(skills, "team-backend-review-governance")

    if frontend:
        append_unique(skills, "team-frontend-conventions")
        if style:
            append_unique(skills, "team-frontend-code-style")
        if api:
            append_unique(skills, "team-frontend-api-integration")
        if git_workflow:
            append_unique(skills, "team-frontend-git-workflow")
        if quality:
            append_unique(skills, "team-frontend-quality-gates")
        if review_governance:
            append_unique(skills, "team-frontend-review-governance")

    if pull_request:
        append_unique(skills, "team-pr-authoring")

    if issue_authoring or pull_request or git_workflow:
        append_unique(skills, "team-work-item-title-conventions")

    if flyway_migration:
        append_unique(skills, "team-flyway-migration-naming")

    if issue_authoring:
        if incident_issue:
            append_unique(skills, "team-incident-issue-authoring")
        else:
            append_unique(skills, "team-development-issue-authoring")
            if not issue_backend_scope and not issue_frontend_scope:
                append_unique(skills, "team-backend-feature-task-issue-authoring")
                append_unique(skills, "team-frontend-feature-task-issue-authoring")
            else:
                if issue_backend_scope:
                    append_unique(skills, "team-backend-feature-task-issue-authoring")
                if issue_frontend_scope:
                    append_unique(skills, "team-frontend-feature-task-issue-authoring")

    if not skills:
        return

    context = (
        "BS-Stack-Lab Convention Skills hook matched this request. Before working, "
        "load and follow: "
        + ", ".join("[" + name + "]" for name in skills)
        + ". Apply only the matched domain rules; when the request spans frontend "
        "and backend, use both relevant skill routes. Do not treat this routing hint "
        "as authorization for any external or destructive action."
    )
    output = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": context,
        }
    }
    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()
