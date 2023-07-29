import re


data_regexp = r"\d+/\d+/\d+"
data_pattern = re.compile(data_regexp)


def match(arg):
    res = data_pattern.match(arg)
    if res:
        print(res.string)
        print(res.pos)
        print(res.start())
        print(res.group())
    else:
        print(res)


def search(arg):
    res = data_pattern.search(arg)
    if res:
        print("position", res.start(), res.group())
    else:
        print(res)


def split(arg):
    res = re.split(data_regexp, arg)
    print(res)


def findall(arg):
    res = re.findall(data_regexp, arg)
    print(res)


if __name__ == "__main__":
    match("Today we are 01/02/2023 and soon it will be 02/02/2023")
    match("01/02/2023 is today and soon it will be 02/02/2023")
    print("-" * 80)
    search("Today we are 01/02/2023 and soon it will be 02/02/2023")
    search("01/02/2023 is today and soon it will be 02/02/2023")
    print("-" * 80)
    split("Today we are 01/02/2023 and soon it will be 02/02/2023")
    split("01/02/2023 is today and soon it will be 02/02/2023")
    print("-" * 80)
    findall("Today we are 01/02/2023 and soon it will be 02/02/2023")
    findall("01/02/2023 is today and soon it will be 02/02/2023")
