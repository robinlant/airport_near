import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key_for_testing_only'
    AIRPORTS_FILE_PATH = os.environ.get('AIRPORTS_FILE') or os.path.join(basedir, 'app', 'static', 'data', 'large_medium_airports.csv')