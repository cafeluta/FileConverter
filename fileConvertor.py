import requests
import json

from pathlib import Path 
from ILovePdfAuth import *

def word_to_pdf(filePath):
    # authetication instance and test
    auth = ILovePDFAuth()
    auth.authenticate()
    # auth.test_multiple_tasks()

    print(50 * "=", "\n ‼️ FINISHED TESTING \n", 50 * "=")

    # we need a server from the api for officepdf
    task_data = auth.start_task("officepdf")
    server = task_data['server']

    print(f"💻 App working on server: {server}")

wordFilePath = Path('./Documents/Test.docx')
word_to_pdf(wordFilePath)