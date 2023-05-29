FROM python:3.10

RUN apt-get update && apt-get install -y cron


# Copy your script and other files
COPY . /app/.

# Install the requirements
RUN pip3 install -r /app/requirements.txt

# Add the cron job
RUN crontab /app/cron-test.txt

#COPY cron-test.txt /etc/cron.d/cron-test.txt
#RUN chmod 0644 /etc/cron.d/cron-test.txt && crontab /etc/cron.d/cron-test.txt

# Start the cron service and run the script
#CMD which python3
CMD cron && python3 /app/main.py

#ENTRYPOINT ["bash", "-c", "service cron start && /app"]