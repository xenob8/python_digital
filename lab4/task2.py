# TODO решите задачу
import json

INPUT_FILE_NAME = "input.json"
def task() -> float:
    with open(INPUT_FILE_NAME) as input_f:
        data = json.load(input_f)
        return round(sum(dict_el["score"]*dict_el["weight"] for dict_el in data),3)

print(task())
