from abc import ABC, abstractmethod


class Maths(ABC):

    @abstractmethod
    def __init__(self):
        """
        Currently sets a welcome message.
        Any instance variables necessary for game play should
        be declared here.
        Derived classes must implement this abstract method.
        """
        print("Welcome to the Math Game")

    @property
    @abstractmethod
    def input_property(self):
        pass

    @abstractmethod
    def play(self):
        pass


class Fibonacci(Maths):
    def __init__(self):
        """
        Initialisation class. Calls the base classe's
        welcome message. Sets an instance variable
        called self.__input to
        receive the user input. Start content is 0.
        """
        super().__init__()
        self._input = 0

    @property
    def input_property(self):
        return self._input

    @input_property.setter
    def input_property(self, value):
        self._input = value

    def play(self):
        guesses = 0
        playing = True

        while playing:
            try:
                self.input_property = int(input("Enter 1 to play and 2 to exit:"))
                if self._input not in range(1,3):
                    print("Please pick either 1 or 2")
            except:
                print("Must be 1 or 2")
                continue

            if self.input_property == 1:
                terms = int(input("How many terms?"))

                if terms != 0:

                    result = self.calculate(terms+1)

                    print(result[:-1])
                    guess = int(input("What's the last term"))

                    if guess == result[-1]:
                        guesses += 1
                        print("Correct!")
                    else:
                        print("Incorrect")

            if self.input_property == 2:
                print(f"Amount of times correct: {guesses}")
                playing = False

    @staticmethod
    def calculate(term):

        num_list = []

        if term > 1:
            num_list.extend([0, 1])

            one_before = num_list[0]
            before = num_list[1]

            if term > 2:
                for number in range(2, term):
                    current = one_before + before
                    num_list.append(current)
                    one_before = before
                    before = current

        if term == 1:
            num_list.append(0)

        return num_list


f = Fibonacci()
f.play()



