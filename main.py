import datetime
import shutil
import time

import schedule


def imprime_hora():
    print("test", datetime.datetime.now())


if __name__ == "__main__":
    schedule.every(1).minutes.do(imprime_hora())

    while True:
        schedule.run_pending()
        time.sleep(1)
