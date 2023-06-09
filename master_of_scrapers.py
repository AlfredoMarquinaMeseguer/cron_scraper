"""
This class is the old __init__. Deprecated.
"""
import asyncio
from asyncio import Task
from typing import Callable, Any

from classes.dao import Petition
from classes import mongo_conn
from scrapers import talent, infoempleo, wearehiring, tecno_empleo


def master_scraper():
    """
    Scraps all the data for all petitions not disabled present in the database.
    """

    petitions: list[Petition] = [Petition.from_mongo(petition) for petition in
                                 mongo_conn.connect_to_petitions().find({"disabled": False})]
    # Fire & Forgive - PowerWolf
    for petition in petitions:
        print(petition)
        # Para cada petición llamar a todos los scrapper de forma síncrona
        asyncio.run(trigger_all_scrapers(petition))


# NOTE: InfoJobs not added because it's shit
SCRAPERS: list[Callable] = [
    # talent.scrap, # Loop infinito
    # infoempleo.scrap, # Errores
    tecno_empleo.scrap,
    wearehiring.scrap
]


async def trigger_all_scrapers(petition: Petition):
    """
    Calls all available scrapers with the given parameter. These scrapers save the results in the configured
    MongoDB DB.
    :param petition: Petition object parameter to the scrapers
    """
    background_tasks: list[Task[Any]] = [asyncio.create_task(scrap(petition)) for scrap in SCRAPERS]
    await asyncio.gather(*background_tasks)


if __name__ == '__main__':
    master_scraper()
    # crontab.CronTab("0 0 * * * *", "")
