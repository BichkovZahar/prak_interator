def multiply_by():
    def mult(a , b):
        return a * b
    return mult
mult = multiply_by()
print(mult(3 , 9))
