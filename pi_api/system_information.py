import re
import subprocess
from typing import List, Dict

# *COMMANDS
DISK_INFO_COMMAND = ["df", "-h"]
LIST_CPU_INFO_COMMAND = ["lscpu"]
FREE_COMMAND = ["free", "-thw"]
MEM_DISTRIBUTION_COMMAND = [
    "vcgencmd",
    "get_mem",
]

CPU = ["arm"]
GPU = ["gpu"]


# *INFORMATION
DISK_INFO_HEADLINES = [
    "filesystem",
    "size",
    "used",
    "available",
    "usage",
    "mounted on",
]

MEM_ALLOCATION_HEADLINES = ["cpu_allocated", "gpu_allocated"]

MEM_INFO_HEADLINES = ["total", "used", "free", "shared"]

SWAP_INFO_HEADLINES = ["swap_total", "swap_used", "swap_free"]


def get_command_output(command: List[str]) -> str:
    output = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout, _ = output.communicate()

    return re.sub("[ \t]+", " ", stdout.decode())


def get_disk_info() -> Dict[str, str]:

    info = get_command_output(DISK_INFO_COMMAND)
    info_line = info.split("\n")[1]
    info_list = info_line.split(" ")

    info = {key: value for key, value in zip(DISK_INFO_HEADLINES, info_list)}

    return info


def get_cpu_info() -> Dict[str, str]:
    # TODO: parse lscpu and cat /proc/cpuinfo
    # TODO: parse vcgencmd measure_temp
    print(get_command_output(LIST_CPU_INFO_COMMAND))
    return None


def get_mem_info() -> Dict[str, str]:
    # TODO: parse free
    # TODO: parse vcgencmd get_mem arm && vcgencmd get_mem gpu

    print(get_command_output(MEM_DISTRIBUTION_COMMAND + CPU))
    print(get_command_output(MEM_DISTRIBUTION_COMMAND + GPU))
    print(get_command_output(FREE_COMMAND))

    return None


def get_hostname_and_ip() -> Dict[str, str]:
    # TODO: parse hostname and hostname -I
    return None


def get_uptime_and_processes() -> Dict[str, str]:
    # TODO: parse uptime
    # * uptime -p (pretty) uptime -s (running since)
    # * ps x | wc -l (minus 1 for title)
    return None
