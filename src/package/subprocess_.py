import subprocess


def ls_subprocess():
    r = subprocess.run("ls", shell=True)
    # subprocess.call("ls", shell=True)
    # subprocess.check_call("ls", shell=True)
    print("Finished!")
    return r


def ls_Popen():
    r = subprocess.Popen("ls", shell=True)
    print("Finished!")
    return r


def ls_check_output():
    r = subprocess.check_output("ls", shell=True)
    print("Finished!")
    return r


if __name__ == "__main__":
    # r = ls_subprocess()
    # print(r)
    # r = ls_Popen()
    # print(r)
    r = ls_check_output()
    print(r)
