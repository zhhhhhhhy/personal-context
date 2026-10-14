param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }),
    [string]$RepoRoot = (Split-Path -Parent $PSScriptRoot),
    [switch]$Force
)

$ErrorActionPreference = 'Stop'
$target = Join-Path $CodexHome 'AGENTS.md'
if ((Test-Path -LiteralPath $target) -and -not $Force) {
    throw "Global Codex AGENTS.md already exists: $target. Inspect it and rerun with -Force only if the merge is intentional."
}

New-Item -ItemType Directory -Path $CodexHome -Force | Out-Null
if (Test-Path -LiteralPath $target) {
    $backup = "$target.bak-$(Get-Date -Format yyyyMMdd-HHmmss)"
    Copy-Item -LiteralPath $target -Destination $backup -Force
    Write-Output "Backed up existing global router to $backup"
}

$content = @"
# Personal Context global router

For every Codex session, read these four core Context files once before handling the user request:
- $RepoRoot\rules\SOUL.md
- $RepoRoot\profile.md
- $RepoRoot\habits\communication.md
- $RepoRoot\INDEX.md

Use $RepoRoot as the source of truth. Load detailed Context and Skills only by INDEX.md routing. Do not load all conversation history. When the user requests Context evolution, follow $RepoRoot\docs\evolution\POLICY.md and $RepoRoot\skills\personal-context\SKILL.md; raw conversation evidence stays local and automatic writes are limited to the learned-rule path with validation and rollback.
"@
Set-Content -LiteralPath $target -Value $content -Encoding utf8
Write-Output "Installed personal Context router at $target"
