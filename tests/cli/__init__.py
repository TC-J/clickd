from clickd import clickd

@clickd(dpath="./tests/cli", ignore=[])
def cli_test():
    pass

if __name__ == "__main__":
    cli_test()