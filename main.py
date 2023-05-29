import datetime
import os
import shutil
import time

import schedule

import imprime


def imprime_hora():
    print("test", datetime.datetime.now())


if __name__ == "__main__":
    print("hola 1")
    schedule.every(5).seconds.do(imprime.prueba)

    while True:
        a = os.environ["MONGO_CONN"]
        print(type(a), a)
        schedule.run_pending()
        time.sleep(1)
