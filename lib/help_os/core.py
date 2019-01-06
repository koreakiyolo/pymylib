#!/usr/bin/env python3


import os


def extract_basenm_in_dirnm(dir_nm):
    fnms = os.listdir(dir_nm)
    base_nm = [os.path.splitext(fnm)[0] for fnm in fnms]
    return base_nm


def gene_normal_path(paths):
    for a_path in paths:
        normed_path = os.path.normpath(a_path)
        yield normed_path


def gene_abs_path(paths):
    for a_path in paths:
        abs_path = os.path.abspath(a_path)
        yield abs_path


def gene_absnormal_path(paths):
    tmp_iter = gene_abs_path(paths)
    iter_absnormal_path = gene_normal_path(tmp_iter)
    return iter_absnormal_path


class CompareFilePath(object):
    def __init__(self, ref_paths):
        self.ref_paths_set = self._convert_normal_set_from_paths(
                                                            ref_paths)

    def _convert_normal_set_from_paths(self, paths):
        paths = list(gene_absnormal_path(paths))
        paths_set = set(paths)
        return paths_set

    def ref_minus_target_paths(self, target_paths):
        target_paths_set = self._convert_normal_set_from_paths(
                                                        target_paths)
        ref_minus_target_paths = self.ref_paths_set - target_paths_set
        ref_minus_target_paths = list(ref_minus_target_paths)
        return ref_minus_target_paths
