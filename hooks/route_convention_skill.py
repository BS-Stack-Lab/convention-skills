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
    )
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
            "issue 작성",
            "issue create",
            "issue 생성",
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

    if issue_authoring:
        append_unique(
            skills,
            "team-incident-issue-authoring"
            if incident_issue
            else "team-development-issue-authoring",
        )

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
