from pathlib import Path

import openai
import os


path_key = Path(__file__).parent.parent.parent / "private" / "api.key"


def login():
    with open(path_key, "r") as read_file:
        openai.api_key = read_file.read()
