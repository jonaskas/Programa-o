import os
import csv
from pathlib import Path

def write_CSV_DICT(filepath, lista_jogador, headers, delim = ";"):
    with open(filepath, "w", newline='') as file:
        writer = csv.DictWriter(file, delimiter=delim, fieldnames=headers)
        writer.writeheader()
        for row in lista_jogador:
            writer.writerow(row)

def readlista_CSV(filepath, lista_jogador, delim = ";") :
    with open(filepath, "r") as file:
        lista_jogador = csv.reader(file, delimiter=delim)
        for row in lista_jogador:
            lista_jogador.append(row)

def read_CSV(filepath, delim = ";") :
    with open(filepath, "r") as file:
        lista_jogador = csv.reader(file, delimiter=delim)
        for row in lista_jogador:
            print("\t".join(row))