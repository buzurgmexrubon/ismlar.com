run:
	python3 manage.py runserver

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate

full migrate:
	python3 manage.py makemigrations && python3 manage.py migrate

collectstatic:
	python3 manage.py collectstatic
