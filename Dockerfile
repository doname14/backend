FROM python:3.11.7

# Create non-root user
RUN useradd -m -u 1000 appuser

WORKDIR /app

# RUN pip install django-oauth-toolkit


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --upgrade channels

# Change ownership of the app directory
RUN chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

EXPOSE 8000

# Comment out or remove this line since docker-compose.yml provides the command
# CMD ["daphne", "-b", "0.0.0.0:8000", "backend.asgi:application"]