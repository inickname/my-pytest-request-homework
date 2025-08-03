from enum import Enum


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
        "username": "mail1@gmail.com",
        "password": "Kofper-7mazdo-gaxger",
        "scope": "",
        "client_id": "",
        "client_secret": ""
    }
