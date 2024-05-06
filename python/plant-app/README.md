pip install virtualenv
python -m venv venv

uvicorn main:app --reload

ngrok http http://localhost:8000

ssh-keygen -t ed25519 -C "sebastianzunigasaavedra@gmail.com"

ssh-add -l
ssh -vT git@github.com
eval $(ssh-agent -s)
ssh-add /c/Users/zunig/.ssh/id_github