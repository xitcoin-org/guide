#!/usr/bin/env python3
"""Validate the canonical public Xitcoin Guide."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
SUMMARY = ROOT / "SUMMARY.md"
errors: list[str] = []

if not SUMMARY.is_file():
    errors.append("SUMMARY.md is missing")
    pages: list[Path] = []
else:
    summary_text = SUMMARY.read_text(encoding="utf-8")
    links = re.findall(r"\]\(([^)]+\.md)\)", summary_text)
    pages = [ROOT / link for link in dict.fromkeys(links)]
    for page in pages:
        if not page.is_file():
            errors.append(f"missing SUMMARY page: {page.relative_to(ROOT)}")

required = {
    "README.md": [
        "Cosmos chain ID | `xitcoin-testnet-1`",
        "EVM chain ID | `101089`",
        "Base denomination | `axtc`",
        "Decimals | 18",
        "Canonical staging active; public cutover pending",
        "Mainnet has not launched",
    ],
    "start/network-status.md": [
        "Public name | Xitcoin Testnet",
        "Initial validators | Atlas, Borealis, Meridian and Zenith",
        "Validator capacity | 258",
        "Minimum self-delegation | 5,000,000 XTC",
        "7d13d7ed6a19ea48e2ce3c408f1f457e0961e72df6dd480d8200a6db5bae8414",
    ],
    "governance/overview.md": [
        "193 reserved Member-State positions",
        "65 general validator positions",
    ],
    "resources/brand-assets.md": [
        "Current Cronos display symbol | XTC",
    ],
    "bridge/status-and-security.md": [
        "The canonical Xitcoin bridge is not currently presented as active",
    ],
}

for relative, statements in required.items():
    path = ROOT / relative
    if not path.is_file():
        errors.append(f"required file missing: {relative}")
        continue
    text = path.read_text(encoding="utf-8")
    for statement in statements:
        if statement not in text:
            errors.append(f"{relative}: required statement missing: {statement}")

prohibited = {
    r"xitcoin-testnet(?!-1)": "obsolete Cosmos chain ID",
    r"\b195 sovereign reference positions\b": "obsolete 195-position policy",
    r"\b63 public positions\b": "obsolete 63-position policy",
    r"\b1,000,000 XTC\b": "obsolete validator minimum",
    r"\breset candidate\b": "obsolete reset-candidate status",
    r"\brelease candidate\b": "obsolete release-candidate status",
    r"Current Cronos display symbol\s*\|\s*\$XTC": "obsolete current symbol",
    r"Public display symbol\s*\|\s*XTC\s*\|\s*\$XTC": "obsolete current symbol table",
}

for page in pages:
    if not page.is_file():
        continue
    text = page.read_text(encoding="utf-8")
    for pattern, label in prohibited.items():
        if re.search(pattern, text, flags=re.IGNORECASE):
            errors.append(f"{page.relative_to(ROOT)}: {label}")

if errors:
    for error in errors:
        print(f"ERROR: {error}")
    raise SystemExit(1)

print(f"summary_pages={len(pages)}")
print("canonical_identity=OK")
print("validator_policy=OK")
print("current_symbol=OK")
print("bridge_boundary=OK")
print("validation=OK")
