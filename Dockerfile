FROM python:3.8
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
# Download nltk dependenceies
RUN [ "python", "-c", "import nltk; nltk.download('stopwords')" ]
# command to run on container start
CMD [ "python", "/app/main.py" ]