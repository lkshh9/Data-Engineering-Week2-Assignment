def greet(person):
    return "Hi {name}".format(**person)


def test_greet():
    lokesh = {"name": "Lokesh"}  # Arrange
    greeting = greet(lokesh)  # Act
    assert greeting == "Hi Lokesh"  # Assert
