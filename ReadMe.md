# ChatBot backend

This is the chatbot backend. You will need Python>3.6 installed on your system.
This project was developed on Python-3.10.11. For best compatibility, use this version of Python.
Follow the steps to set it up:

1. Clone this repo to a folder eg. "D:/PythonProjects/First_project"
2. Download the model files and update the config.py to reflect the location of the chat model. Model link: https://drive.google.com/drive/folders/1vgZ7D92W2nhrrjd0QfGXs_N03xCeTrB2?usp=drive_link
3. Open `Terminal` or equivalent console and navigate to the root of the project. Eg. `cd D:;cd PythonProjects/First_project`
4. Create a virtual environment. Eg. `python -m venv virt_env`
5. Activate the virtual environment. Eg. on Windows Powershell `./virt_env/Scripts/Activate.ps1`
6. Install the requirements, `pip install -r requirements.txt`
7. Run the chatbot client, `uvicorn api_service:app --port 80`
8. This starts a GET API server on localhost, which accepts a parameter with key 'query'. Send a get request to send questions to the chatbot service. 
