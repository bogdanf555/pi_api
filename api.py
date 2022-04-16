from fastapi import FastAPI

from pi_api import system_information as sys_info

api = FastAPI()


@api.get("/")
def read_root() -> str:
    return "Hello World!"


@api.get("/sys_info/disk")
def read_disk_info() -> str:
    return sys_info.get_disk_info()
