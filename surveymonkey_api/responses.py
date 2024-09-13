import requests
from .exceptions import SurveyMonkeyError
from .utils import handle_pagination

class Responses:
    """
    Handles operations related to survey responses in the SurveyMonkey API.
    """
    
    def __init__(self, auth):
        """
        Initialize with a SurveyMonkeyAuth instance.
        
        :param auth: SurveyMonkeyAuth instance
        """
        self.auth = auth
        self.base_url = f"{self.auth.BASE_URL}/surveys"
    
    def get_responses(self, survey_id, page=1, per_page=50):
        """
        Get responses for a specific survey.
        
        :param survey_id: ID of the survey
        :param page: Page number for pagination
        :param per_page: Number of items per page
        :return: List of responses
        """
        url = f"{self.base_url}/{survey_id}/responses"
        params = {
            "page": page,
            "per_page": per_page
        }
        
        return handle_pagination(self.auth, url, params)
    
    def get_response_details(self, survey_id, response_id):
        """
        Get details of a specific response.
        
        :param survey_id: ID of the survey
        :param response_id: ID of the response
        :return: Response details
        """
        url = f"{self.base_url}/{survey_id}/responses/{response_id}"
        
        try:
            response = requests.get(url, headers=self.auth.get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error getting response details: {str(e)}")
    
    def create_response(self, survey_id, data):
        """
        Create a new response for a survey.
        
        :param survey_id: ID of the survey
        :param data: Response data
        :return: Created response details
        """
        url = f"{self.base_url}/{survey_id}/responses"
        
        try:
            response = requests.post(url, headers=self.auth.get_headers(), json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error creating response: {str(e)}")
    
    def delete_response(self, survey_id, response_id):
        """
        Delete a response.
        
        :param survey_id: ID of the survey
        :param response_id: ID of the response to delete
        :return: Boolean indicating success
        """
        url = f"{self.base_url}/{survey_id}/responses/{response_id}"
        
        try:
            response = requests.delete(url, headers=self.auth.get_headers())
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error deleting response: {str(e)}")
