FROM python:3.11-slim

# Mencegah Python membuat file .pyc dan memastikan output langsung tampil di log
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode proyek
COPY . /app/

# Salin dan siapkan script entrypoint
COPY entrypoint.sh /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["sh", "/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
