FROM python:3.10

RUN apt-get update && apt-get install -y cron


# Copy your script and other files
COPY . /app/.

# Install the requirements
RUN pip3 install -r /app/requirements.txt

# Add the cron job
RUN chmod 777 /app/crontab && crontab /app/crontab

# COPY crontab /etc/cron.d/crontab
# RUN chmod 0644 /etc/cron.d/crontab && crontab /etc/cron.d/crontab
# Connect to internet
docker run --net=host -it ubuntu

# Start the cron service and run the script

# CMD service cron start  &&
CMD ip -a &&  python3 /app/main.py && service cron start

#ENTRYPOINT ["bash", "-c", "service cron start && /app"]