#!/usr/bin/env bash
set -u
shopt -s nullglob

PASS=0
FAIL=0
TOTAL=0

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
RISCV_SIM="${RISCV_SIM:-$HOME/RiscSim/driver.py}"
PA_ROOT="${PA_ROOT:-$SCRIPT_DIR}"

strip_sim_noise() {
  grep -v '^Using default machine configuration' \
    | grep -v '^Initializing machine with' \
    | grep -v '^Execution time:'
}

if [[ ! -f "$RISCV_SIM" ]]; then
  echo "ERROR: RiscSim driver not found: $RISCV_SIM" >&2
  echo "Set RISCV_SIM to driver.py or install RiscSim in ~/RiscSim" >&2
  exit 2
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found on PATH." >&2
  exit 2
fi

run_suite () {
  local name="$1"
  local asm="$2"
  local suite_dir="$PA_ROOT/tests/${name}"
  local inputs=( "${suite_dir}"/test*.in )
  if (( ${#inputs[@]} == 0 )); then
    echo "No tests in ${suite_dir}"
    return
  fi
  local f
  for f in "${inputs[@]}"; do
    local base
    base="$(basename "$f" .in)"
    local outf="${suite_dir}/${base}.out"
    ((TOTAL++))
    if [[ ! -f "$outf" ]]; then
      echo "[FAIL] ${name}/${base}: missing ${outf}"
      ((FAIL++))
      continue
    fi
    local actual expected
    actual="$(python3 "$RISCV_SIM" "$asm" < "$f" 2>&1 | tr -d '\r' | strip_sim_noise)"
    expected="$(tr -d '\r' < "$outf")"
    if [[ "$actual" == "$expected" ]]; then
      echo "[PASS] ${name}/${base}"
      ((PASS++))
    else
      echo "[FAIL] ${name}/${base}"
      echo "  --- actual ---"
      printf '%s\n' "$actual"
      echo "  --- expected (${outf}) ---"
      printf '%s\n' "$expected"
      ((FAIL++))
    fi
  done
}

run_suite program1 "$PA_ROOT/program1.asm"
run_suite program2 "$PA_ROOT/program2.asm"

echo
echo "Summary: ${PASS} passed, ${FAIL} failed, ${TOTAL} total"
(( FAIL == 0 ))
