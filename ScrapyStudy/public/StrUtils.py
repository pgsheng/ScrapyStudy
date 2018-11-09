"""
 @Author  : pgsheng
 @Time    : 2018/9/7 17:31
"""
import re


class StrUtils(object):
    """字符串相关的操作工具类"""

    def get_num(self, text):  # 获取字符串中的数字
        num_list = re.findall('\d+\.?\d*', text)
        return num_list

    def has_letter(self, text):  # 判断字符串中是否含有字母
        return bool(re.search('[a-z,A-Z]', text))

    def has_china(self, text):  # 判断字符串中是否含有中文
        return bool(re.search('[\u4e00-\u9fa5]+', text))


if __name__ == '__main__':
    print(StrUtils().get_num("sdf中国kj10dfjds20"))
    print(StrUtils().has_letter("A"))
    print(StrUtils().has_china("sdf國kj10dfjds20"))
