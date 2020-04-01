import numpy as np, json, csv

# Loading in the file into a dictionary with the json library
def open_file():
    with open('train.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


if __name__ == "__main__":
    data = open_file()
    print(data[2][0])
