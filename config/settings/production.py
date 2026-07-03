from .base import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    cast=lambda value: [host.strip() for host in value.split(",")],
)