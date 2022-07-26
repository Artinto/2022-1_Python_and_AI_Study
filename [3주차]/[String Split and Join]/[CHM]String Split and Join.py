def split_and_join(line):
    # write your code here
    split_text=line.split()
    join_text="-".join(split_text)
    return join_text

if __name__ == '__main__':
    line = input()
