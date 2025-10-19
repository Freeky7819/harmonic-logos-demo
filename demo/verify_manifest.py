import argparse, hashlib, json, os, sys
DEMO_FILES = [
    "demo/mirror_test.py",
    "demo/crosslink_demo.py",
    "demo/verify_manifest.py",
    "demo/ethics_prompt.txt",
    "demo/resonant_engine.py",
    "demo/run_resonant.py",
]
def sha256_concat(paths):
    h = hashlib.sha256()
    for rel in paths:
        with open(rel, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
    return "SHA256-" + h.hexdigest()
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--update", action="store_true")
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(base)
    man_path = os.path.join("demo","manifest.json")
    if args.update:
        new_hash = sha256_concat(DEMO_FILES)
        try:
            with open(man_path, "r", encoding="utf-8") as f:
                man = json.load(f)
        except Exception:
            man = {"project":"Harmonic Logos Demo","version":"v1.2","timestamp":"","resonance_hash":"","signature":"RSA-v1-PUBLIC-PLACEHOLDER"}
        man["resonance_hash"] = new_hash
        if not man.get("timestamp"):
            import datetime
            man["timestamp"] = datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"
        with open(man_path, "w", encoding="utf-8") as f:
            json.dump(man, f, indent=2)
        print(f"Updated manifest with {new_hash}")
        sys.exit(0)
    if args.check:
        with open(man_path, "r", encoding="utf-8") as f:
            man = json.load(f)
        expected = man.get("resonance_hash","")
        actual = sha256_concat(DEMO_FILES)
        if expected == actual:
            print("OK: resonance hash matches.")
            sys.exit(0)
        else:
            print("FAIL: resonance hash mismatch.")
            print(" expected:", expected)
            print(" actual:  ", actual)
            sys.exit(1)
    print("Nothing to do. Use --update or --check.")
