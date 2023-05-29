FROM python:3.10

RUN apt-get update && apt-get install -y cron

# Copy your script and other files
COPY . /app/.

# Set up the cron job
RUN crontab /app/cronjob.txt

# Start the cron service
CMD cron && python /app/script.py