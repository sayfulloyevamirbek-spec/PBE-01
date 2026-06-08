#Car class yozish
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get_make(self):
#         return self.make

#     def get_model(self):
#         return self.model

#     def get_year(self):
#         return self.year

# car1=Car("Toyota", "Camry", 2020)
# print(car1.get_make())  
# print(car1.get_model()) 
# print(car1.get_year())  
#Teacher class yozish
# class Teacher:
#     def __init__(self, ismi, familiyasi, ish_staji, yonalishi):
#         self.ismi = ismi
#         self.familiyasi = familiyasi
#         self.ish_staji = ish_staji
#         self.yonalishi = yonalishi
    
#     def get_ismi(self):
#         return self.ismi
    
#     def get_familiyasi(self):
#         return self.familiyasi
    
#     def get_ish_staji(self):
#         return self.ish_staji   
    
#     def get_yonalishi(self):
#         return self.yonalishi

# teacher1=Teacher("Ali", "Valiyev", 10, "Matematika")
# print(teacher1.get_ismi())
# print(teacher1.get_familiyasi())
# print(teacher1.get_ish_staji())
# print(teacher1.get_yonalishi())
#Animal → Cat inheritance qilish
# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

#     def get_name(self):
#         return self.name

#     def get_species(self):
#         return self.species
# class Cat(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

#     def get_breed(self):
#         return self.breed
# cat1 = Cat("Whiskers", "Felis catus", "Siamese")
# print(cat1.get_name())
# print(cat1.get_species())
# print(cat1.get_breed()) 

#Polymorphism misoli yozish
 
# class cat :
#     def sound(self):
#         return "Meow"
# class dog :
#     def sound(self):
#         return "Woof"
# def make_sound(animal):
#     print(animal.sound())
# cat1=cat()
# dog1=dog()
# make_sound(cat1)
# make_sound(dog1)

# class transport:
#     def __init__(self, model, yili, rangi, id ):
#         self.model=model
#         self.yili=yili
#         self.rangi=rangi
#         self.id=id
#     def get_model(self):
#         return self.model
#     def get_yili(self):
#         return self.yili
#     def get_rangi(self):
#         return self.rangi
#     def get_id(self):
#         return self.id

# class car(transport):
#     def __init__(self, model, yili, rangi, id, eshik_soni):
#         super().__init__(model, yili, rangi, id)
#         self.eshik_soni=eshik_soni
#     def get_eshik_soni(self):
#         return self.eshik_soni
# class bike(transport):
#     def __init__(self, model, yili, rangi, id, turi):
#         super().__init__(model, yili, rangi, id)
#         self.turi=turi
#     def get_turi(self):
#         return self.turi
# car1=car("Toyota Camry", 2020, "Qora", "123ABC", 4)
# bike1=bike("Yamaha YZF-R3", 2021, "Qizil", "456DEF", "Sport")
# print(car1.get_model())
# print(car1.get_yili())
# print(car1.get_rangi())
# print(car1.get_id())
# print(car1.get_eshik_soni())
# print(bike1.get_model())
# print(bike1.get_yili())
# print(bike1.get_rangi())
# print(bike1.get_id())
# print(bike1.get_turi())

    


   
        