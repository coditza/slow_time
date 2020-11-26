from setuptools import setup

setup(
    name='slow-time',
    install_requires=['Flask', 'gunicorn'],
    py_modules='slow_time'
)

