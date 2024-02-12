import time
import sys


def progress_bar(iteration, total, prefix="Progress:", length=20, fill="█"):
    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + "-" * (length - filled_length)

    # Handling the case when iteration reaches total
    if iteration == total:
        loading_bar = f"\r{prefix} |{bar}| {percent}% Complete\n"
    else:
        loading_bar = f"\r{prefix} |{bar}| {percent}% Complete "

    sys.stdout.write(loading_bar)
    sys.stdout.flush()


def section_messages(messages):
    print("\n-----------------------------------------------------------------------")
    for message in messages:
        print(message)
    print("-----------------------------------------------------------------------")
