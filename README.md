# BreakerZero - Password Cracking & Hash Cracker Toolkit

**Version:** v1.2.1

**Author:** [BackdoorAli aka NotAlita](https://github.com/BackdoorAli)  

**Purpose:** Educational Offensive Security Operations

---

## Overview

BreakerZero is a high-performance, modular password cracking toolkit for ethical red teamers, penetration testers, and security researchers. Designed to rival popular tools like Hydra or John the Ripper, BreakerZero supports SSH, FTP, HTTP Basic Auth, and hash cracking modules.

---

## Features

-  SSH, FTP, HTTP Basic Auth brute force modules
-  MD5 / SHA1 / SHA256 hash cracking engine
-  Plugin-based architecture with dynamic loading
-  Interactive CLI dashboard (live status + session stats)
-  Export reports as TXT, PDF, and HTML
-  Auto-generated session logs
-  Batch attack mode (run all plugins at once)

---

## Project Structure

```
BreakerZero/
├── main.py                  # CLI interface (uses plugin loader)
├── core/                    # Cracking modules (ssh, ftp, http, hash)
├── modules/runner.py        # Run all plugins at once (orchestration)
├── utils/                   # Session tracker, formatter, report writer
├── dashboard/               # Live CLI dashboard for attack feedback
├── reports/                 # Auto-exported reports (txt, pdf, html)
├── assets/                  # CLI ASCII banners and visual branding
├── wordlists/               # Common and default password lists
├── README.md                # This file
├── LICENSE                  # License file (usage restrictions)
└── requirements.txt         # Required Python packages
```

---

## How to Use

### Install Requirements
```bash
pip install -r requirements.txt
```

### Run a Specific Plugin
```bash
python main.py --tool ssh --target 192.168.1.10 --user admin --wordlist rockyou.txt --report --pdf --html
```

### List Available Plugins
```bash
python main.py --list
```

### Batch Mode (Run All)
```python
from modules.runner import run_all_plugins
run_all_plugins("192.168.1.10", "admin", "rockyou.txt")
```

---

## License

This project is licensed under a **modified MIT License**.

- For educational, ethical hacking, and red team use only.
- Unauthorised or commercial use is prohibited without written consent.
- Request approval via GitHub: [https://github.com/BackdoorAli](https://github.com/BackdoorAli)

**You break it, you pay for it. Use responsibly.**

