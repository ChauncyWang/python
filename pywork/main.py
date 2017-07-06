from pywork import core


def bl():
    a = input("请输入要查询的词组A:")
    b = input("请输入要查询的词组B:")

    A = set(core.index.get(a))
    B = set(core.index.get(b))

    print("同时包含【%s和%s】的文章在:" % (a, b))
    show(A & B)
    print("包含【%s或%s】的文章在:" % (a, b))
    show(A | B)
    print("包含【%s】不包含【%s】的文章在:" % (a, b), )
    show(A - B)
    print("包含【%s】不包含【%s】的文章在:" % (b, a), )
    show(B - A)


def show(file_set):
    for f in file_set:
        print("---%s---" % f)
        a = open(f, 'r').read()
        print(a)


# print(core.index['手机'])

