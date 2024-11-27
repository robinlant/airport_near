from flask import Flask
from config import Config
import logging

logging.basicConfig(level=logging.DEBUG, format = "%(asctime)s - %(levelname)s - %(message)s")
logging.debug("Starting the app")

app = Flask(__name__)
app.config.from_object(Config)

# import at the bottom to avoid import loops as routes module imports app at the top of the file
from app import routes  # noqa: E402, F401