#lamdata/my_mod.py

def enlarge(n):
    return n * 100


def main():
    print("junk")
    print('global_scope')

    y = float(input('please input a number to enlarge:'))
    print(enlarge(y))

if __name__ == "__main__":
    main()