#!/usr/bin/env python3


import numpy as np
import tempfile


def equally_divide_width(fin, sep_num, init=0.0):
    width = fin - init
    one_width = width / sep_num
    ini_step = init + one_width/2.0
    return np.arange(ini_step,
                     fin,
                     one_width)


def convert_ar_to_writeli(ars, encode=True):
    if ars.ndim == 1:
        write_li = [repr(num) + "\n" for num in ars]
    elif ars.ndim == 2:
        tmp_fob = tempfile.TemporaryFile(mode="w+b")
        np.savetxt(tmp_fob, ars)
        tmp_fob.seek(0)
        write_li = tmp_fob.readlines()
        tmp_fob.close()
        if encode:
            write_li = [line.decode("utf-8")
                        for line in write_li]
    else:
        raise TypeError("ars.ndim must be 2 or less.")
    return write_li


class IdsEliminator(object):
    def __init__(self, tot_ids_ar):
        self.tot_ids_ar = np.array(
                             tot_ids_ar).astype(np.int64)

    def __call__(self, cand_ids):
        if cand_ids.dtypoe == np.int64:
            raise TypeError("cand_ids's type must be np.int64.")
        cond_ar = np.in1d(cand_ids, self.tot_ids_ar)
        selected_ids = cand_ids[cond_ar]
        return selected_ids, cond_ar
