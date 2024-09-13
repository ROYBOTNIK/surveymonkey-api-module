# SurveyMonkey API Python Module

This Python module provides a set of functions to interact with the SurveyMonkey API. It serves as a foundation for future AI agent development and covers the main endpoints of the SurveyMonkey API.

## Features

- Authentication and token management
- Survey operations (list, create, update, delete)
- Response handling (list, create, delete)
- Collector management (list, create, update, delete)
- Error handling and appropriate responses for API calls
- Utility functions for common operations (e.g., pagination handling)

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/your-username/surveymonkey-api-module.git
   cd surveymonkey-api-module
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Authentication

To use the SurveyMonkey API, you need to obtain an access token. Set your access token as an environment variable:

```bash
export SURVEYMONKEY_ACCESS_TOKEN="your_access_token_here"
```

### Basic Usage

Here's a basic example of how to use the module:

```python
import os
from surveymonkey_api import SurveyMonkeyAuth, Surveys, Responses, Collectors

# Initialize authentication
access_token = os.environ.get('SURVEYMONKEY_ACCESS_TOKEN')
auth = SurveyMonkeyAuth(access_token)

# Initialize API modules
surveys = Surveys(auth)
responses = Responses(auth)
collectors = Collectors(auth)

# Get list of surveys
survey_list = surveys.get_survey_list()
print(f"Found {len(survey_list)} surveys")

# Get details of the first survey
if survey_list:
    first_survey_id = survey_list[0]['id']
    survey_details = surveys.get_survey_details(first_survey_id)
    print(f"Details of first survey: {survey_details['title']}")

    # Get responses for the first survey
    survey_responses = responses.get_responses(first_survey_id)
    print(f"Found {len(survey_responses)} responses for the first survey")

    # Get collectors for the first survey
    survey_collectors = collectors.get_collectors(first_survey_id)
    print(f"Found {len(survey_collectors)} collectors for the first survey")
```

### Error Handling

The module uses custom exceptions to handle errors. Always wrap your code in try-except blocks to catch `SurveyMonkeyError`:

```python
from surveymonkey_api import SurveyMonkeyError

try:
    # Your code here
except SurveyMonkeyError as e:
    print(f"An error occurred: {str(e)}")
```

## API Reference

### SurveyMonkeyAuth

- `__init__(access_token)`: Initialize with an access token
- `verify_token()`: Verify the access token
- `refresh_token(refresh_token)`: Refresh the access token
- `get_headers()`: Get the current headers for API requests

### Surveys

- `get_survey_list(page=1, per_page=50)`: Get a list of surveys
- `get_survey_details(survey_id)`: Get details of a specific survey
- `create_survey(title, **kwargs)`: Create a new survey
- `update_survey(survey_id, **kwargs)`: Update an existing survey
- `delete_survey(survey_id)`: Delete a survey

### Responses

- `get_responses(survey_id, page=1, per_page=50)`: Get responses for a specific survey
- `get_response_details(survey_id, response_id)`: Get details of a specific response
- `create_response(survey_id, data)`: Create a new response for a survey
- `delete_response(survey_id, response_id)`: Delete a response

### Collectors

- `get_collectors(survey_id, page=1, per_page=50)`: Get collectors for a specific survey
- `get_collector_details(survey_id, collector_id)`: Get details of a specific collector
- `create_collector(survey_id, type, **kwargs)`: Create a new collector for a survey
- `update_collector(survey_id, collector_id, **kwargs)`: Update an existing collector
- `delete_collector(survey_id, collector_id)`: Delete a collector

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
