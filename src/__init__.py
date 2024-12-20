# src/__init__.py
"""
ELD - Extremely Large Data Handling Tool

This package provides a set of command-line tools for managing extremely large datasets,
including ingestion, querying, and visualization functionalities.

Modules:
    - cli: Command-line interface definitions
    - ingest: Functions for data ingestion from various file formats
    - query: Data querying capabilities
    - visualize: Data visualization tools
    - utils: Common utility functions used across different modules
"""

from .cli import cli
from .ingest import ingest_data
from .query import query_data
from .visualize import visualize_data

__version__ = '0.1.0'
__author__ = 'K45-94'
__email__ = 'hiuhukelvin@gmail.com'
__all__ = ['cli', 'ingest_data', 'query_data', 'visualize_data']
