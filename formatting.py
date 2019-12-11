import string


class Circle(object):
    def __init__(self, diameter: float):
        self.diameter = diameter

    def __repr__(self) -> str:
        return str(float(self.diameter))

    def __str__(self) -> str:
        return f"The circle diameter is {self.diameter}"

    @property
    def radius(self):
        return self._diameter / 2

    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, value: float):
        self._diameter = value


def remove_punctuation(input_string: str) -> str:
    """Returns a string with the punctuation signs stripped out

    Arguments:
        input_string {str} -- Input string from which to remove the punctuation

    Returns:
        str -- String with punctuation signs removed
    """
    return "".join([char for char in input_string if char not in string.punctuation])


if __name__ == "__main__":
    print(remove_punctuation("dit is een test. probeer het ook eens!"))

    a = Circle(10)
    a.diameter = 10
    print(a)
    print(f"the radius of {repr(a)} = {a.radius}")
