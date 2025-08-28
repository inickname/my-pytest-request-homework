from enum import Enum
import os
from dotenv import load_dotenv

load_dotenv()


class Url(Enum):
    BASE_URL = "https://api.pomidor-stage.ru"


class Headers(Enum):
    AUTH_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    API_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }


class AuthData(Enum):
    AUTH_DATA = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD"),
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }
