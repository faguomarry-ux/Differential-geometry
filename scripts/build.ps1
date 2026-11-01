param([string]$PythonCommand = 'python', [switch]$WithFigureGallery)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
Push-Location $projectRoot
try {
    & $PythonCommand scripts/check-sources.py
    if ($LASTEXITCODE -ne 0) { throw 'Source check failed' }
    if ($WithFigureGallery) {
        & $PythonCommand scripts/build-figures.py
        if ($LASTEXITCODE -ne 0) { throw 'Figure gallery build failed' }
    }
    latexmk -r latexmkrc main.tex
    if ($LASTEXITCODE -ne 0) { throw 'LaTeX build failed' }
    Write-Output 'PDF: build/main.pdf'
} finally { Pop-Location }
