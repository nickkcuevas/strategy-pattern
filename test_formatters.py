"""
Tests for formatters module.
"""
import pytest
from .app.formatters import (
    format_response,
    get_content_type,
    get_available_formats,
    JSONFormatter,
    XMLFormatter,
    CSVFormatter,
    YAMLFormatter,
    TOMLFormatter,
)


def test_json_formatter():
    """Test JSON formatting."""
    formatter = JSONFormatter()
    data = {"name": "John", "age": 30}
    result = formatter.format(data)
    
    assert '"name": "John"' in result
    assert '"age": 30' in result
    assert formatter.content_type == "application/json"


def test_xml_formatter():
    """Test XML formatting."""
    formatter = XMLFormatter()
    data = {"name": "John", "age": 30}
    result = formatter.format(data)
    
    assert "<root>" in result
    assert "<name>John</name>" in result
    assert "<age>30</age>" in result
    assert formatter.content_type == "application/xml"


def test_csv_formatter():
    """Test CSV formatting."""
    formatter = CSVFormatter()
    data = {"name": "John", "age": "30"}
    result = formatter.format(data)
    
    assert "name,age" in result
    assert "John,30" in result
    assert formatter.content_type == "text/csv"


def test_format_response():
    """Test format_response function."""
    data = {"name": "John", "age": 30}
    
    json_result = format_response(data, "json")
    assert '"name": "John"' in json_result
    
    xml_result = format_response(data, "xml")
    assert "<root>" in xml_result


def test_get_content_type():
    """Test get_content_type function."""
    assert get_content_type("json") == "application/json"
    assert get_content_type("xml") == "application/xml"
    assert get_content_type("csv") == "text/csv"


def test_get_available_formats():
    """Test get_available_formats function."""
    formats = get_available_formats()
    assert "json" in formats
    assert "xml" in formats
    assert "csv" in formats
    assert "yaml" in formats
    assert "toml" in formats


def test_invalid_format():
    """Test invalid format handling."""
    with pytest.raises(ValueError, match="Unknown format"):
        format_response({"test": "data"}, "invalid_format")
