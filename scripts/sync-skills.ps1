param(
    [string]$CodexHome = $(if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }),
    [string[]]$SkillName = @()
)

$ErrorActionPreference = 'Stop'
$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $repoRoot 'skills'
$destinationRoot = Join-Path $CodexHome 'skills'

if (-not (Test-Path -LiteralPath $sourceRoot)) {
    throw "Skill source directory does not exist: $sourceRoot"
}

New-Item -ItemType Directory -Path $destinationRoot -Force | Out-Null
$copied = @()

foreach ($skill in Get-ChildItem -LiteralPath $sourceRoot -Directory) {
    if ($SkillName.Count -gt 0 -and $skill.Name -notin $SkillName) { continue }
    $destination = Join-Path $destinationRoot $skill.Name
    New-Item -ItemType Directory -Path $destination -Force | Out-Null
    foreach ($entry in Get-ChildItem -LiteralPath $skill.FullName -Force) {
        Copy-Item -LiteralPath $entry.FullName -Destination $destination -Recurse -Force
    }
    $copied += $skill.Name
}

Write-Output "Synced $($copied.Count) skills to $destinationRoot"
$copied | ForEach-Object { Write-Output "- $_" }
