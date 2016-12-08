import sys
import re

def encoding(filename, key_cod):
    '''Creates a new file containing the encrypted text original file

    If original file called "example.txt" then new file will be
    called "example_encoding.txt"

    "'''
    with open(filename, 'r') as f:
        file = f.read()
        
    # create list_2 which contains ASCII-code for every include symbol in text
    # and copy this in list_1 without repeating symbol's
    string = file
    MASS_2 = [ord(MASS_2) + key_cod for MASS_2 in string] 
    MASS_1 = list(set(MASS_2.copy())) 
    tab = dict.fromkeys(MASS_1)
    
    # append value's in dict
    for i in list(set(MASS_2)):
        list_index = []
        for num in range(MASS_2.count(i)):
            list_index.append(MASS_2.index(i))
            MASS_2[MASS_2.index(i)] = 'DONE'
        tab[i] = list_index

    # create new file and  write a result     
    name = filename.split('.')
    with open(name[0] + '_encoding.' + name[1], 'w') as f:
        for key in tab:
            f.write(str(key)+ ': '+ str(tab[key]) + '\n' )    

def decoding(filename, key_cod):
    '''Decrypts the file and write the result to a new file which called
    example_decoding.txt

    '''
    dict_sym = {}

    # переводит строковый текст в словарь
    with open(filename, 'r') as f:
        for line in f:
            foo = re.sub(r'[\[\]\n]', '', line)
            string = foo.split(': ')
            dict_sym.update(
                {int(string[0]) - key_cod:list(string[1].split(', '))}
                )

    counter = 0
    
    # находит максимальное положение символов и создает
    # список такой длины
    for key in dict_sym:
        for val in dict_sym[key]:
            if int(val) > counter:
                counter = int(val)

    list_sym = ['']*(counter + 1)

    # переводит значения в списке, который является значением ключа словаря
    for key in dict_sym:
        dict_sym[key] = [int(item) for item in dict_sym[key]]

    # располагает все символы на свои места
    for key in dict_sym:
        for ind in dict_sym[key]:
            list_sym[ind] = str(chr(int(key))) 

    # записывает все в файл
    name = filename.split('.')
    with open(name[0] + '_decoding.' + name[1], 'w') as f:
        f.write(''.join(list_sym))

        
def main():
    args = sys.argv[1:] # пример:\\\kriptograffy.py\\\ --encoding example.txt 

    if not args or len(args)!=3:
        print('usage:[--encoding] or [--decoding] filename key')
        sys.exit(1)

    if args[0] == '--encoding':
        encoding(args[1], int(args[2]))
    elif args[0] == '--decoding':
        decoding(args[1], int(args[2]))
        
        
if __name__ == "__main__":
    print('This program encrypts \ decrypt text files.')
    print('Use [--encoding] flag for encription and [--decoding] flag for decription.\n')
    main()
