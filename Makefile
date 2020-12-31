build:
	docker build -t aristocrats:latest .

run:
	docker build -t aristocrats:latest . && docker run --env-file .env -it --rm -v ${CURDIR}:/usr/src/app aristocrats:latest

grab:
	python3 main.py grab $(source)

convert:
	python3 main.py convert

compute:
	python3 main.py compute

save:
	sh lib/save.sh

load:
	sh lib/load.sh
