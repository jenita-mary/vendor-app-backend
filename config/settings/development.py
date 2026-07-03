from .base import *
from decouple import config

DEBUG = config("DEBUG", cast=bool, default=True)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda value: [host.strip() for host in value.split(",")],
    default="127.0.0.1,localhost",
)