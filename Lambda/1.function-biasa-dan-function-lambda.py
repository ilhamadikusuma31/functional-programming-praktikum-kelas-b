# function biasa
tanya = "ilham"
def sayHi(var):
    return "hallo aku bernama " + var
penampung = sayHi(tanya)
print(penampung)

# function lambda
sayHi = lambda var: "hallo aku bernama " + var
penampung = sayHi(tanya)
print(penampung)