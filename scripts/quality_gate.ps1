$ErrorActionPreference = "Stop"

uv sync
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

uv run pytest -m "not integration" -v
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

uv run ruff check .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

uv run black --check .
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

uv run pyright
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

uv run python -c "import mayday"
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

uv build
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

Write-Host ""
Write-Host "========================================="
Write-Host "✅ Quality Gate Passed Successfully!"
Write-Host "========================================="