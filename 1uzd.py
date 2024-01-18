#Izveidot Python programmu, kas nolasītu un izdrukātu visu teksta faila saturu (txt formātā). 

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Datne nav atrasta")

file_name = input("Ievadiet teksta faila nosaukumu ar .txt formātu paplašinājumu: ")
print(file_name)