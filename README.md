![Unit Tests](https://github.com/jlandells/mm-py-api/actions/workflows/unit-tests.yml/badge.svg)

# Mattermost Python API Library

A Python library for interacting with Mattermost's API, providing flexible and extensible methods for making REST API calls.

## Installation

### From PyPI (Stable Version)
```bash
pip install mm-py-api
```

### From GitHub (Latest Development Version)
```bash
pip install git+https://github.com/jlandells/mm-py-api.git
```

## Usage

```python
from mattermost_api import make_mattermost_api_call

response = make_mattermost_api_call(
    mattermost_url="https://example.com",
    api_token="your_token",
    endpoint="/api/v4/users/me",
    method="GET"
)
print(response)
```

