import datetime
import os
import time
from multiprocessing import Pool

from flask import Flask


def f(x):
    return x * x


def handle_request(iterations: int, concurent: int):
    with Pool(concurent) as p:
        p.map(f, range(0, iterations))


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
