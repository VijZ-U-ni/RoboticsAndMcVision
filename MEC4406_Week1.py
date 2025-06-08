my_Name = "Vijesh"
mirror_name = my_Name[::-1]   
print(my_Name)
print(mirror_name)

fav_number = 11
for i in range((fav_number)**2 +1):

        print(i)

    
    
    
class Engineer:
    skill = "problem solver"
    
    def __init__(self, name, type_of_engineering, experience ):
        self.name = name
        self.type_of_engineering = type_of_engineering
        self.experience = experience
    def self_print(self):
        print(self.name, end=" ")
        print(self.type_of_engineering, end=" ")
        print(self.experience)
       
e1=Engineer(my_Name,"Mechatronics",4)
e2=Engineer(mirror_name,"Mechatronics",8)
e1.self_print()
e2.self_print()
mirror_name = my_Name[::-1]