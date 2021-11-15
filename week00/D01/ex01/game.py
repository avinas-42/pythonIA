class GotCharacter:
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

    def get_first_name(self):
        return self.first_name

    def get_is_alive(self):
        return self.is_alive

    def __str__(self):
        return "first_name: " + self.first_name + \
                " , " + "is_alive: " + self.is_alive


class Lannister(GotCharacter):
    """A class representing the Lannister family."""

    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.house_words = "chocapik"

    def print_house_words(self):
        print(self.house_words)

    def die(self):
        self.is_alive = False

    def get_family_name(self):
        return self.family_name

    def get_house_words(self):
        return self.house_words

    def __str__(self):
        return "family_name: " + self.family_name + " , " + \
                "house_words: " + self.house_words
