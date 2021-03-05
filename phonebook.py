class PhoneBook:

    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        # This creates map with 'name' as key and 'number' as value
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True

    def get_names(self):
        # Comprehension instead of for-loop
        # '_' indicates to python that we do NOT care about the second variable in the tuple
        # So, in this case it returns a list of names only ('number' is ignored)
        return [name for name, _ in self.numbers.items()]

    def get_numbers(self):
        return [number for _, number in self.numbers.items()]



