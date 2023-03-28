from pathlib import Path
import os

path_data = Path(__file__).parent / "data"

for i in os.listdir(path_data):
    os.remove(path_data / i)
