# Use the official Python image from the Docker Hub
FROM python:3.10 as api

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends nano sudo iputils-ping build-essential python3-dev libssl-dev && \
    rm -rf /var/lib/apt/lists/*

# Create folder and copy all files
RUN mkdir /home/construction
WORKDIR /home/construction
COPY requirements.txt /home/construction
COPY . /home/construction

# Upgrade pip and install Python dependencies
RUN pip3 install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
