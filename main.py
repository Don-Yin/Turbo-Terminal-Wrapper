from src.utils.login import login
import openai
from src.utils.response import chatbot
import argparse

parser = argparse.ArgumentParser(description="Process some strings.")
parser.add_argument("strings", type=str, nargs="+", help="one or more string inputs")
args = parser.parse_args()
args = " ".join(args.strings)

login()

chatbot(args)
