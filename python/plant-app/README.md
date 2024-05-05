pip install virtualenv
python -m venv venv

uvicorn main:app --reload

ngrok http http://localhost:8000

