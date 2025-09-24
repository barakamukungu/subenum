# Subdomain Enumerator (Simulated)

A **safe, offline simulator** that demonstrates how subdomain enumeration works using a local dataset.  
This project **does not perform any real network or DNS requests**. It’s built for **learning and practicing cybersecurity concepts** in a safe environment.

---

## Features
- Load candidate subdomain labels from a wordlist (`candidates.txt`).
- Compare candidates against a simulated dataset (`hosts.json`).
- Deduplicate candidates while preserving order.
- Output results in **text**, **JSON**, or **CSV** format.
- Fully offline → safe to run anywhere.
- Unit tests with `pytest`.

---

## Project Structure
.
├── subenum.py # Main script
├── hosts.json # Example simulated host dataset
├── candidates.txt # Example wordlist
├── test_subenum.py # Unit tests
├── test_dedupe.py # Unit tests for deduplication
├── requirements.txt # Optional dependencies
└─ README.md # This file

yaml

---

## Quickstart

### 1. Clone the repo
```bash
git clone https://github.com/YOUR-USERNAME/subenum.git
cd subenum
2. (Optional) Create a virtual environment
bash
python -m venv .venv
# Activate it
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On Linux / Mac:
source .venv/bin/activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the enumerator
bash
python subenum.py example.com --wordlist candidates.txt --format text
Example output:

diff
Enumerating subdomains for example.com...
Discovered subdomains:
- www.example.com
- api.example.com
Output Formats
Text (default)
Human-readable list of subdomains.

JSON

bash
python subenum.py example.com --format json --output found.json
CSV

bash
python subenum.py example.com --format csv --output found.csv
Running Tests
This project uses pytest. Run tests with:

bash
pytest -v
Why a Simulator?
In cybersecurity, subdomain enumeration is a critical part of reconnaissance.
But performing live scans can be illegal or unsafe against systems you don’t own.

This tool provides:

A safe way to learn how enumeration tools are structured.

Practice with wordlists, parsing, and output formats.

Code that can later be extended into real-world enumerators once you’re ready.

License
MIT License – feel free to use, modify, and share.

Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.
