FROM python:3.8

# set the working directory in the container
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .

# command to run on container start
CMD [ "python", "/app/main.py" ]