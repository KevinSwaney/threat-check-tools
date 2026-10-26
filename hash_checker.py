#!/usr/bin/env python3
"""Compute SHA-256 and MD5 for a file, optionally compare to an expected SHA-256."""
import sys, hashlib
def hashes(path):
    h256, hmd5 = hashlib.sha256(), hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h256.update(chunk); hmd5.update(chunk)
    return h256.hexdigest(), hmd5.hexdigest()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 hash_checker.py <file> [expected-sha256]"); sys.exit(2)
    s256, md5 = hashes(sys.argv[1])
    print(f"SHA-256: {s256}")
    print(f"MD5: {md5}")
    if len(sys.argv) > 2:
        print("MATCH" if s256.lower() == sys.argv[2].lower() else "NO MATCH")
