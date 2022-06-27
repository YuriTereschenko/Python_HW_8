def readlines_file(path):
    with open(path, 'r') as txt:
        file_data = txt.readlines()
    return file_data


def write_file(path, data_to_write):
    with open(path, 'a') as txt:
        txt.writelines(data_to_write)


