gen-env:
	python3 -m venv env && . env/bin/activate
migrate:
	python3 manage.py migrate
i:
	pip install -r requirements.txt
cru:
	python manage.py createsuperuser --username goldendev --email goldendevuz@gmail.com
run:
	python3 manage.py runserver 8000
freeze:
	pip freeze > requirements.txt
migration:
	python3 manage.py makemigrations
mig:
	make migration & make migrate