class init:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def add(a, b, c):
        return a + b + c


if __name__ == '__main__':
    ini = init()
    print(ini.add(12, 34, 45))
