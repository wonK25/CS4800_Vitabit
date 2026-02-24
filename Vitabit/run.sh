#!/usr/bin/env bash
set -euo pipefail

APP_DIR="$HOME/Vitabit"
APP_FILE="vitabit_main.py"
APP_PORT="5050"
PY="$APP_DIR/.venv/bin/python"

cd "$APP_DIR"

# Pull latest code (rebase is risky in automation; use a clean sync)
git fetch --all
git reset --hard origin/main

# Ensure venv exists
if [ ! -d ".venv" ]; then
  python3.12 -m venv .venv
fi

# Install/update deps
"$PY" -m pip install -U pip
"$PY" -m pip install -r requirements.txt

# Load environment variables for runtime
if [ ! -f ".env" ]; then
  echo ".env is missing in $APP_DIR. Add MONGODB_URI before deployment."
  exit 1
fi
set -a
# shellcheck disable=SC1091
source .env
set +a

# Stop previous process (if any) by matching the exact command
# This avoids killing unrelated python processes.
pkill -f "$PY $APP_FILE" || true

# Start new process
nohup "$PY" "$APP_FILE" > log.txt 2>&1 &

echo "Started on port $APP_PORT. Tail logs with: tail -n 200 -f $APP_DIR/log.txt"
