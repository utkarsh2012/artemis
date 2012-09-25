# -*- coding: utf-8 -*-

from celery import Celery
import logging
import requests
from utils import IsNotNull
import settings

celery = Celery('tasks', broker=settings.BROKER_URL)

@celery.task
def perform_collection(list_of_nodes, url_pattern):
        logging.debug(" ---------> Worker starting to process: %d nodes" %len(list_of_nodes))
        for node in list_of_nodes:
            try:
                url = _construct_url(node, url_pattern)
                metric = _get_metrics(url)

                if metric:
                    _write_to_db(metric)
            except IOError:
                logging.error("  ---------> Invalid input: " + url)
            except requests.ConnectionError:
                logging.error("  ---------> Error while fetching data for: " + url)


def _construct_url(node, url_pattern):
    if IsNotNull(node) and IsNotNull(url_pattern):
        url = ''.join(["http://", node, "/", url_pattern])
        return url
    else:
        raise IOError("Node or url_pattern not passed!")


def _get_metrics(url):
    logging.debug("  ---------> Fetching: " + url)
    data = requests.get(url).text
    return data


def _write_to_db(x):
    try:
        f = open("fetched_data.txt", "w")
        f.write(str(x))
    finally:
        f.close()

