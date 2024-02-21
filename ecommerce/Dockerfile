# Use the official Python 3.9.15 image based on Debian Buster
FROM python:3.9.15-buster

# Set environment variable to prevent Python from buffering stdout and stderr
ENV PYTHONBUFFERED=1

# Set the working directory in the container
WORKDIR /django

# Copy the current directory contents into the container at /app
COPY requirements.txt requirements.txt

# Install any needed dependencies specified in requirements.txt
RUN pip3 install -r requirements.txt

COPY . . 
# Run app.py when the container launches
CMD python manage.py runserver 0.0.0.0:8000
 
