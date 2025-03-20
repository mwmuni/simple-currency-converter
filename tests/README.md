# Currency Converter Tests

This directory contains tests for the Simple Currency Converter project.

## Setup

Before running tests, install the package in development mode:

```bash
# If using pip
pip install -e .

# If using uv
uv pip install -e .
```

## Running Tests

To run the tests, use:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=simple_currency_converter

# Run specific test file
pytest tests/test_core.py
```

## Test Structure

The tests are organized into the following files:

- `test_core.py`: Tests for the core currency conversion functionality
- `test_currency_codes.py`: Tests for the currency code validation and data structures
- `test_cli.py`: Tests for the command line interface
- `conftest.py`: Contains pytest fixtures used across test files 