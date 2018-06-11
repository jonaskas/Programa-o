"""
csv
"""

import os
import csv
import random
from pathlib import Path


def write_CSV(filepath, data, delim = ";"):
    with open(filepath, "w", newline='') as file:
        writer = csv.writer(file, delimiter=delim)
        for line in data:
            writer.writerow(line)

def write_CSV_DICT(filepath, data, headers, delim = ";"):
    with open(filepath, "w", newline='') as file:
        writer = csv.DictWriter(file, delimiter=delim, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def read_CSV(filepath, delim = ";") :
    with open(filepath, "r") as file:
        data = csv.reader(file, delimiter=delim)
        for row in data:
            print("\t".join(row))

if __name__ == "__main__":

    filePath = "_temp/data.csv"

    Students = [
        ["student 1", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
        ["student 2", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
        ["student 3", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)],
        ["student 4", random.randint(0, 20), random.randint(0, 20), random.randint(0, 20)]
    ]

    write_CSV(filePath, Students)
    read_CSV(filePath)

    print('-' * 50)
    print('-' * 50)

    # Creates dict
    header = ["Name", "Grade 1", "Grade 2", "Grade 3"]
    newStudents = [dict(zip(header, row)) for row in Students]
    print( "\n".join([str(row) for row in newStudents]))

    print()
    write_CSV_DICT(filePath, newStudents, header)
    read_CSV(filePath)
    