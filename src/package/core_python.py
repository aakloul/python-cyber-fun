import sys
import os


def stdout_stderr():
    with open("/tmp/out.txt", "w") as out, open("/tmp/err.txt", "w") as err:
        # sys.stdout = out
        # sys.stderr = err
        sys.stdout.write("Hello")
        sys.stderr.write("Error 1")
        sys.stdout.write("World!")
        sys.stderr.write("Error 2")


def print_sys():
    print(sys.path[0])
    print(sys.path)
    print(sys.version)
    print(sys.version_info)


def print_os():
    print(os.getcwd())
    print(os.getpid())
    print(os.name)
    print(os.pathsep)
    print(os.sep)
    print(os.environ)
    print(sys.platform)


def system():
    os.system("ls /tmp")
    with open("/tmp/test.txt", "w") as writer:
        writer.writelines(["Thank", "You\n", "very", "much"])
    with open("/tmp/test.txt", "r") as reader:
        sys.stdout.write(reader.read())
    os.remove("/tmp/test.txt")


def walk():
    for root, dirs, files in os.walk(".", topdown=False):
        for name in files:
            print(os.path.join(root, name))
        for name in dirs:
            print(os.path.join(root, name))


if __name__ == "__main__":
    # print_sys()
    # print_os()
    # walk()
    system()
