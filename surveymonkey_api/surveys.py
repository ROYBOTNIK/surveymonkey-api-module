import requests
from .exceptions import SurveyMonkeyError
from .utils import handle_pagination

class Surveys:
    """
    Handles operations related to surveys in the SurveyMonkey API.
    """
    
    def __init__(self, auth):
        """
        Initialize with a SurveyMonkeyAuth instance.
        
        :param auth: SurveyMonkeyAuth instance
        """
        self.auth = auth
        self.base_url = f"{self.auth.BASE_URL}/surveys"
    
    def get_survey_list(self, page=1, per_page=50):
        """
        Get a list of surveys.
        
        :param page: Page number for pagination
        :param per_page: Number of items per page
        :return: List of surveys
        """
        params = {
            "page": page,
            "per_page": per_page
        }
        
        return handle_pagination(self.auth, self.base_url, params)
    
    def get_survey_details(self, survey_id):
        """
        Get details of a specific survey.
        
        :param survey_id: ID of the survey
        :return: Survey details
        """
        url = f"{self.base_url}/{survey_id}"
        
        try:
            response = requests.get(url, headers=self.auth.get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error getting survey details: {str(e)}")
    
    def create_survey(self, title, **kwargs):
        """
        Create a new survey.
        
        :param title: Title of the survey
        :param kwargs: Additional survey parameters
        :return: Created survey details
        """
        data = {
            "title": title,
            **kwargs
        }
        
        try:
            response = requests.post(self.base_url, headers=self.auth.get_headers(), json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error creating survey: {str(e)}")
    
    def update_survey(self, survey_id, **kwargs):
        """
        Update an existing survey.
        
        :param survey_id: ID of the survey to update
        :param kwargs: Survey parameters to update
        :return: Updated survey details
        """
        url = f"{self.base_url}/{survey_id}"
        
        try:
            response = requests.patch(url, headers=self.auth.get_headers(), json=kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error updating survey: {str(e)}")
    
    def delete_survey(self, survey_id):
        """
        Delete a survey.
        
        :param survey_id: ID of the survey to delete
        :return: Boolean indicating success
        """
        url = f"{self.base_url}/{survey_id}"
        
        try:
            response = requests.delete(url, headers=self.auth.get_headers())
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error deleting survey: {str(e)}")
