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

    def handle_request(durations: int, cpus: int):
        with Pool(cpus) as p:
            p.map(handle_one_cpu, range(0, cpus))


    app = Flask(__name__)


    @app.route('/slow_time')
    def hello_world():
        ts = time.time()
        duration = int(os.environ.get('SLOW_TIME_DURATION', 1))
        cpus = int(os.environ.get('SLOW_TIME_CPU', 2))
        print(f"Handling request, duration={duration}, cpus={cpus}")
        handle_request(duration, cpus)
        return {
            "gmt-time": datetime.datetime.now().isoformat(),
            "duration": time.time() - ts
        }

else:
    print("Usage: SLOW_TIME_DURATION=<int> SLOW_TIME_CPU=<int> gunicorn -w <workers> -b 0.0.0.0:<port> slow_time:app")
