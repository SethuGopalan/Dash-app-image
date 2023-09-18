# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app

# Install necessary Python packages
COPY requirements.txt .
RUN pip install -r requirements.txt

# Expose the port your Dash app will run on
EXPOSE 8050

# Define the command to run your Dash app
CMD python ./app.py
