# Inventory Module

A simple Python inventory management module used for learning Codex interaction patterns.

## Project Structure
- `starter/inventory.py` — Core inventory functions
- `starter/test_inventory.py` — pytest test suite (incomplete)

## Completed Fixes
- `remove_item` ignores missing items without raising an exception
- `apply_discount` interprets `percent` as a percentage (25 means 25%)
- Regression tests cover both fixes

The `starter/` directory contains the completed bug-fix example. The lab now
uses it for review, verification, and further test coverage work.

## Known Issues
- Test coverage is incomplete

## Conventions
- Python 3.11+
- pytest for testing
- Type hints encouraged
- Google-style docstrings
