import datetime
import os
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
    iterations = os.environ.get('SLOW_TIME_ITERATIONS', 1)
    concurent = os.environ.get('SLOW_TIME_CONCURENT', 2)
    handle_request(iterations, concurent)
    return {"gmt-time": datetime.datetime.now().isoformat()}
