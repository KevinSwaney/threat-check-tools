# Threat Check Tools

Small offline command line tools to go with the Threat Check page: check a URL's structure, and check a file's hash.

These tools give heuristics and facts, not verdicts. A clean result does not mean a URL or file is safe. Check with your security team before opening anything suspicious.

## url_checker.py

Usage: `python3 url_checker.py https://example.com/path`

It reports: scheme (http vs https), host, whether the host looks like an IP address, and whether the URL contains common lookalike tricks such as a username part before the @ sign. It does not fetch the URL, and it sends nothing anywhere.

## hash_checker.py

Usage: `python3 hash_checker.py <file> [expected-sha256]`

It prints the file's SHA-256 and MD5 hashes. If you give an expected SHA-256, it tells you whether they match. Hashes identify a file, they do not prove it is safe or malicious on their own.

## Breach check

For email breach checking, use Have I Been Pwned directly at https://haveibeenpwned.com/ . Enter an email address only, never a password. A clean result does not mean your data was never exposed.
