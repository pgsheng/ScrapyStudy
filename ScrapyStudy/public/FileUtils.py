"""
 @Author  : pgsheng
 @Time    : 2018/8/23 17:43
"""
import os
import random
import shutil

import pythoncom
import win32com.client
import yaml

from ScrapyStudy.public.Log import Log


class FileUtils(object):
    """
    文件操作类
    """

    def __init__(self):
        self.log = Log().get_logger()

    def read_yaml(self, path):
        try:
            with open(path, 'r', encoding='utf-8') as file:
                data_dict = yaml.load(file)
                self.log.info('读取yaml文件成功')
                if isinstance(data_dict, dict):
                    return data_dict
                else:
                    return dict()
        except Exception as e:
            return dict()

    def write_yaml(self, path, data):
        try:
            # a追加写入，w覆盖写入
            with open(path, 'w', encoding='utf-8') as file:
                yaml.dump(data, file)
                self.log.info('数据写入yaml文件成功')
                return True
        except Exception as e:
            self.log.error('数据写入yaml文件出现异常：%s' % e)
            return None

    def read_txt(self, path):
        try:
            with open(path, 'r', encoding='utf-8-sig') as file:
                message_list = file.readlines()
                if len(message_list) > 0:
                    msg_list = []
                    for line in message_list:
                        line = line.strip().replace(" ", "")  # 去掉换行符和空格
                        if len(line) > 0:  # 去掉空行
                            msg_list.append(line)
                    if len(msg_list) > 0:
                        return msg_list
                return None
        except Exception as e:
            self.log.error('读取txt文件出现异常：%s' % e)
            return None

    def write_txt(self, path, text):
        try:
            # a追加写入，w覆盖写入
            with open(path, 'w', encoding='utf-8') as file:
                file.write(str(text))
                self.log.info('数据写入文件成功')
                return True
        except Exception as e:
            self.log.error('数据写入txt文件出现异常：%s' % e)
            return None

    def del_file(self, path):
        ls = os.listdir(path)
        for i in ls:
            c_path = os.path.join(path, i)
            if os.path.isdir(c_path):
                self.del_file(c_path)
            else:
                os.remove(c_path)

    def copy_file_random(self, file_dir, tar_dir, num):  # 随机复制num张图片
        sample = random.sample(os.listdir(file_dir), num)
        for name in sample:
            shutil.copyfile(file_dir + name, tar_dir + name)

    def clip_file_random(self, file_dir, tar_dir, num):  # 随机剪贴num张图片,并重复复制多张
        sample = random.sample(os.listdir(file_dir), num)
        for name in sample:
            shutil.copyfile(file_dir + name, tar_dir + name)
            os.remove(file_dir + name)
            self.copy_redo(tar_dir, name, 32)

    def copy_redo(self, file_dir, name, num):  # 同目录下重复复制多张图片
        for index in range(0, num):
            shutil.copyfile(file_dir + name, file_dir + str(index) + name)

    def copy_word(self, path):  # 复制word的所有内容到了剪切板，包括图片、文字、格式
        try:
            pythoncom.CoInitialize()
            w = win32com.client.DispatchEx('Word.Application')
            try:
                # # 后台运行，不显示，不警告
                w.Visible = 0
                w.DisplayAlerts = 0
                doc = w.Documents.Open(path)  # 打开word，经测试要是绝对路径
                doc.Content.Copy()  # 复制word的所有内容
                doc.Close()  # 关闭word
            except Exception as e:
                self.log.error('复制word文档出现异常：%s' % e)
            finally:
                if w:  # 对com操作，一定要确保退出word应用
                    self.log.info('退出word应用')
                    w.Quit()
                    del (w)
                pythoncom.CoUninitialize()
        except Exception as e:
            pass


if __name__ == '__main__':
    f = FileUtils()
