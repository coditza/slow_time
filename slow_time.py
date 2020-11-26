import datetime
import os
import time
from multiprocessing import Pool

from flask import Flask


if __name__ != "__main__":

    def handle_one_cpu(duration: int) -> None:
        ts = time.time()
        while True:
            if time.time() - ts > duration:
                break
            foo = duration * duration

    def handle_request(durations: int, concurent: int):
        with Pool(concurent) as p:
            p.map(handle_one_cpu, range(0, concurent))


    app = Flask(__name__)


    @app.route('/slow_time')
    def hello_world():
        ts = time.time()
        iterations = int(os.environ.get('SLOW_TIME_ITERATIONS', 1))
        concurent = int(os.environ.get('SLOW_TIME_CONCURENT', 2))
        print(f"Handling request, iterations={iterations}, concurent={concurent}")
        handle_request(iterations, concurent)
        return {
            "gmt-time": datetime.datetime.now().isoformat(),
            "duration": time.time() - ts
        }

else:
    print("Usage: SLOW_TIME_ITERATIONS=<int> SLOW_TIME_CONCURENT=<int> gunicorn -w <workers> -b 0.0.0.0:<port> slow_time:app")
