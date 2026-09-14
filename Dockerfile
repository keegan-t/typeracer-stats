FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    MPLCONFIGDIR=/app/.matplotlib

RUN useradd --uid 1000 --create-home bot

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY fonts/ /usr/share/fonts/truetype/custom/
COPY changelog.txt .
COPY src/ src/

# Builds the font cache now so Exo 2 is found on first run
RUN python -c "import matplotlib.font_manager" \
    && chown -R bot:bot /app

USER bot
WORKDIR /app/src

EXPOSE 8888

CMD ["python", "main.py"]
