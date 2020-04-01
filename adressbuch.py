from Tkinter import *

class GUI:
    def __init__(self,surface):
        self.surface = surface
    
    def main(self):
        lbl = Label(self.surface, text="Hello", font=("Arial Bold", 50))
        lbl.grid(column=0, row=0)
        self.surface.geometry('350x200')


class Person:
    def __init__(self,fname,lname,adr,city,state,plz,phone):
        self.firstName = fname
        self.lastName = lname
        self.address = adr
        self.city = city
        self.state = state
        self.plz = plz
        self.phone = phone

    def person_edit(self,adr,city,state,plz,phone):
        self.address = adr
        self.city = city
        self.state = state
        self.plz = plz
        self.phone = phone

    def person_print(self):
        print(self.firstName)
        print(self.lastName)
        print(self.address)
        print(self.city)
        print(self.state)
        print(self.plz)
        print(self.phone)

class Addressbook:
    def __init__(self):
        self.person_list = []
    def create_person(self,fname,lname,adr,city,state,plz,phone):
        self.person_list.append(Person(fname,lname,adr,city,state,plz,phone))
    def print_person(self):
        for i in self.person_list:
            i.person_print()
            print('')
    def sort_plz(self):
        self.person_list.sort(key=lambda person: person.plz)
    def sort_name(self):
        self.person_list.sort(key=lambda person: person.lastName)
    def person_del(self,pos):
        del self.person_list[pos]

# surface = Tk()

# Addressbook = GUI(surface)
# Addressbook.main()


# surface.mainloop()
# person = Person(1,2,3,4,5,6,7)
# person.person_print()
# person.person_edit(8,9,10,11,12)
# person.person_print()
adressbook = Addressbook()
adressbook.create_person('c','c','c','c','c','c','c')
adressbook.print_person()
adressbook.create_person('b','b','b','b','b','b','b')
adressbook.create_person('a','a','a','a','a','a','a')
adressbook.print_person()
adressbook.sort_name()
adressbook.print_person()
adressbook.person_del(0)
adressbook.print_person()