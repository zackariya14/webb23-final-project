# Använd en officiell Python-bild som bas
FROM python:3.10

# Ställ in arbetskatalogen i containern
WORKDIR /app

# Kopiera requirements-filen och installera beroenden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera hela projektet
COPY . .

# Exponera porten som Django kör på
EXPOSE 8000

# Starta Django-applikationen
CMD ["python", "blog_project/manage.py", "runserver", "0.0.0.0:8000"]
