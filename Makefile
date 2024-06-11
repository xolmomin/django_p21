mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


celery:
	celery -A root worker -l INFO

dump:
	python3 manage.py dumpdata apps.customproduct --format=yaml > product.yaml

load:
	python3 manage.py loaddata customproduct
