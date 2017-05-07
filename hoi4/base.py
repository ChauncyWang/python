class Base(object):
    def __str__(self):
        re = "{ "
        for key, value in self.__dict__.items():
            re = re + key + " = " + str(value) + " "
        re += "}"
        return re
