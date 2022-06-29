def main():
    data = read_file('wordlist.txt')
    data_dict = create_dictionary(data)
    print(filter_anagrams(data_dict))


def read_file(file) -> list:
    with open(file, encoding="ISO-8859-1") as file:
        data = file.read().split('\n')
        return data


def create_dictionary(data) -> dict:
    data_dict = {}
    for i in data:
        if tuple(sorted(i)) in data_dict:
            data_dict[tuple(sorted(i))].append(i)
        else:
            data_dict[tuple(sorted(i))] = [i]
    return data_dict


def filter_anagrams(data_dict) -> dict:
    filtered_data_dict = {}
    for key, value in data_dict.items():
        if len(value) > 1:
            filtered_data_dict[key] = value
    return filtered_data_dict


if __name__ == '__main__':
    main()
