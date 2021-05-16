import os

import yaml

from config import BASE_PATH


def read_yaml(filename):
    # 定义一个空列表
    arr = []
    # 组合路径
    """os.sep 为了实现WINDOWS MAC等不同平台的路径下划线动态匹配"""
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    # 打开文件流
    with open(file_path, "r", encoding="utf-8") as f:
        # 使用yaml.safe_load().value()进行读取数据（如果没记错，json也可以）
        for datas in yaml.safe_load(f).values():
            # 强转
            """
                注意：
                1.data.values() 取出yaml中值的值
                2.强转 把列表嵌套字典型转换为列表嵌套元组型
            """
            arr.append(tuple(datas.values()))
    return arr

# if __name__ == '__main__':
#     print(read_yaml("mp_login.yaml"))
