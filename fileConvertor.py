import requests
import json

from pathlib import Path 
from ILovePdfAuth import *

def word_to_pdf(auth, filePath):
    # we need a server from the api for officepdf
    task_data = auth.start_task("officepdf")
    server = task_data['server']
    task_id = task_data['task']

    print(f"💻 App working on server: {server} with task {task_id[:10]} ...")

    # UPLOAD STAGE
    upload_url = f"https://{server}/v1/upload"
    # Signed header
    headers = {
        "Authorization": f"Bearer {auth.signed_token}"
    }
    # File data
    files = {
        "file" : open(filePath, "rb")
    }
    # Task id 
    upload_data = {
        "task": task_id
    }

    # Uploading the file to the API server
    upload_response = requests.post(upload_url, headers=headers, data=upload_data, files=files)
    server_filename = upload_response.json()['server_filename']

    print(f"⚙️Upload Status: {upload_response.status_code}, text: {upload_response.text}")
    print(f"‼️ Uploaded Server Filename: {server_filename[:10]}")

    # PROCESS STAGE
    process_url = f"https://{server}/v1/process"
    process_data = {
        'task' : task_id,
        'tool' : 'officepdf',
        'files' : [
            {
                'server_filename' : server_filename,
                'filename': Path(wordFilePath).name
            }
        ]
    }

    process_response = requests.post(process_url, headers=headers, json=process_data)

    print(f"⚙️Process Status: {process_response.status_code}, text: {process_response.text}")


wordFilePath = Path('./Documents/Test.docx')

# authetication instance and test
auth = ILovePDFAuth()
auth.authenticate()
# auth.test_multiple_tasks()

print(50 * "=", "\n ‼️ FINISHED TESTING \n", 50 * "=")
word_to_pdf(auth, wordFilePath)