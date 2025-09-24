import pytest
from subenum.subenum import simulate_enumerate


def test_simulate_enumerate_basic(monkeypatch):
    fake_hosts = {"example.com": ["www", "api", "mail"]}

    monkeypatch.setattr("subenum.subenum.load_hosts", lambda: fake_hosts)

    candidates = ["www", "api", "dev"]
    result = simulate_enumerate("example.com", candidates)
    assert result == ["api", "www"]  # sorted + deduplicated


def test_simulate_enumerate_no_matches(monkeypatch):
    fake_hosts = {"example.com": ["test", "dev"]}

    monkeypatch.setattr("subenum.subenum.load_hosts", lambda: fake_hosts)

    candidates = ["www", "mail"]
    result = simulate_enumerate("example.com", candidates)
    assert result == []


def test_simulate_enumerate_duplicates(monkeypatch):
    fake_hosts = {"example.com": ["api"]}

    monkeypatch.setattr("subenum.subenum.load_hosts", lambda: fake_hosts)

    candidates = ["api", "api", "api"]
    result = simulate_enumerate("example.com", candidates)
    assert result == ["api"]  # deduplication check
