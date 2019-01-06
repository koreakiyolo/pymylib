#!/usr/bin/env python3


import tempfile


def to_tmpfio_from_lines_li(byte_lines, seek0=True):
    tmp_fio = tempfile.TemporaryFile(mode="w+b")
    tmp_fio.writelines(byte_lines)
    if seek0:
        tmp_fio.seek(0)
    return tmp_fio


def gene_bytelines_from_strlines(strlines):
    for sline in strlines:
        yield sline.encode("utf-8")


def gene_line_with_ncode(strlines):
    for line in strlines:
        yield line + "\n"


def gene_line_striped(line_iter):
    for line in line_iter:
        new_line = line.strip()
        yield new_line
