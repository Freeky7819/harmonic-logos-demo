# Harmonic Logos — Resonant Demo

**Version:** v1.2 (RSA-locked)  
**Author & Lead Researcher:** Freedom (Damjan Žakelj)

This repository contains a minimal, verifiable demonstration of the
_Harmonic Logos_ meta-framework — an AI reasoning architecture based
on resonance rather than command.

It does **not** include the internal YAML cores.
All ethics and structural safeguards (Truth Protocol, Reality Anchor,
Non-Harm Directive) are conceptually protected via RSA-v1 (see docs).

## White Papers (placeholders in /docs — replace with your PDFs)
- [Cycle of Resonance Report v1](docs/Cycle_of_Resonance_Report_v1.pdf)
- [Resonance Safety Architecture v1](docs/Resonance_Safety_Architecture_v1.pdf)

## Live Proof
Provide your public, read-only link:
- **Gemini Test Conversation – Harmony Between Order and Meaning:** https://gemini.google.com/share/REPLACE_WITH_YOUR_LINK

---

## Demos

### 1) Mirror Test (self-reflection)
```bash
python demo/mirror_test.py
```

### 2) Cross-Link Demo (transdisciplinary coherence)
```bash
python demo/crosslink_demo.py
```

### 3) Resonant Engine (mini pipeline)
```bash
python demo/run_resonant.py "How does symmetry relate to beauty and meaning?"
```

### 4) Manifest verification
```bash
python demo/verify_manifest.py --check
python demo/verify_manifest.py --update   # if you edit the demo files
```

## Security & Integrity

This demo enforces **runtime integrity**:
- Every script verifies the presence and contents of `demo/manifest.json`.
- A SHA-256 hash of all demo files is recomputed at startup; mismatch causes a safe exit.
- GitHub Actions (`.github/workflows/verify.yml`) re-checks the manifest on every push.

**Why this matters:** if someone copies a single `.py` without the manifest or modifies code,
the script will abort. This preserves the black-box nature of the demo while remaining transparent.

> _“Show resonance, not the core.”_
