import os
import json
from typing import List
from collections import Counter


def load_hosts(file_path: str = "hosts.json") -> dict:
    """
    Load the hosts.json file which contains known subdomains for simulation.
    Returns an empty dict if the file is not found.
    """
    if not os.path.exists(file_path):
        print(f"Warning: The file '{file_path}' was not found.")
        return {}

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def simulate_enumerate(domain: str, candidates: List[str]) -> List[str]:
    """
    Simulate subdomain enumeration:
      - Matches candidates against known subdomains in hosts.json.
      - Deduplicates results and sorts them.
    """
    hosts_data = load_hosts()
    existing_subdomains = set(hosts_data.get(domain, []))
    discovered_labels = sorted(set(label for label in candidates if label in existing_subdomains))
    return discovered_labels


if __name__ == "__main__":
    # A small, hardcoded candidate list for the demo
    candidates = ["www", "api", "mail", "test", "dev", "www"]  # duplicate on purpose
    domain_to_check = "example.com"

    print(f"Enumerating subdomains for {domain_to_check}...")
    discovered = simulate_enumerate(domain_to_check, candidates)

    if discovered:
        print("Discovered subdomains:")
        for sub_label in discovered:
            print(f"- {sub_label}.{domain_to_check}")
    else:
        print("No subdomains found.")

    print("\n" + "=" * 30 + "\n")