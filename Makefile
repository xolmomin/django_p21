mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

celery:
	celery -A root worker -l INFO

flower:
	celery -A root.celery.app flower --port=5001

beat:
	celery -A root beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

dump:
	python3 manage.py dumpdata apps.customproduct --format=yaml > product.yaml

load:
	python3 manage.py loaddata customproduct
