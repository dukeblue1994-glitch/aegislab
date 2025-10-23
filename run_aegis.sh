#!/usr/bin/env bash
set -euo pipefail
bold=$(tput bold 2>/dev/null||true);reset=$(tput sgr0 2>/dev/null||true)
green=$(tput setaf 2 2>/dev/null||true);cyan=$(tput setaf 6 2>/dev/null||true)
yellow=$(tput setaf 3 2>/dev/null||true);red=$(tput setaf 1 2>/dev/null||true);dim=$(tput dim 2>/dev/null||true)
banner(){ cat <<'B'
    ___        _           _         _         _     
   / _ \  ___ | |__   ___ (_)  __ _ | |  __ _ | |__  
  / /_)/ / _ \| '_ \ / _ \| | / _` || | / _` || '_ \ 
 / ___/ |  __/| |_) |  __/| || (_| || || (_| || | | |
 \/      \___||_.__/ \___|/ | \__,_||_| \__,_||_| |_|
                       |__/   (Synthetic • Safe • Local)
B
}
hr(){ printf '%s\n' "${dim}────────────────────────────────────────────────────────────${reset}"; }
ok(){ printf '%s\n' "${green}✔${reset} $*"; }
info(){ printf '%s\n' "${cyan}ℹ${reset} $*"; }
warn(){ printf '%s\n' "${yellow}⚠${reset} $*"; }
err(){ printf '%s\n' "${red}✖${reset} $*"; }
step(){ printf '%s\n' "${bold}$*${reset}"; }

ROOT="$(cd "$(dirname "$0")" && pwd)"
TOOLS="$ROOT/tools"; AEG="$TOOLS/aegisctl.py"; VENV="$ROOT/.venv"; REQS="$TOOLS/requirements.txt"; OUT="$ROOT/report/aegislab-report.md"

clear; banner; hr; info "Repo: $ROOT"; info "Report → $OUT"; hr

PY=$(command -v python3 || command -v python || true); [[ -n "$PY" ]] || { err "Install Python 3.8+"; exit 3; }
ok "Using $($PY --version 2>&1)"

[[ -d "$VENV" ]] || { step "Creating venv…"; $PY -m venv "$VENV"; }
# shellcheck source=/dev/null
source "$VENV/bin/activate"; ok "Venv active ($(python --version 2>&1))"
pip install --upgrade pip >/dev/null; pip install -r "$REQS" >/dev/null || warn "Deps install emitted warnings"
chmod +x "$AEG" 2>/dev/null || true

step "1) Synthesizing logs…";   python "$AEG" synth   | sed "s/^/[synth] /"
step "2) Analyzing logs…";      python "$AEG" analyze | sed "s/^/[analyze] /"
step "3) Building report…";     python "$AEG" report  | sed "s/^/[report] /"

[[ -f "$OUT" ]] && { ok "Report ready: $OUT"; (command -v open && open "$OUT") >/dev/null 2>&1 || true; } || { err "Report missing"; exit 4; }
