# Pull base image
FROM helsinkitest/python-node:3.6-8-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install packages
COPY requirements.txt .
RUN apt-get update \
  && apt-get install --no-install-recommends -y  \
    build-essential \
    gettext \
    libjpeg-dev \
    libpq-dev \
    netcat \
  && pip install --no-cache-dir -r requirements.txt --src /usr/local/src \
  && apt-get remove -y build-essential \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/* \
  && rm -rf /var/cache/apt/archives

# Install node packages
COPY package.json package-lock.json ./
RUN npm install \
  && npm install -g coffee-script@^1.12.6 \
  && npm cache clean --force

# Copy project
COPY . .

# Entrypoint
ENTRYPOINT ["./docker-entrypoint.sh"]
