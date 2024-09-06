# Use the official Python 3.12 image as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /

# Copy the requirements.txt file to the working directory
COPY ./requirements.txt ./

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application code to the working directory
COPY ./ ./

# Start the Uvicorn server
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80", "--reload"]