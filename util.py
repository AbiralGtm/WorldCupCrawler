import json
import os


def read_file(file_path):
    if os.path.exists(file_path):
        with open(file_path) as f:
            return f.read()
    else:
        return None


class Util:
    def __init__(self, file_path):
        self.file_path = file_path

    def get_json(self):
        text = read_file(self.file_path)
        teams = json.loads(text)
        return teams

