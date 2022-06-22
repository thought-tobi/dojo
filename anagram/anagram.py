def main():
    pass


def is_anagram(x: str, y:str) -> bool:
    if len(x) != len(y):
        return False
    else:
     if sorted(x) == sorted(y):
         return True
     else:
         return False


if __name__ == '__main__':
    main()
