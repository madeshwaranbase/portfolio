from configparser import ConfigParser
from pathlib import Path


CONFIG_FILE = Path(__file__).resolve().parents[1] / "config" / "config.ini"


def get_config():
    config = ConfigParser()
    config.read(CONFIG_FILE)
    return config
