from fastapi import FastAPI

import subprocess
import re

api = FastAPI()


@api.get("/")
def read_root():
    return "Hello World!"


@api.get("/disk")
def read_disk_info():

    output = subprocess.Popen(
        ["df", "-h"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    stdout, _ = output.communicate()

    stdout = re.sub("[ ]+", " ", stdout.decode())
    info_line = stdout.split("\n")[1]
    info_list = info_line.split(" ")
    system_info_headlines = [
        "filesystem",
        "size",
        "used",
        "available",
        "usage",
        "mounted on",
    ]

    info = {key: value for key, value in zip(system_info_headlines, info_list)}

    return info
