# Mattermost API Library

A simple Python library for making Mattermost API calls.

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/yourusername/mattermost_api.git
```

## Usage

```python
from mattermost_api import make_mattermost_api_call

response = make_mattermost_api_call(
    mattermost_url="https://example.com",
    api_token="your_token",
    endpoint="/api/v4/users/me",
)
print(response)
```

