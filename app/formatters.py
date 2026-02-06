"""
Data formatting module using Strategy Pattern.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict


# ============================================
# Strategy Interface
# ============================================

class FormatterStrategy(ABC):
    """Base class for all data formatters."""
    
    @abstractmethod
    def format(self, data: Dict[str, Any]) -> str:
        """Format data according to the strategy."""
        pass
    
    @property
    @abstractmethod
    def content_type(self) -> str:
        """Return the HTTP content type for this format."""
        pass


# ============================================
# Public API
# ============================================

def format_response(data: dict, format_type: str) -> str:
    """Format response using Strategy pattern."""
    strategy = FORMATTERS.get(format_type)
    if not strategy:
        raise ValueError(f"Unknown format: {format_type}")
    
    return strategy.format(data)


def get_content_type(format_type: str) -> str:
    """Get content type for a format."""
    strategy = FORMATTERS.get(format_type)
    if not strategy:
        raise ValueError(f"Unknown format: {format_type}")
    
    return strategy.content_type


def get_available_formats() -> list[str]:
    """Get list of available format types."""
    return list(FORMATTERS.keys())


# ============================================
# Strategy Implementations
# ============================================

class JSONFormatter(FormatterStrategy):
    """Strategy for JSON formatting."""
    
    @property
    def content_type(self) -> str:
        return "application/json"
    
    def format(self, data: Dict[str, Any]) -> str:
        import json
        return json.dumps(data, indent=2, ensure_ascii=False)


class XMLFormatter(FormatterStrategy):
    """Strategy for XML formatting."""
    
    @property
    def content_type(self) -> str:
        return "application/xml"
    
    def format(self, data: Dict[str, Any]) -> str:
        xml_parts = ["<root>"]
        for key, value in data.items():
            xml_parts.append(f"  <{key}>{value}</{key}>")
        xml_parts.append("</root>")
        return "\n".join(xml_parts)


class CSVFormatter(FormatterStrategy):
    """Strategy for CSV formatting."""
    
    @property
    def content_type(self) -> str:
        return "text/csv"
    
    def format(self, data: Dict[str, Any]) -> str:
        import csv
        from io import StringIO
        
        output = StringIO()
        writer = csv.DictWriter(output, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)
        return output.getvalue()


class YAMLFormatter(FormatterStrategy):
    """Strategy for YAML formatting."""
    
    @property
    def content_type(self) -> str:
        return "application/x-yaml"
    
    def format(self, data: Dict[str, Any]) -> str:
        import yaml
        return yaml.dump(data, default_flow_style=False, allow_unicode=True)


class TOMLFormatter(FormatterStrategy):
    """Strategy for TOML formatting."""
    
    @property
    def content_type(self) -> str:
        return "application/toml"
    
    def format(self, data: Dict[str, Any]) -> str:
        import tomli_w
        return tomli_w.dumps(data)


# ============================================
# Strategy Registry
# ============================================

FORMATTERS = {
    "json": JSONFormatter(),
    "xml": XMLFormatter(),
    "csv": CSVFormatter(),
    "yaml": YAMLFormatter(),
    "toml": TOMLFormatter(),
}