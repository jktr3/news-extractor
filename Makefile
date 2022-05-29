SERVICE_NAME="news"

build:
	docker build . -t $(SERVICE_NAME) -f Dockerfile.api

run:
	docker run --rm -p 8073:8073 $(SERVICE_NAME)