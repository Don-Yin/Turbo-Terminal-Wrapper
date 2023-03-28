from src.utils.login import login
import openai
from src.utils.general import c_paste
import sys
import json
from pathlib import Path


# print(openai.Engine.list())
# [{"role": "user", "content": "write a poem that is 10 words long!"}]

path_data = Path(__file__).parent.parent.parent / "data"


class Hook:
    def __init__(self, chat_name: str = "default"):
        self.chat_name = chat_name
        self.chat_path = path_data / (chat_name + ".json")
        self.init_chat_history()

    def init_chat_history(self):
        if not self.chat_path.exists():
            with open(self.chat_path, "w") as write_file:
                json.dump([], write_file)

        with open(self.chat_path, "r") as read_file:
            self.chat_history = json.load(read_file)

    def dump(self):
        with open(self.chat_path, "w") as write_file:
            json.dump(self.chat_history, write_file)

    def add_user_message(self, message):
        self.chat_history.append({"role": "user", "content": message})

    def add_bot_response(self, message):
        self.chat_history.append({"role": "system", "content": message})


def chatbot(message, chat_name: str = "default"):
    hook = Hook(chat_name)
    hook.add_user_message(message)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # The name of the OpenAI chatbot model to use
        messages=hook.chat_history,  # The chat history to use as context
        max_tokens=3800,  # The maximum number of tokens (words or subwords) in the generated response
        stop=None,  # The stopping sequence for the generated response, if any (not used here)
        temperature=0.7,  # The "creativity" of the generated response (higher temperature = more creative)
        stream=True,  # Whether to stream the response as it is generated
    )

    cache = ""
    # Print the response with the streaming effect
    for character in response:
        delta = character.choices[0].delta
        if "content" in delta:
            cache += delta.content
            sys.stdout.write(c_paste(delta.content, "green"))
            sys.stdout.flush()
        else:
            sys.stdout.write("\n")
            sys.stdout.flush()

    hook.add_bot_response(cache)
    hook.dump()


if __name__ == "__main__":
    pass
