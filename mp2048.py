from dashboard import Dashboard
from hoard import Hoard
from multiprocessing import Queue, Manager, log_to_stderr
from packing import human2bin
import csv
import logging
import sys


if __name__ == "__main__":
    logger = log_to_stderr()
    logger.setLevel(logging.INFO)
    queue = Queue()
    pre = dict()
    with open("base.csv", newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if len(row) == 2:
                pre[human2bin(row[0])] = float(row[1])
    games = 8
    h = Hoard(queue, games, 2)
    d = Dashboard(queue, games)
    if len(sys.argv) > 1:
        start = sys.argv[1]
    else:
        start = "1011::"
    h.run(start, pre, logger)
    d.run(queue)
