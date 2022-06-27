import file_working


def convert_to_f2(path_from, path_to):
    data = file_working.readlines_file(path_from)
    for i in range(len(data) - 1):
        data[i] = data[i][:-1]
    while "***" in data:
        data.remove('***')
    converted_data = []
    temp = ''
    count = 0
    for i in data:
        temp += str(i) + ', '
        count += 1
        if count == 4:
            converted_data.append(temp[:-2])
            temp = ''
            count = 0
    for i in converted_data:
        file_working.write_file(path_to, i)
        file_working.write_file(path_to, "\n")


def convert_to_f1(path_from, path_to):
    data = file_working.readlines_file(path_from)
    list_of_data = []
    for i in range(len(data)):
        list_of_data.append(str(data[i]).split(', '))
    for i in range(len(list_of_data)):
        for j in range(len(list_of_data[i])):
            if '\n' not in list_of_data[i][j]:
                list_of_data[i][j] = str(list_of_data[i][j]) + '\n'
        list_of_data[i].append('***')
    for i in range(len(list_of_data)):
        for j in range(len(list_of_data[i])):
            file_working.write_file(path_to, list_of_data[i][j])
        file_working.write_file(path_to, '\n')


