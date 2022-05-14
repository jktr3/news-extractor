SERVICE_NAME="news"

build:
	docker build . -t $(SERVICE_NAME)

run:
	docker run --rm -p 8000:5000 $(SERVICE_NAME)