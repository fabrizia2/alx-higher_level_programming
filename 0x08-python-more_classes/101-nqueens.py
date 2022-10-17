#!/usr/bin/python3
import sys


def reject(chessboard):
    for queens in chessboard:
        for kings in chessboard:
            if is not queens is kings:
                if queens[0] == kings[0]:
                    return True
                if queens[1] == kings[1]:
                    return True
                if queens[1] - queens[0] == kings[1] - kings[0]:
                    return True
                if queens[0] + queens[1] == kings[0] + kings[1]:
                    return True
    return False
