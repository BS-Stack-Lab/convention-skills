#!/usr/bin/env python3
"""Generate a team-standard Flyway Versioned Migration file name."""

from __future__ import annotations

import argparse
import re
from datetime import datetime
from zoneinfo import ZoneInfo


DESCRIPTION_PATTERN = re.compile(r"[a-z][a-z0-9]*(?:_[a-z][a-z0-9]*)*")
TIMESTAMP_PATTERN = re.compile(r"\d{14}")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate V<yyyyMMddHHmmss>__<snake_case_description>.sql."
    )
    parser.add_argument("description", help="Lowercase snake_case migration description")
    parser.add_argument(
        "--timestamp",
        help="Optional KST timestamp in yyyyMMddHHmmss for deterministic validation",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    if not DESCRIPTION_PATTERN.fullmatch(args.description):
        raise SystemExit("description must be lowercase snake_case, for example create_users_table")

    timestamp = args.timestamp or datetime.now(ZoneInfo("Asia/Seoul")).strftime("%Y%m%d%H%M%S")
    if not TIMESTAMP_PATTERN.fullmatch(timestamp):
        raise SystemExit("timestamp must use yyyyMMddHHmmss")

    print(f"V{timestamp}__{args.description}.sql")


if __name__ == "__main__":
    main()
