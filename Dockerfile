# Step 1: Use an official Python runtime as the base image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current directory contents into the container at /app
COPY . /app

# Step 4: Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port the app will run on
EXPOSE 8000

# Step 6: Define the environment variable for production (optional)
ENV FLASK_ENV=production

# Step 7: Run gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "wsgi:app"]
