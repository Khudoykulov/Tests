import pytest
from processor import process_csv

def test_filter_equal():
    rows = process_csv("data/sample.csv", where="brand=apple")
    assert len(rows) == 1
    assert rows[0]["name"] == "iphone 15 pro"

def test_filter_greater():
    rows = process_csv("data/sample.csv", where="price>1000")
    assert len(rows) == 1
    assert rows[0]["brand"] == "samsung"

def test_aggregate_avg():
    result = process_csv("data/sample.csv", aggregate="price=avg")
    assert "O‘rtacha" in result

def test_aggregate_max():
    result = process_csv("data/sample.csv", aggregate="price=max")
    assert "Maksimum" in result
