from enum import Enum
from dotenv import load_dotenv

load_dotenv()


class Headers(Enum):
    AUTH_HEADERS = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }
    API_HEADERS = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
