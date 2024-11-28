import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
logging.debug("logging is enabled")

from flask import Flask  # noqa: E402
from config import Config  # noqa: E402

app = Flask(__name__)
app.config.from_object(Config)


# import at the bottom to avoid import loops as routes module imports app at the top of the file
from app import routes  # noqa: E402, F401