import datetime
import os
import shutil
import time

import schedule

import imprime


def imprime_hora():
    print("test", datetime.datetime.now())


if __name__ == "__main__":
    schedule.every(1).day.do(imprime.prueba)

    while True:
        schedule.run_pending()
        time.sleep(1)
