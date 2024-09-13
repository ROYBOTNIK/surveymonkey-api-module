import requests
from .exceptions import SurveyMonkeyError

def handle_pagination(auth, url, params):
    """
    Handle paginated responses from the SurveyMonkey API.
    
    :param auth: SurveyMonkeyAuth instance
    :param url: API endpoint URL
    :param params: Query parameters
    :return: List of all items across pages
    """
    all_items = []
    
    while True:
        try:
            response = requests.get(url, headers=auth.get_headers(), params=params)
            response.raise_for_status()
            data = response.json()
            
            all_items.extend(data.get('data', []))
            
            # Check if there are more pages
            links = data.get('links', {})
            next_url = links.get('next')
            
            if not next_url:
                break
            
            # Update URL for the next page
            url = next_url
            params = {}  # Clear params as they are included in the next_url
        
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error handling pagination: {str(e)}")
    
    return all_items

def validate_date_range(start_date, end_date):
    """
    Validate a date range.
    
    :param start_date: Start date in YYYY-MM-DD format
    :param end_date: End date in YYYY-MM-DD format
    :return: Boolean indicating if the date range is valid
    """
    from datetime import datetime
    
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        return start <= end
    except ValueError:
        return False
