# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
 @Author  : pgsheng
 @Time    : 2018/4/7 15:22
"""

import os

import sys


def get_project_path():
    if getattr(sys, 'frozen', None):  # 解决打包文件路径问题
        return './'  # 相对路径 ， os.path.dirname(sys.executable)获取是运行程序的目录
    else:
        return os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.path.pardir, os.path.pardir))  # 绝对路径


def get_results_path():
    if getattr(sys, 'frozen', None):  # 解决打包文件路径问题
        is_exists = os.path.exists('./results')
        if not is_exists:
            os.makedirs('./results')
        return './results/'  # 相对路径
    else:
        results_path = get_project_path() + '/results'
        is_exists = os.path.exists(results_path)
        if not is_exists:
            os.makedirs(results_path)
        return results_path + '/'  # 绝对路径


def get_images_path():
    if getattr(sys, 'frozen', None):  # 解决打包文件路径问题
        is_exists = os.path.exists('./images')
        if not is_exists:
            os.makedirs('./images')
        return './images/'  # 相对路径
    else:
        images_path = get_project_path() + '/images'
        is_exists = os.path.exists(images_path)
        if not is_exists:
            os.makedirs(images_path)
        return images_path + '/'  # 绝对路径


def get_datas_path():
    if getattr(sys, 'frozen', None):  # 解决打包文件路径问题
        is_exists = os.path.exists('./datas')
        if not is_exists:
            os.makedirs('./datas')
        return './datas/'  # 相对路径
    else:
        datas_path = get_project_path() + '/datas'
        is_exists = os.path.exists(datas_path)
        if not is_exists:
            os.makedirs(datas_path)
        return datas_path + '/'  # 绝对路径


def get_log_path():
    if getattr(sys, 'frozen', None):  # 解决打包文件路径问题
        is_exists = os.path.exists('./log')
        if not is_exists:
            os.makedirs('./log')
        return './log/'
    else:
        log_path = get_project_path() + '/log'
        is_exists = os.path.exists(log_path)
        if not is_exists:
            os.makedirs(log_path)
        return log_path + '/'


def get_word_datas_path():
    if getattr(sys, 'frozen', None):  # 解决打包文件路径问题
        is_exists = os.path.exists('./word_datas')
        if not is_exists:
            os.makedirs('./word_datas')
        return './word_datas/'
    else:
        word_datas_path = get_project_path() + '/word_datas'
        is_exists = os.path.exists(word_datas_path)
        if not is_exists:
            os.makedirs(word_datas_path)
        return word_datas_path + '/'


if __name__ == '__main__':
    print(get_project_path())
