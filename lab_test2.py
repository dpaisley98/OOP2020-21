# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# B. Schoen-Phelan
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self.characters = []
        self.cursor = 0
        self.filename = file_name
        self.range_char = 0

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
#       error checking to ensure the input is an integer
        if not isinstance(character, str):
            raise TypeError("Wrong type, we need a string")

        self.chars_property.insert(self.cursor_property, character)
        self.cursor_property += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        try:
            if self.cursor_property not in range(self.range_property):
                self.cursor_property = int(self.cursor_property / self.range_property)
            del self.chars_property[self.cursor_property]
        except:
            raise TypeError(f"Cursor outside range")

    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.chars_property))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor_property += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
#       error checking to ensure the input is an integer
        if not isinstance(steps, int):
            raise TypeError("Wrong type, we need a number")
#       used to find the range of the character array to ensure all user inputs can be within the range
        self.range_property = len(self.chars_property)
#           if statement to make sure the number is within the the character array
        if steps not in range(-self.range_property, self.range_property):
            steps = int(steps / self.range_property)

        self.cursor_property -= steps

#   encapsulation for the character array
    @property
    def chars_property(self):
        return self.characters

    @chars_property.setter
    def chars_property(self, value):
        self.characters = value

#   encapsulation for the character array
    @property
    def range_property(self):
        return self.range_char

    @range_property.setter
    def range_property(self, value):
        self.range_char = value

#   encapsulation for the cursor
    @property
    def cursor_property(self):
        return self.cursor

    @cursor_property.setter
    def cursor_property(self, value):
        self.cursor = value


# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

doc.backward()
doc.delete()
doc.insert('s')
doc.save()
