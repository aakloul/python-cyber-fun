import os
import yara


directory = "."
yara_rules = yara.compile(filepath="./sample/test_rules.yara")


def mycallback(data):
    if data["matches"]:
        pass
        # print(f"[Infected]\t{filename}", data["rule"])
    else:
        pass
        # print(f"[Clean]\t{filename}")
    return yara.CALLBACK_CONTINUE


def run_yara_callback():
    for filename in os.listdir(directory):
        matches = yara_rules.match(data=filename, callback=mycallback)
        if matches:
            print(f"[Infected]\t{filename}")
        else:
            print(f"[Clean]\t{filename}")


def run_yara():
    for filename in os.listdir(directory):
        matches = yara_rules.match(data=filename)
        if matches and len(matches) > 1:
            print(
                f"[Infected] {filename}",
                [x.rule for x in matches if x.rule != "GlobalRuleExample"],
            )
            for m in matches:
                print(
                    f"\trule: '{m.rule}', "
                    + f"meta: '{m.meta}', "
                    + f"namespaces: '{m.namespace}', "
                    + f"tags: {m.tags},"
                    + f"strings: {m.strings}"
                )
        else:
            print(f"[Clean] {filename}")


def warnings_callback(warning_type, message):
    # if warning_type == yara.CALLBACK_TOO_MANY_MATCHES:
    print(
        f"warn:'{warning_type}' namespace:'{message.namespace}' "
        + f"rule:'{message.rule}' string:'{message.string}'"
    )
    return yara.CALLBACK_CONTINUE


def run_yara_warning():
    for filename in os.listdir(directory):
        matches = yara_rules.match("./hello.txt", warnings_callback=warnings_callback)
        if matches:
            print(f"[Infected]\t{filename}")
        else:
            print(f"[Clean]\t{filename}")


if __name__ == "__main__":
    run_yara()
    # run_yara_warning()
