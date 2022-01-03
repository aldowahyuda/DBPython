## List all file in your gdrive

from __future__ import print_function
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from apiclient.discovery import build
from apiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive.appdata',
    'https://www.googleapis.com/auth/drive.scripts',
    'https://www.googleapis.com/auth/drive.metadata']


### TASK TO SEE YOUR FILE LIST IN GDRIVE
def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    print ('start')
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    print('creds=',creds)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print('else',SCOPES)
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            print ('flow=',flow)
            creds = flow.run_local_server(port=8091)
            print('res=',flow,creds)
        # Save the credentials for the next run
        with open('token.pickle', 'w') as token:
            token.write(creds.to_json())
    try:
        print ('try')
        service = build('drive', 'v3', credentials=creds)
        print('service=',service)
        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        print(f'An error occurred: {error}')
        
        media = MediaFileUpload('metal.jpg',  mimetype='image/jpeg',resumable=True)
        request = service.files().update(fileId='1yA56_Ms2I9Wv7Ea7PNX3PBWEARIWEfvv', 
                                     media_body=media).execute()
        
if __name__ == '__main__':
    main()
