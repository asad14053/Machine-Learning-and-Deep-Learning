# Finish implementing the following class, called Specimen, as indicated in the comments

'''
Python Raw Coding by a C/C++ expert
Compiled by:
Md. Asaduzzaman Jabin
Ph.D. Student, ECE, UGA
'''

class Specimen:

    def __init__(self,ID, type, height_cm, weight_kg):
        # Input: ID (any object, but likely int or string), type (string), height_cm (numeric), weight_kg (numeric)
        # Output: None, side effect of initialized object (self) with ID, type, height_cm, and weight_kg properties

        self.ID = int(ID)
        self.type = str(type)
        self.height_cm = float(height_cm)
        self.weight_kg = float(weight_kg)
        pass

    def __str__(self):
        # Input: None
        # Output: a string to print
        # such that a = Specimen(1,"human",25.234252,2.24231); print(a) would yield "1: human - 25.23 cm, 2.24 kg"

        return f"{self.ID}: {self.type} - {self.height_cm} cm, {self.weight_kg} kg"

    def height(self, units_str):
        # Input: units_str (string, optional), the return the height in the requested units, which should be one of {"cm","m","ft","in"}
        # Output: The height in the desired units
        # Note: Conversion constants: cm->m /100, cm->ft /30.48, cm->in /2.54

        if(units_str == "m"):
            return (self.height_cm)/100
        elif(units_str == "ft"):
            return (self.height_cm)/30.48
        elif(units_str == "in"):
            return (self.height_cm)/2.54
        else: return self.height_cm

    def weight(self, units_str):
        # Input: units_str (string, optional), return the weight in the requested units, which should be one of {"g","kg","lb","oz"}
        # Output: The weight in the desired units
        # Note: Conversion constants: kg->g *1000, kg->lb *2.205, kg->oz *35.274

        if(units_str == "g"):
            return (self.weight_kg)*1000
        elif(units_str == "lb"):
            return (self.weight_kg)*2.205
        elif(units_str == "in"):
            return (self.weight_kg)*35.274
        else: return self.weight_kg

# A = Specimen(1,"human",25.234252,2.24231)
# print(Specimen.height(A, "ft"))
# print(Specimen.weight(A, "lb"))

'''


Output:
$ "C:/Users/Wrong Answer/miniconda3/python.exe" "c:/Users/...........assignment-3-functions-and-classes-asad14053/specimen.py"
0.827895406824147
4.944293549999999
'''

