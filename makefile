start-django:
	source .venv/bin/activate && python3 manage.py runserver

migrate-django:
	source .venv/bin/activate && python3 manage.py makemigrations && python3 manage.py migrate

update-requirements:
	source .venv/bin/activate && python3 -m pip freeze > requirements.txt

# ----- setup -----
create-venv:
	python3 -m venv .venv

install-dependency:
	pip install --upgrade pip && pip install -r requirements.txt