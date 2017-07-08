import pywork.algorithm as A

# 建立倒排索引的类
ReverseIndex = A.ReverseIndex
# 布尔检索的三种方法
search_and = A.search_and
search_or = A.search_or
search_not = A.search_not
# 读取或加载倒排索引
reverse = ReverseIndex()
index = reverse.index


def bl():
    a = input("请输入要查询的词组A:")
    b = input("请输入要查询的词组B:")
    # a = "苹果"
    # b = "手机"

    A = set(index.get(a))
    B = set(index.get(b))

    print("同时包含【%s和%s】的文章在:" % (a, b))
    t = A & B
    t.remove("IDF")
    print(t)
    print("包含【%s或%s】的文章在:" % (a, b))
    print(A | B)
    print("包含【%s】不包含【%s】的文章在:" % (a, b), )
    print(A - B)
    print("包含【%s】不包含【%s】的文章在:" % (b, a), )
    print(B - A)


def vsm(sentence, k=5):
    """
    查看句子和文章的相关性 并 标注
    :param sentence: 句子
    :param k: 标准
    :return:
    """
    words = reverse.bmm_seg(sentence)
    files = set()
    vector = {}
    result = {}
    for word in words:
        for file in index[word]:
            if file != "IDF":
                files.add(file)

    for word in words:
        vector[word] = {}
        for file in files:
            tf = index[word].get(file)
            idf = index[word]["IDF"]
            if tf is None:
                tf = 0
            vector[word][file] = round(tf * idf, 5)

    for file in files:
        result[file] = 0
        for word in words:
            result[file] += vector[word][file]
    items = result.items()
    items = sorted(items, key=lambda x: -x[1])
    print("-"*50)
    print('与"%s"相关的前%s名:' % (sentence, k))
    print(items[0:k])
