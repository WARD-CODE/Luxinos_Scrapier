# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy 'app.py' into the container at /app
COPY lux_bookscraper/app.py /app

# Copy the rest of the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Define environment variable
ENV NAME World
EXPOSE 8080

# Run your Scrapy spider and then the Flask app when the container launches
CMD ["sh", "-c", "scrapy crawl lux_bookspider & python /app/app.py"]
