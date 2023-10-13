# TODO импортировать необходимые молули
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_f:
        first_line = input_f.readline().strip()
        columns = first_line.split(sep=",")
        list_of_dicts = []
        for line in input_f:
            values = line.strip().split(sep=",")
            list_of_dicts.append(dict(zip(columns, values)))

        with open(OUTPUT_FILENAME, "w") as write_file:
            json.dump(list_of_dicts, write_file, indent=4)

    ...  # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")