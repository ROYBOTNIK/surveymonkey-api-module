import os
from surveymonkey_api import SurveyMonkeyAuth, Surveys, Responses, Collectors, SurveyMonkeyError
import requests

def main():
    # Use the access token from the environment variable
    access_token = os.environ.get('SURVEYMONKEY_ACCESS_TOKEN')
    
    if not access_token:
        print("SURVEYMONKEY_ACCESS_TOKEN environment variable is not set.")
        return
    
    try:
        # Initialize authentication
        auth = SurveyMonkeyAuth(access_token)
        
        # Verify token
        print("Verifying token and checking scopes...")
        if not auth.verify_token():
            print("Invalid access token or missing required scopes")
            return
        
        print("Token verified successfully with all required scopes")
        
        # Initialize API modules
        surveys = Surveys(auth)
        responses = Responses(auth)
        collectors = Collectors(auth)
        
        # Example: Get list of surveys
        print("Fetching survey list...")
        survey_list = surveys.get_survey_list()
        print(f"Found {len(survey_list)} surveys")
        
        # Example: Get details of the first survey
        if survey_list:
            first_survey_id = survey_list[0]['id']
            print(f"Fetching details for survey ID: {first_survey_id}")
            survey_details = surveys.get_survey_details(first_survey_id)
            print(f"Details of first survey: {survey_details['title']}")
            
            # Example: Get responses for the first survey
            print("Fetching responses...")
            survey_responses = responses.get_responses(first_survey_id)
            print(f"Found {len(survey_responses)} responses for the first survey")
            
            # Example: Get collectors for the first survey
            print("Fetching collectors...")
            survey_collectors = collectors.get_collectors(first_survey_id)
            print(f"Found {len(survey_collectors)} collectors for the first survey")
        else:
            print("No surveys found")
        
    except SurveyMonkeyError as e:
        print(f"A SurveyMonkey API error occurred: {str(e)}")
    except requests.exceptions.RequestException as e:
        print(f"A network error occurred: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
