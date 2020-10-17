import os
import subprocess
from shlex import quote


def send(phone, message):
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        relative_path = 'sendMessage.js'
        path = f'{dir_path}/{relative_path}'
        cmd = f'osascript -l JavaScript {path} {quote(phone)} {quote(message)}'
        subprocess.call(cmd, shell=True)
    except Exception as e:
        return f"Error: {e}"


def sendFileWords(phone, message):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    relative_path = 'sendMessage.js'
    path = f'{dir_path}/{relative_path}'

    with open('input.txt', 'r') as r:
        for line in r:
            for word in line:
                cmd = f'osascript -l JavaScript {path} {quote(phone)} {quote(word)}'
                subprocess.call(cmd, shell=True)
    return 'bruh'


def sendFileLines(phone, message):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    relative_path = 'sendMessage.js'
    path = f'{dir_path}/{relative_path}'

    with open('input.txt', 'r') as r:
        for line in r:
            cmd = f'osascript -l JavaScript {path} {quote(phone)} {quote(line)}'
            subprocess.call(cmd, shell=True)
    return 'bruh'
