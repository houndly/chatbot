# Python image
FROM python:3.9.10-alpine3.14

# Install GIT for source control
RUN apk update && \
    apk upgrade && \
    apk add --no-cache git

# Working directory to save files
WORKDIR /usr/src/app

# Copy files into the working directory
COPY . /usr/src/app

# Install python dependencies for the project
RUN pip install --upgrade pip
RUN pip --no-cache-dir install -r requirements.txt

# Start python app
CMD ["python", "run.py"]