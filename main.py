import crontab
from crontab import CronTab


def scraper_cron_job():
    cron = CronTab()
    # job = cron.new(command='python3 cron_scraper/master_of_scrapers.py')
    job = cron.new(command='echo "hello"')

    job.minute.every(1)

    cron.write("stdout")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    scraper_cron_job()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
