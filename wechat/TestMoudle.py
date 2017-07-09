
def log(fn):
    def gg(a):
        a()
        print(fn)
    return gg


@log("SSSSS")
def ggg():
    print("sdasda")
