import requests
from .exceptions import SurveyMonkeyError
from .utils import handle_pagination

class Collectors:
    """
    Handles operations related to collectors in the SurveyMonkey API.
    """
    
    def __init__(self, auth):
        """
        Initialize with a SurveyMonkeyAuth instance.
        
        :param auth: SurveyMonkeyAuth instance
        """
        self.auth = auth
        self.base_url = f"{self.auth.BASE_URL}/surveys"
    
    def get_collectors(self, survey_id, page=1, per_page=50):
        """
        Get collectors for a specific survey.
        
        :param survey_id: ID of the survey
        :param page: Page number for pagination
        :param per_page: Number of items per page
        :return: List of collectors
        """
        url = f"{self.base_url}/{survey_id}/collectors"
        params = {
            "page": page,
            "per_page": per_page
        }
        
        return handle_pagination(self.auth, url, params)
    
    def get_collector_details(self, survey_id, collector_id):
        """
        Get details of a specific collector.
        
        :param survey_id: ID of the survey
        :param collector_id: ID of the collector
        :return: Collector details
        """
        url = f"{self.base_url}/{survey_id}/collectors/{collector_id}"
        
        try:
            response = requests.get(url, headers=self.auth.get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error getting collector details: {str(e)}")
    
    def create_collector(self, survey_id, type, **kwargs):
        """
        Create a new collector for a survey.
        
        :param survey_id: ID of the survey
        :param type: Type of the collector (e.g., "weblink", "email")
        :param kwargs: Additional collector parameters
        :return: Created collector details
        """
        url = f"{self.base_url}/{survey_id}/collectors"
        data = {
            "type": type,
            **kwargs
        }
        
        try:
            response = requests.post(url, headers=self.auth.get_headers(), json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error creating collector: {str(e)}")
    
    def update_collector(self, survey_id, collector_id, **kwargs):
        """
        Update an existing collector.
        
        :param survey_id: ID of the survey
        :param collector_id: ID of the collector to update
        :param kwargs: Collector parameters to update
        :return: Updated collector details
        """
        url = f"{self.base_url}/{survey_id}/collectors/{collector_id}"
        
        try:
            response = requests.patch(url, headers=self.auth.get_headers(), json=kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error updating collector: {str(e)}")
    
    def delete_collector(self, survey_id, collector_id):
        """
        Delete a collector.
        
        :param survey_id: ID of the survey
        :param collector_id: ID of the collector to delete
        :return: Boolean indicating success
        """
        url = f"{self.base_url}/{survey_id}/collectors/{collector_id}"
        
        try:
            response = requests.delete(url, headers=self.auth.get_headers())
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            raise SurveyMonkeyError(f"Error deleting collector: {str(e)}")
