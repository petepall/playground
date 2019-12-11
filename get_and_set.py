class Geeks:
    """class to set and get the age of a person
        
    Keyword Arguments:
        age {int} -- age of a person (default: {None})
    """

    def __init__(self, age: int = None):
        self.age = age

    @property
    def age(self):
        """property showing the age
        
        Returns:
            int -- age of the person
        """
        return self.__age

    @age.setter
    def age(self, age: int):
        """property to set the age
        
        Arguments:
            age {int} -- age of the person
        
        Raises:
            ValueError: raises an error if the age value is <= 0
        """
        if age <= 0:
            raise ValueError("Sorry the given age is not correct")
        self.__age = age


peter = Geeks(5)
print(peter.age)
peter.age = 47
print(peter.age)
