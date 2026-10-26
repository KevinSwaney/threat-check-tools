#!/usr/bin/env python3
"""Offline URL structure checker. Heuristics only, not a safety verdict."""
import sys, ipaddress
from urllib.parse import urlparse
def check(url):
    p = urlparse(url)
    print(f"Scheme: {p.scheme or '(none)'}")
    print(f"Host: {p.hostname or '(none)'}")
    try:
        ipaddress.ip_address(p.hostname or "")
        print("Note: host is an IP address, not a domain name. Treat with extra care.")
    except ValueError:
        pass
    if p.username:
        print("Note: URL contains a username part before @. The real host is after the last @.")
    if p.scheme == "http":
        print("Note: plain http, not encrypted. Do not enter credentials.")
    elif p.scheme == "https":
        print("Scheme is https, which encrypts the connection but does not prove the site is trustworthy.")
    else:
        print("Note: unusual or missing scheme.")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 url_checker.py <url>"); sys.exit(2)
    check(sys.argv[1])
