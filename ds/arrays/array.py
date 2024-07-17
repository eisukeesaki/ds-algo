"""

This is a re-implementation of the array data structure.

The purpose of this data structure is to handle values in a sequential manner.

"""

class CustomArray():
    def __init__(self, *elements):
        self.data = self._create_array(elements)

    def _create_array(self, elements):
        return [element for element in elements]

a = CustomArray(11, 22, 33, 44, 55)
print(a.data[0])
