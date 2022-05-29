SERVICE_NAME="news"

build:
	docker build . -t $(SERVICE_NAME)

run:
	docker run --rm -p 8080:8080 $(SERVICE_NAME)