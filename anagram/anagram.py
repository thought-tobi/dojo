def main():
    data = read_file('wordlist.txt')
    print(data)


def read_file(file) -> list:
    with open(file, encoding="ISO-8859-1") as file:
        data = file.read().split('\n')
        return data


def is_anagram(x: str, y: str) -> bool:
    if len(x) != len(y):
        return False
    else:
        return sorted(x) == sorted(y)


if __name__ == '__main__':
    main()
