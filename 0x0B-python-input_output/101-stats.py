#!/usr/bin/python3
""" Read stdin and computes metrics """
import sys


def print_metrics(fileSize, statusCodes):
    """ Print the metrics

    Args:
      fileSize (int): File size.
      statusCodes (dict): Status codes that was found.
    """
    print("File size: {}".format(fileSize))
    for key in sorted(statusCodes):
        print("{}: {}".format(key, statusCodes[key]))


def get_metrics():
    """ Get the metrics from stdin """
    lineCount = 0
    fileSize = 0
    possibleStatus = ["200", "301", "400", "401", "403", "404", "405", "500"]
    statusCodes = {}

    try:
        for line in sys.stdin:
            if lineCount == 10:
                print_metrics(fileSize, statusCodes)
                lineCount = 1
            else:
                lineCount += 1

            try:
                line = line.split()
                size = int(line[-1])
                status = line[-2]

                fileSize += size
                if status in possibleStatus:
                    if status in statusCodes:
                        statusCodes[status] += 1
                    else:
                        statusCodes[status] = 1
            except (IndexError, ValueError):
                pass

        print_metrics(fileSize, statusCodes)

    except KeyboardInterrupt:
        print_metrics(fileSize, statusCodes)


if __name__ == "__main__":
    get_metrics()
