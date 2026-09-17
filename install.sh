#!/usr/bin/env bash

set -euo pipefail

package_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
codex_root="${CODEX_HOME:-${HOME}/.codex}"
target_root="${codex_root}/skills"

skills=(
  team-backend-conventions
  team-frontend-conventions
  team-frontend-code-style
  team-frontend-api-integration
  team-frontend-git-workflow
  team-frontend-quality-gates
  team-frontend-review-governance
  team-pr-authoring
)

for skill in "${skills[@]}"; do
  source_dir="${package_dir}/skills/${skill}"
  target_dir="${target_root}/${skill}"

  if [[ ! -f "${source_dir}/SKILL.md" ]]; then
    echo "Missing SKILL.md: ${source_dir}" >&2
    exit 1
  fi

  mkdir -p "${target_dir}"
  cp -R "${source_dir}/." "${target_dir}/"
  echo "Installed: ${target_dir}"
done

echo
echo "Restart Codex or open a new task to refresh the available skills."
