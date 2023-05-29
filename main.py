import datetime
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
        print("hola 2")
        schedule.run_pending()
        time.sleep(1)
