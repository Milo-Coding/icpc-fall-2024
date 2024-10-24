# to test in bash/mac terminal use command: cat test.txt | python3 FasterStarterCode.py

if __name__ == '__main__':
    from sys import stdin
    print([line.strip().split(" ") for line in stdin])
    exit()