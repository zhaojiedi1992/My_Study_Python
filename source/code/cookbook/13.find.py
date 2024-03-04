
import os 
def find_file_name(start_path, file_name):
     for relpath, dirs, files in os.walk(start_path):
        if file_name in files:
            full_path = os.path.join(start_path, relpath, file_name)
            return os.path.normpath(os.path.abspath(full_path))


if __name__ == '__main__':
    print('='*10)
    print(find_file_name(r'.', os.path.basename(__file__)))
    print('='*10)