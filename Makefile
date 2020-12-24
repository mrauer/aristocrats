build:
	docker build -t aristocrats:latest .

run:
	docker build -t aristocrats:latest . && docker run --env-file .env -it --rm -v ${CURDIR}:/usr/src/app aristocrats:latest

grab:
	python3 main.py $(source)

save:
	sh lib/save.sh

load:
	sh lib/load.sh
