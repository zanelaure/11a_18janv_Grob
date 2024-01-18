#Izveidot Python programmu, kas ļauj lietotājam ievadīt savu vārdu terminālī.
#Ievadīto vārdu pēc tam ierakstīt teksta failā (piemēram, "lietotajs.txt").
#Programmai jābūt spējīgai apstrādāt kļūdas, piemēram, faila nepieejamību vai rakstīšanas problēmas.
#Pēc ierakstīšanas izvadīt paziņojumu par veiksmīgu darbību vai kļūdu gadījumā attiecīgu kļūdas ziņojumu.
import json
file_name = input
with  open('lietotajs.txt', 'w', encoding='utf-8') as bum:
    json.dump(...)