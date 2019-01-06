#!/usr/bin/env python3


import os
import sys
import re


def print_global_variables(variable_dict=None):
    if variable_dict is None:
        variable_dict = globals()
    mes_dict = {key: va for key, va in variable_dict.items()
                if key.isupper()}
    print("GLOBAL VARIABLES are in the following.")
    print("======================================")
    print(mes_dict)
    print("======================================")


def confirm_paths_exist(paths):
    invalid_paths = [a_path for a_path in paths
                     if not os.path.exists(a_path)]
    if len(invalid_paths) != 0:
        print(invalid_paths, file=sys.stderr)
        sys.stderr.flush()
        raise OSError("invalid paths are existing")


def dirstr(path_str):
    if not os.path.isdir(path_str):
        err_mes = "{} is not directory.".format(path_str)
        raise OSError(err_mes)
    return path_str


def fnmstr(path_str):
    if not os.path.exists(path_str):
        err_mes = "{} is not file path".format(path_str)
        raise OSError(err_mes)
    return path_str


def wio(path_str, mode="w"):
    if os.path.exists(path_str):
        mes = "overwrite {} ?:(y/n)".format(path_str)
        cond = yes_no_confirm(mes)
        if cond:
            return open(path_str, mode)
        else:
            raise TypeError("path isn't overwritten.")
    else:
        return open(path_str, mode)


def noexist_fnmstr(path_str):
    if os.path.exists(path_str):
        raise OSError("{} is already existing.")
    return path_str


def remove_invalid_paths(paths):
    valid_path = [a_path for a_path in paths
                  if os.path.exists(a_path)]
    return valid_path


def nconfirm_invalid_dirs(paths):
    invalid_paths = [a_dir for a_dir in paths
                     if not os.path.isdir(a_dir)]
    if len(invalid_paths) != 0:
        print(invalid_paths, file=sys.stderr)
        sys.stderr.flush()
        raise OSError("invalid paths are existing.")


def to_float_or_nan(string):
    if string == "None":
        return None
    else:
        return float(string)


def cnvt_dirnm_from_fapth(fpath, dir_nm):
    base = os.path.basename(fpath)
    new_path = os.path.join(dir_nm, base)
    return new_path


def yes_no_confirm(mes):
    yes_reins = re.compile("y.*|Y.*")
    no_reins = re.compile("n.*|N.*")
    cond = input(mes)
    if yes_reins.fullmatch(cond):
        return True
    elif no_reins.fullmatch(cond):
        return False
    else:
        raise TypeError("invalid input is entered.")
