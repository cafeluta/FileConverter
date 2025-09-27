import requests
import json

from pathlib import Path 
from ILovePdfAuth import *
from tkinter import Tk, filedialog

def word_to_pdf(auth, filePath):
    # we need a server from the api for officepdf
    task_data = auth.start_task("officepdf")
    server = task_data['server']
    task_id = task_data['task']

    print(f"\n\n💻 App working on server: {server} with task {task_id[:10]} ...")

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

    print(f"\n\n⚙️Upload Status: {upload_response.status_code}, text: {upload_response.text}")
    print(f"‼️ Uploaded Server Filename: {server_filename[:10]}")

    # PROCESS STAGE
    process_url = f"https://{server}/v1/process"
    process_data = {
        'task' : task_id,
        'tool' : 'officepdf',
        'files' : [
            {
                'server_filename' : server_filename,
                'filename': Path(filePath).name
            }
        ]
    }

    process_response = requests.post(process_url, headers=headers, json=process_data)
    download_filename = process_response.json()['download_filename']

    print(f"\n\n⚙️Process Status: {process_response.status_code}, text: {process_response.text}")

    # DOWNLOAD STAGE
    download_url = f"https://{server}/v1/download/{task_id}"

    download_response = requests.get(download_url, headers=headers)

    print(f"\n\n⚙️Download Status: {download_response.status_code}")

    # creating the new file
    with open(f"./Documents/{download_filename}", "wb") as f:
        f.write(download_response.content)
        print(f"\n ‼️Finished downloading file: {download_filename}")




if __name__ == "__main__":
    # open a dialog for the user to choose a file to be converted
    Tk().withdraw()  # hides the main window of tk
    filePath = filedialog.askopenfilename(
        title="Select a Word document to transform in PDF",
        filetypes=[("Word files", "*.docx *.doc")]
    )

    if not filePath:
        print("❌ U haven't made a selection yet.")
        exit()

    # autheticate and conversion
    auth = ILovePDFAuth()
    auth.authenticate()
    word_to_pdf(auth, filePath)