import time


def main_method():
    try:
        while True:
            print("Running")
    except KeyboardInterrupt:
        print("Interrupted waiting 5 seconds ...")
        time.sleep(3.0)
        print("Going back")
        main_method()


main_method()


