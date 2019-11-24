import string


def remove_punctuation(input_string: str) -> str:
    """Returns a string with the punctuation signs stripped out

    Arguments:
        input_string {str} -- Input string from which to remove the punctuation

    Returns:
        str -- String with punctuation signs removed
    """
    return "".join(
        [char for char in input_string if char not in string.punctuation]
    )


if __name__ == "__main__":
    print(remove_punctuation("dit is een test. probeer het ook eens!"))
