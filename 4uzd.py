#Izveidot Python programmu, kur  lietotājs ievada gan faila nosaukumu, gan faila formātu (paplašinājumu),
# un atkarībā no faila paplašinājuma tiek nolasīts faila saturs.  Nolasītā informācija ir jāizdrukā terminālī.
# Ievērot iespejamās kļūdas!

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "Datne nav atrasta"

def read_until_length(content, length):
    try:
        length = int(length)
        return content[:length]
    except ValueError:
        return "Ievadītias garums nav skaitlis"

def print_first_line(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            first_line = file.readline()
            print(first_line)
    except FileNotFoundError:
        print("Datne nav atrasta")

file_name = input("Ievadi datnes nosaukumu: ")
file_content = read_file(file_name)