#!/usr/bin/env bash
# Due to the MacOS environment, we'll need to use a virtual environment
# to ensure the correct python and packages are used.
# You can run this script to set up the environment and launch the app.
# Afterwards, you can run main_gui.py directly or continue using this file.

set -euo pipefail

VENV_DIR=".venv"
REQ_PACKAGES=(PyQt6 numpy Pillow scipy pygltflib)

command_exists() { command -v "$1" >/dev/null 2>&1; }

get_python_cmd() {
	if command_exists python3; then
		echo python3
	elif command_exists python; then
		echo python
	else
		return 1
	fi
}

PY_CMD=$(get_python_cmd || true)
if [[ -z "$PY_CMD" ]]; then
	echo "No python executable found (python3 or python). Please install Python 3 and retry." >&2
	exit 1
fi

# Show which python command was chosen and its full path
SYS_PY_PATH="$(command -v "$PY_CMD" 2>/dev/null || true)"
SYS_PY_EXEC="$($PY_CMD -c 'import sys; print(sys.executable)' 2>/dev/null || echo "$SYS_PY_PATH")"
echo "Using python command: $PY_CMD"
echo "System python executable: ${SYS_PY_EXEC}"

# If script was invoked with 'sh' the shebang may not be honored; advise using bash
if [[ -z "${BASH_VERSION:-}" ]]; then
	echo "Warning: this script is intended to run under bash (./installDepend.sh or bash installDepend.sh)."
fi

if [[ ! -d "$VENV_DIR" ]]; then
	echo "Creating virtualenv in ${VENV_DIR} using ${PY_CMD}"
	"$PY_CMD" -m venv "$VENV_DIR"
else
	echo "Virtualenv already exists at ${VENV_DIR}, reusing it."
fi

# Activate venv for this script
# shellcheck disable=SC1090
source "${VENV_DIR}/bin/activate"

echo "Virtualenv activated: VIRTUAL_ENV=${VIRTUAL_ENV:-}" 
echo "Virtualenv python executable: $(python -c 'import sys; print(sys.executable)')"
echo "Upgrading pip and installing packages: ${REQ_PACKAGES[*]}"
python -m pip install --upgrade pip
python -m pip install --upgrade "${REQ_PACKAGES[@]}"

echo "Done. To manually activate the environment later: source ${VENV_DIR}/bin/activate"
if [[ "${1:-}" != "--no-run" ]]; then
	echo "Running the application with the virtualenv python..."
	python main_gui.py
else
	echo "Skipping running the application (called with --no-run)."
fi