# ------- runtime integrity guard (Harmonic Logos Demo) -------
import json as _json, hashlib as _hashlib, os as _os, sys as _sys
def _hl_abort(msg):
    print("INTEGRITY CHECK FAILED:", msg)
    _sys.exit(1)
def _hl_sha256_concat(files):
    h = _hashlib.sha256()
    for rel in files:
        if not _os.path.exists(rel):
            _hl_abort(f"Missing demo file: {rel}")
        with open(rel, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
    return "SHA256-" + h.hexdigest()
_man_path = _os.path.join(_os.path.dirname(__file__), "manifest.json")
if not _os.path.exists(_man_path):
    _hl_abort("manifest.json missing (integrity enforcement).")
with open(_man_path, "r", encoding="utf-8") as _mf:
    _man = _json.load(_mf)
_expected = _man.get("resonance_hash", "")
if not _expected:
    _hl_abort("manifest.json missing 'resonance_hash'.")
_demo_files = ["mirror_test.py","crosslink_demo.py","verify_manifest.py","ethics_prompt.txt","resonant_engine.py","run_resonant.py"]
_demo_files = [_os.path.join(_os.path.dirname(__file__), f) for f in _demo_files]
_actual = _hl_sha256_concat(_demo_files)
if _actual != _expected:
    _hl_abort(f"hash mismatch. expected {_expected} but got {_actual}")
# ------- end integrity guard -------

from resonant_engine import run
import sys
if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "How can harmony emerge from structure?"
    print(run(q))
