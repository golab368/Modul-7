from faker import Faker
fake = Faker()
list_of_people = []
#Ten program tworzy wizytowki Podstawowe lub Businessowe
#Mozna sprawdzac dlugosc imienia i nazwiska oraz wybierac polaczenie do osoby z wizytowki

#tworzy konakty podstawowe
def create_contacts():
    faker_BaseContact = BaseContact(name = fake.name(),private_phone = fake.phone_number() ,email_adress = fake.email())
    return faker_BaseContact
#tworzy kontakty businessowe
def create_contacts_for_business():
    faker_BusinessContact = BusinessContact(name = fake.name(),private_phone = fake.phone_number() ,email_adress = fake.email() ,position = fake.job(), company_name = fake.company(), business_phone =  fake.email())
    #tutaj pytac uzytkonika czy fejkowac biznes czy standard
    return faker_BusinessContact
# klasa dla podstawy ze stringiem i wybieraniem numeru
class BaseContact:
    def __init__(self,name,private_phone,email_adress):
        self.name = name
        self.private_phone = private_phone
        self.email_address = email_adress
    def __str__(self):
        return f'{self.name} {self.private_phone} {self.email_address}'
    def contact(self):
        return f"Wybieram numer {self.private_phone} i dzwonie do {self.name}"

#Na podstawie BaseContact tworze dziedziczenie klasy dla BusinessContact z paroma dodatkowymi parametrami
class BusinessContact(BaseContact):
    def __init__(self , position, company_name, business_phone, *args, **kwargs ):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company_name = company_name
        self.business_phone = business_phone
    def __str__(self):
        return f'{self.name} {self.private_phone} {self.email_address} {self.position} {self.company_name} {self.business_phone}'
    def contact(self):
        return f"Wybieram numer businessowy {self.business_phone} i dzwonie do {self.name}"

#Tutaj mam pare pytan, jakie sa sposoby na odwolywanie sie do utworzonych wizytowek?
#Jak zrobila by to osoba z doswiadczeniem?
#jak moge sie odwolywac do klasy z listy list_of_people ? aby sie ona drukowala nie uzywajac def __str__(self)?
# jak tworzyc inputa z numerem +1 czyli do_you_want_to_contact_with_someone ma zakres od 0 do 4 a chce od 1 do 5, jak to zrobic?
#Jak oddzielic label_length czyli Milosz6 Golebiowski11 na Milosz 6 golebiowski 11
#ostatnie jak zamiast fakera skorzystac ze storny internetowej fakegenerator pobierajac np. 5 randomowcyh danych
#to co nas interesuje imie nazwisko email itd, uzywac api samego czytania z json? api chyba nie jest potrzebne bo chce odczytac i skopiowac dane do programu?
what_user_what_to_do = input("Co Tworzymy 5 wizytowek Podstawowych = 1 czy Businessowych = 2 ? Wpisz: 1 lub 2: ")
print()

if what_user_what_to_do == "1":
    i= 0
    for i in range(5):
        list_of_people.append(create_contacts())
    for x in list_of_people:
        print(x,"\n")
elif what_user_what_to_do == "2":
    i= 0
    for i in range(5):
        list_of_people.append(create_contacts_for_business())
    for y in list_of_people:
        print(y,"\n")

do_you_want_to_contact_with_someone = input("Z kim chcesz sie skontaktowac : od 0 do 4 (numer odpowiada osobie wydrukowanej we wczesniejszym etapie zaczynajac od 0)\n")
print(list_of_people[int(do_you_want_to_contact_with_someone)].contact(),"\n")

do_you_want_to_know_len_of_name = input("Potrzebujesz dlugosci imienia i nazwiska osoby z wizytowki wpisz imie i nazwisko lub skopiuj i wklej : ")
label_length =["{}{}".format(i,len(i)) for i in do_you_want_to_know_len_of_name.split(" ")]
print(label_length)



