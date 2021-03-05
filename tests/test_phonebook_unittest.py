import unittest
from phonebook import PhoneBook


class PhoneBookTest(unittest.TestCase):
    # Runs before EVERY test
    def setUp(self) -> None:
        self.phonebook = PhoneBook()

    # Runs after EVERY test
    def tearDown(self) -> None:
        pass

    def test_lookup_by_name(self):
        self.phonebook.add("Bob", "12345")
        number = self.phonebook.lookup("Bob")
        self.assertEqual("12345", number)

    def test_missing_name_raises_error(self):
        # This will test that any of the code below the "with" stmt throws a KeyError
        with self.assertRaises(KeyError):
            self.phonebook.lookup("fake number")

    def test_is_consistent_when_empty(self):
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_consistent_when_all_nums_different(self):
        self.phonebook.add("Bob", "1234567")
        self.phonebook.add("Sue", "6171830")
        self.assertTrue(self.phonebook.is_consistent())

    def test_is_NOT_consistent_when_duplicates(self):
        self.phonebook.add("Bob", "1234567")
        self.phonebook.add("Sue", "1234567")
        self.assertFalse(self.phonebook.is_consistent())

    def test_is_NOT_consistent_when_duplicate_prefixes(self):
        self.phonebook.add("Bob", "1234567")
        self.phonebook.add("Sue", "123")
        self.assertFalse(self.phonebook.is_consistent())

    def test_phonebook_adds_names_and_numbers(self):
        self.phonebook.add("Sue", "12345")
        self.phonebook.add("Bob", "1234567")
        self.assertIn("Sue", self.phonebook.get_names())
        self.assertIn("12345", self.phonebook.get_numbers())
        self.assertIn("Bob", self.phonebook.get_names())
        self.assertIn("1234567", self.phonebook.get_numbers())