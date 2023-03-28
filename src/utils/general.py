def c_print(text, color):
    if color == "red":
        print(f"\033[31m{text}\033[0m")
    elif color == "green":
        print(f"\033[32m{text}\033[0m")
    elif color == "yellow":
        print(f"\033[33m{text}\033[0m")
    elif color == "blue":
        print(f"\033[34m{text}\033[0m")
    elif color == "magenta":
        print(f"\033[35m{text}\033[0m")
    elif color == "cyan":
        print(f"\033[36m{text}\033[0m")
    elif color == "white":
        print(f"\033[37m{text}\033[0m")


def c_paste(text, color):
    if color == "red":
        return f"\033[31m{text}\033[0m"
    elif color == "green":
        return f"\033[32m{text}\033[0m"
    elif color == "yellow":
        return f"\033[33m{text}\033[0m"
    elif color == "blue":
        return f"\033[34m{text}\033[0m"
    elif color == "magenta":
        return f"\033[35m{text}\033[0m"
    elif color == "cyan":
        return f"\033[36m{text}\033[0m"
    elif color == "white":
        return f"\033[37m{text}\033[0m"
