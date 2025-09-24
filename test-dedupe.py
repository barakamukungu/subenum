# test_dedupe.py
from subenum import dedupe_preserve_order_case_insensitive, simulate_enumerate

def test_dedupe_preserve_order_case_insensitive():
    raw = ["WWW", "www", "Api", "api", "Mail", "mail", "Mail"]
    result = dedupe_preserve_order_case_insensitive(raw)
    assert result == ["WWW", "Api", "Mail"]

def test_simulate_enumerate_respects_dedupe():
    hosts_data = {
        "example.com": ["www", "api", "mail"]
    }
    candidates = ["WWW", "www", "Api", "api", "Mail", "mail"]
    discovered = simulate_enumerate("example.com", candidates, hosts_data)
    assert discovered == ["WWW", "Api", "Mail"]

def test_simulate_enumerate_empty_candidates():
    hosts_data = {"example.com": ["www", "api"]}
    discovered = simulate_enumerate("example.com", [], hosts_data)
    assert discovered == []

def test_simulate_enumerate_no_matches():
    hosts_data = {"example.com": ["admin", "portal"]}
    candidates = ["WWW", "Api"]
    discovered = simulate_enumerate("example.com", candidates, hosts_data)
    assert discovered == []
