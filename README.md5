Artemis
===
A web app to fetch metrics via REST endpoints based on celery's distributed task queue.



0. ###Design consideration:
    1. [Flask][1] to run the web app
    2. [Celery][2] with [redis][3] as message broker
    	* Alternative: In place of celery, python's [multiprocessing][4] can be used for parallelism. But I chose clerey for clear separation of web app and task workers.

1. ###Installation:
    1. pip install -r requirements.txt
    2. Install redis (and keep the default config, if a different port is needed, please change the setting in settings.py)

2. ###Running the app:
    1. Flask web app: python artemis.py runserver
    2. Start redis: ./src/redis-server
    3. Start Celery: celery -A tasks worker --loglevel=debug
    4. Start accepting requests (via POST request)!
        Example: curl -d "node=localhost:5000&node=127.0.0.1:5000&url=metric" http://localhost:5000/fetch


3. ###Input explanation:

        node should be 1 or more
        node=localhost:5000
        node=127.0.0.1:5000

        url pattern should be 1 which can be applied to all the nodes
        url=metric

3. ###How does it work:
     1. POST request is received and a task will be added to celery queue and all processing is asynchronous now.
     2. artemis will construct the metrics endpoint by concatenating the 2 inputs:
     	1. http://localhost:5000/metric
     	2. http://127.0.0.1:5000/metric
     3. Celery task will get the JSON data from /metric (using requests.get)
     4. Write JSON to a flat file for now (this can be changed to be written to a DB)



[1]: http://flask.pocoo.org/
[2]: http://celeryproject.org/
[3]: http://redis.io/
[4]: http://docs.python.org/library/multiprocessing.html