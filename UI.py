import file_working
import converting


def start_prog(storage_path):
    while True:
        action = input('Choose an action:\n"1" to import\n"2" to export\n"3" to exit the program\n')
        if action == '1':
            path = input('What path to importing file is?\n')
            format = int(input('What type of importing file 1 or 2?\n'))
            if format == '1':
                converting.convert_to_f2(path, storage_path)
                print("Import successful")
            elif format == '2':
                imported_file = file_working.readlines_file(path)
                file_working.write_file(storage_path, imported_file)
                print("Import successful")
            else:
                print('Unsupported format')
        elif action == '2':
            path = input('What the path to export to?\n')
            format = int(input('In what format to export 1 or 2?\n'))
            if format == 1:
                converting.convert_to_f1(storage_path, path)
                print("Export successful")
            elif format == 2:
                exported_file = file_working.readlines_file(storage_path)
                file_working.write_file(path, exported_file)
                print("Export successful")
            else:
                print('Unsupported format')
        elif action == '3':
            exit(0)
        else:
            print("Unsupported action")