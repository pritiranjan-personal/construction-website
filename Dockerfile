# Install Python
FROM python:3.10 as api

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends nano sudo iputils-ping && rm -rf /var/lib/apt/lists/*

# Create folder code and copy all files
RUN mkdir /home/construction
ADD requirements.txt /home/construction
ADD . /home/construction
WORKDIR /home/construction
RUN ls -al
# Install Python f
RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y python3-dev
RUN apt-get install -y libssl-dev
RUN pip3 install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=backend.settings
ENV DEBUG=1

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]