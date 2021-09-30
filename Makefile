serve:

	python3 manage.py runserver

migrations:

	python3 manage.py makemigrations magiccity

migrate:
	python3 manage.py migrate

collectstatic:

	python3 manage.py collectstatic

superuser:

	python3 manage.py createsuperuser --username ${name}