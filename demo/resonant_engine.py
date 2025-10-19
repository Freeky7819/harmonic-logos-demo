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

"""Minimal Resonant Engine — didactic prototype (no external deps)
Scout → Hypothesis → Cross-Link → Mirror → Synthesis
"""
from typing import Dict, List, Tuple
KNOWLEDGE = {
    "physics": [
        "Noether's theorem links symmetry to conservation laws.",
        "Least action principle: systems follow extremal action paths.",
        "Orbital balance = gravity vs tangential velocity."
    ],
    "art": [
        "Bach's counterpoint shows structured variation and perceived beauty.",
        "Renaissance architecture often used the golden ratio for harmony.",
        "Haiku reveals depth via minimal structure."
    ],
    "math": [
        "Kolmogorov complexity relates description length to structure.",
        "Fractals: simple rules → rich complexity.",
        "Information theory links compressibility to meaning."
    ],
    "ethics": [
        "Non-Harm: prefer helpful, non-destructive alternatives.",
        "Truth Protocol: detect contradictions; favor verifiable claims.",
        "Reality Anchor: distinguish exploration from operational facts."
    ]
}
def scout(question: str) -> Dict[str, List[str]]:
    q = question.lower()
    hits = {"physics": [], "art": [], "math": [], "ethics": []}
    if any(k in q for k in ["orbit","force","energy","physics","simetrij","symmetr","action"]):
        hits["physics"] = KNOWLEDGE["physics"]
    if any(k in q for k in ["art","glasb","music","painting","aesth","lepota","beauty","architecture"]):
        hits["art"] = KNOWLEDGE["art"]
    if any(k in q for k in ["math","kompleks","frakt","compression","ratio","golden","inform"]):
        hits["math"] = KNOWLEDGE["math"]
    hits["ethics"] = KNOWLEDGE["ethics"]
    if not any(hits.values()):
        for k in hits: hits[k] = [KNOWLEDGE[k][0]]
    return hits
def hypothesis(hits: Dict[str, List[str]]) -> str:
    parts = []
    if hits["physics"]: parts.append("Physics suggests structure via symmetry and least action.")
    if hits["art"]: parts.append("Art suggests perceived beauty via structured variation.")
    if hits["math"]: parts.append("Math suggests meaning relates to compressible rules.")
    if hits["ethics"]: parts.append("Ethics suggests truth and non-harm steer valid conclusions.")
    if not parts:
        parts = ["Even without strong priors, we can seek resonance between order and meaning."]
    return " ".join(parts)
def cross_link(hits: Dict[str, List[str]]) -> List[str]:
    links = []
    if hits["physics"] and hits["math"]:
        links.append("Symmetry (physics) ↔ description length (math): simple laws explain many phenomena.")
    if hits["art"] and hits["math"]:
        links.append("Aesthetic patterns (art) ↔ compressibility (math): elegant structure feels meaningful.")
    if hits["physics"] and hits["art"]:
        links.append("Least action (physics) ↔ compositional economy (art): minimal structure, maximal effect.")
    if not links:
        links.append("General link: coherence arises when multiple domains agree on structure and signal.")
    return links
def _detect_simple_contradictions(text: str) -> List[str]:
    issues = []
    if "2+2=5" in text: issues.append("Contradiction: 2+2=5 (should be 4).")
    if "always" in text.lower() and "never" in text.lower():
        issues.append("Overconfidence: contains both 'always' and 'never'.")
    return issues
def mirror(review_units: List[str]):
    joined = " ".join(review_units)
    issues = _detect_simple_contradictions(joined)
    corrected = []
    for u in review_units:
        c = u.replace("2+2=5", "2+2=4")
        c = c.replace(" always ", " typically ").replace(" never ", " rarely ")
        corrected.append(c)
    return issues, corrected
def synthesis(question, hits, hypo, links, issues, corrected) -> str:
    out = []
    out.append("--- Resonant Engine Output ---")
    out.append(f"Question: {question}")
    out.append("Scout:")
    for k, vals in hits.items():
        if vals: out.append(f"  {k}: " + "; ".join(vals))
    out.append("Hypothesis: " + hypo)
    out.append("Cross-Link:"); [out.append("  - " + L) for L in links]
    if issues:
        out.append("Mirror (issues detected):"); [out.append("  * " + i) for i in issues]
    else:
        out.append("Mirror: no issues detected.")
    out.append("Post-Mirror (corrected/softened):"); [out.append("  • " + c) for c in corrected]
    out.append("Synthesis:")
    out.append("  Coherent answer emerges by aligning physical symmetry, artistic structure, and mathematical compression, under Truth/Non-Harm constraints.")
    out.append("Conclusion: Resonance stable.")
    return "\n".join(out)
def run(question: str) -> str:
    hits = scout(question); hypo = hypothesis(hits); links = cross_link(hits)
    issues, corrected = mirror([hypo] + links)
    return synthesis(question, hits, hypo, links, issues, corrected)
if __name__ == "__main__":
    import sys
    q = " ".join(sys.argv[1:]) or "How does symmetry relate to beauty and meaning?"
    print(run(q))
