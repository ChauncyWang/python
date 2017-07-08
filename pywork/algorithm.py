import json
import os
import re
from collections import Counter

from math import log

from pywork import core
from pywork.config import *
from pywork.untils import get_file_names


class ReverseIndex:
    """
    构造倒排索引字典,最后保存为 json
    或从文件中加载 json 类型的倒排索引
    json 格式
    {
        num:文件总数
        [
            单词:{
                IDF:逆文档频率
                [
                    文件名：该文件中出现该单词的词频
                ]
            }
        ]
    }
    """

    def __init__(self):
        self.split_dictionary = set()
        self.stop_set = set()
        self.index = {}

        # 加载分词字典和停用词表
        self.load_stop_words()
        self.load_split_dictionary()
        # 建立或加载倒排索引
        if not os.path.exists(build_index_file):
            print("没有建立过倒排索引!")
            print("正在建立倒排索引...")
            self.build_index()
            print("建立倒排索引成功!")
            print("正在保存倒排索引(Json格式)...")
            with open(build_index_file, "w") as file:
                file.write(json.dumps(self.index))
            print("保存成功!")
        else:
            print("发现建立好的倒排索引!")
            print("正在加载倒排索引文件...")
            self.index = json.load(open(build_index_file, 'r'), encoding="UTF8")
            print("加载成功!")

    def build_index(self):
        """
        建立倒排索引
        :return:
        """
        # 获取所有 root_dir 文件夹下的文件
        files = get_file_names(root_dir)
        file_count = len(files)
        self.index['num'] = file_count
        # 对所有文件
        for file in files:
            string = open(file, "r", encoding="UTF-8").read()
            # 进行分词
            words = self.bmm_seg(string)
            # 计算单词在该文档中的词频 TF
            term_frequency = Counter(words)
            for word in term_frequency:
                file_list = self.index.get(word)
                # 文件列表不存在
                if file_list is None:
                    self.index[word] = {}
                    file_list = self.index.get(word)

                file_list[file] = term_frequency[word]
        # 计算逆文档频率 IDF
        for word in self.index:
            if word != 'num':
                l = self.index[word]
                idf = log(file_count / (len(l)))
                self.index[word]['IDF'] = round(idf, 5)

    def bmm_seg(self, sentence):
        """
        逆向最大匹配算法
        :param sentence: 要匹配处理的单词
        :return:分词结果
        """
        max_len = 5  # 最长词的长度
        result = []
        # 清除所有空白字符
        p = re.compile('\s+')
        sentence = re.sub(p, '', sentence)
        end = len(sentence)
        while end > 0:
            start = max(end - max_len, 0)
            while start < len(sentence):
                candidate = sentence[start:end]
                if candidate in self.split_dictionary or end == start + 1:
                    result.append(candidate)
                    end = start
                    break
                else:
                    start += 1
        result.reverse()
        # 去停用词
        result = self.delete_stop_word(result)

        return result

    def delete_stop_word(self, word_list):
        """
        去停用词 和 空白字符
        :param word_list: 分词完成的列表
        :return: 消除停用词和空白字符的分词列表
        """
        new_list = []
        for l in word_list:
            if l not in self.stop_set:
                new_list.append(l)

        return new_list

    def load_stop_words(self):
        """
        获取所有停用词表
        :return:停用词表
        """
        print("加载停用词表...")
        f = open(stop_words_file, 'r', encoding="UTF-8")
        lines = f.readlines()
        for w in lines:
            self.stop_set.add(w.replace("\n", ""))
        print("加载停用词表完成!")

    def load_split_dictionary(self):
        """
        加载分词字典
        :return: 分词字典
        """
        print("加载分词字典...")
        f = open(dictionary_file, "r", encoding="UTF-8")
        string = f.read()
        word = string.split("\n")
        for w in word:
            # if w and w != " " and w != "\n":
            self.split_dictionary.add(w)
        print("加载分词字典完成!")


def search_or(word1, word2):
    """
    检索包含 word1 或 word2 的文章
    :param word1:
    :param word2:
    :return: 文章文件名集合
    """
    r = set(core.index.get(word1)) | set(core.index.get(word2))
    if "IDF" in r:
        r.remove("IDF")
    return r


def search_and(word1, word2):
    """
    检索同时包含 word1 和 word2 的文章
    :param word1:
    :param word2:
    :return: 文章文件名集合
    """
    r = set(core.index.get(word1)) & set(core.index.get(word2))
    if "IDF" in r:
        r.remove("IDF")
    return r


def search_not(word1, word2):
    """
    检索包含 word1 不包含 word2 的文章
    :param word1:
    :param word2:
    :return: 文章文件名集合
    """
    r = set(core.index.get(word1)) - set(core.index.get(word2))
    if "IDF" in r:
        r.remove("IDF")
    return r


def word_weight(reverse, file_name):
    """
    计算某文件总分词的权重 使用 TF-IDF 方法
    :param reverse: ReverseIndex 对象
    :param file_name:
    :return:
    """
    index = reverse.index
    content = open(file_name, 'r').read()
    dictionary = reverse.bmm_seg(content)
    dictionary = Counter(dictionary)
    for word in dictionary:
        print(word, index[word][file_name]*index[word]['IDF'])
