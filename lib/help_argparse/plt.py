#!/usr/bin/env python3


# formal lib
import argparse
# my lib
from .core import to_float_or_nan


COLOR_LI = ["b", "o", "r", "c", "m", "y", "k", "w"]
MARKERS_LI = ["o", "v", "^", ">", "<", "*", "h", "x", "D"]


def make_plot_parser(msg=""):
    parser = argparse.ArgumentParser(description=msg,
                                     fromfile_prefix_chars="@")
    parser.add_argument("--xminmax", nargs=2, type=to_float_or_nan,
                        default=(None, None))
    parser.add_argument("--yminmax", nargs=2, type=to_float_or_nan,
                        default=(None, None))
    return parser


def to_args_from_file(fpath, cnvt_func=str):
    kwargs = {}
    with open(fpath, "r") as read:
        for line in remove_cmtline_gene(read):
            key, va = line.split("=")
            key = key.strip()
            va = key.strip()
            kwargs[key] = cnvt_func(va)
    return kwargs


def remove_cmtline_gene(lines_iter):
    for line in lines_iter:
        tmp = line.strip()
        if tmp[0] == "#":
            continue
        else:
            yield line
