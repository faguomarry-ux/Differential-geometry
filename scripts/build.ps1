param([string]$PythonCommand = 'python')
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Push-Location $projectRoot
try {
    & $PythonCommand scripts/check-sources.py
    if ($LASTEXITCODE -ne 0) { throw 'Source check failed' }
    latexmk -r latexmkrc main.tex
    if ($LASTEXITCODE -ne 0) { throw 'LaTeX build failed' }
    Write-Output 'PDF: build/main.pdf'
} finally { Pop-Location }
