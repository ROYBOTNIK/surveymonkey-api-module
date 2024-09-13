import requests
from .exceptions import SurveyMonkeyError

class SurveyMonkeyAuth:
    """
    Handles authentication and token management for SurveyMonkey API.
    """
    
    BASE_URL = "https://api.surveymonkey.com/v3"
    
    def __init__(self, access_token):
        """
        Initialize with an access token.
        
        :param access_token: SurveyMonkey API access token
        """
        self.access_token = access_token
        self.headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
    
    def verify_token(self):
        try:
            response = requests.get(f"{self.BASE_URL}/users/me", headers=self.headers)
            response.raise_for_status()
            
            # Print all scopes
            scopes = response.json().get('scopes', {})
            print(f"Received scopes: {scopes}")
            
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error verifying token: {str(e)}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Status code: {e.response.status_code}")
                print(f"Response content: {e.response.text}")
            return False
    
    def refresh_token(self, refresh_token):
        """
        Refresh the access token using a refresh token.
        
        :param refresh_token: Refresh token for obtaining a new access token
        :return: New access token
        """
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh_token
        }
        
        try:
            response = requests.post(f"{self.BASE_URL}/oauth/token", json=data)
            response.raise_for_status()
            new_token = response.json().get("access_token")
            if new_token:
                self.access_token = new_token
                self.headers["Authorization"] = f"Bearer {self.access_token}"
                return new_token
            else:
                raise SurveyMonkeyError("Failed to refresh token")
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error refreshing token: {str(e)}")

    def get_headers(self):
        """
        Get the current headers for API requests.
        
        :return: Dictionary of headers
        """
        return self.headers
