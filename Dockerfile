# Start from a Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Create a virtual environment path
ENV VIRTUAL_ENV=/opt/venv

# Install virtualenv and create the virtual environment
RUN python -m venv $VIRTUAL_ENV

# Make sure the virtualenv binaries are used
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install dependencies into the virtualenv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create a non-root user and switch to that user
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Ensure proper permissions for the appuser
RUN chown -R appuser:appgroup /app

# Switch to the non-root user
USER appuser

# Expose the application port
EXPOSE 8080

# Set environment variables
ENV FLASK_ENV=production

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

