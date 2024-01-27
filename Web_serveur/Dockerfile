FROM python:3.8

WORKDIR /app

# Create a virtual environment
RUN python -m venv venv

# Set the virtual environment as the active environment
ENV PATH="/app/venv/bin:$PATH"

# Update pip to the latest version
RUN pip install --no-cache-dir --upgrade pip


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#RUN pip install --upgrade pip
COPY . /app

CMD ["python", "app.py"]