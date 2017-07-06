import os


def get_file(file_name):
    """
    获取文件内容
    :param file_name: 文件名
    :return: 文件内容
    """
    file = open(file_name, 'r', encoding="UTF-8")
    string = file.read()
    return string


def get_file_names(root_dir):
    """
    递归遍历某文件夹下所有文件
    :param root_dir: 根文件夹
    :return:文件名集合
    """
    names = []
    # os.listdir可枚举出指定目录下所有的文件（包括文件夹），返回文件的名字
    for filename in os.listdir(root_dir):
        # os.path.join将目录与文件名相结合得到绝对路径
        path = os.path.join(root_dir, filename)
        # 如果是文件夹
        if os.path.isdir(path):
            # 递归遍历
            names.extend(get_file_names(path))
        else:
            names.append(path)
    return names
