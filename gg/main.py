import os


class GG:
    def __init__(self):
        self.root_dir = "C000010"
        self.stop_words_file = "stoplist_utf8.txt"
        self.dictionary_file = "dictionary.txt"
        self.stop_set = set()
        self.dictionary = set()
        self.load_split_dictionary()
        self.load_stop_words()
        self.index = {}

    # 递归地获取目录下所有的文件名
    def get_file_names(self):
        names = []
        # os.listdir可枚举出指定目录下所有的文件（包括文件夹），返回文件的名字
        for filename in os.listdir(self.root_dir):
            # os.path.join将目录与文件名相结合得到绝对路径
            path = os.path.join(self.root_dir, filename)
            # 如果是文件夹
            if os.path.isdir(path):
                # 递归遍历
                names.extend(self.get_file_names(path))
            else:
                names.append(path)
        return names

    # 获取所有停用词表
    def load_stop_words(self):
        file = open(self.stop_words_file, 'r', encoding="UTF-8")
        file_words = file.readlines()
        for w in file_words:
            self.stop_set.add(w.replace("\n", ""))

    # 获取文件内容
    @staticmethod
    def get_file(file_name):
        file = open(file_name, 'r', encoding="UTF-8")
        string = file.read()
        return string

    # 加载分词字典
    def load_split_dictionary(self):
        file = open(self.dictionary_file, "r", encoding="UTF-8")
        string = file.read()
        word = string.split("\n")
        for w in word:
            # if w and w != " " and w != "\n":
            self.dictionary.add(w)

    # 逆向最大匹配算法
    def bmm_seg(self, sentence):
        max_len = 5  # 最长词的长度
        result = []
        end = len(sentence)
        while end > 0:
            start = max(end - max_len, 0)
            while start < len(sentence):
                candidate = sentence[start:end]
                # print("候选：", candidate)
                if candidate in self.dictionary or end == start + 1:
                    # print("找到一个词：", sentence[start: end])
                    result.append(candidate)
                    end = start
                    break
                else:
                    start += 1
        result.reverse()
        return result

    # 去停用词 和 空白字符
    def delete_stop_word(self, list):
        for l in list:
            if l in self.stop_set:
                # print(l+"是停用词")
                list.remove(l)
            if l == "\u3000" or l == " " or l == "\n":
                list.remove(l)
        return list

    # 建立倒排索引
    def build_index(self):
        for file in self.get_file_names():
            string = open(file, "r", encoding="UTF-8").read()
            temp = self.bmm_seg(string)
            temp = self.delete_stop_word(temp)
            for t in temp:
                value = self.index.get(t)
                if value is None:
                    self.index[t] = set()
                    value = self.index.get(t)
                value.add(file)

if __name__ == "__main__":
    g = GG()
    g.build_index()
    for t in g.index:
        print(t+" "+str(g.index.get(t)))
