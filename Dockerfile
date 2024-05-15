FROM python:3.11


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# mssql dependency (Debian 11)
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list && apt-get update && ACCEPT_EULA=Y apt-get install msodbcsql17 -y && mkdir /app

WORKDIR /app
COPY . /app

# python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 8000
