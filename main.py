lst = [1 , 2 , 3 , 4 , 5, 6 , 7]
class SquareGenerator:

    def __init__(self):
        if isinstance(lst , list) is True:
            print(lst)
        elif isinstance(lst , lst) is not True:
            raise TypeError("Беги🤬")
    def my_generator(self):
        for item in lst :
            yield item ** 2

    for num in my_generator(lst):
        print(num)