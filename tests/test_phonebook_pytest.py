import pytest

from phonebook import PhoneBook


# This is like a setUp method
# Can refer to this to get PhoneBook instance
@pytest.fixture()
def phonebook():
    return PhoneBook()


# Pass phonebook in as param. This will refer to fixture above
# SPELLING COUNTS
def test_lookup_by_name(phonebook):
    phonebook.add("Bob", "1234")
    assert "1234" == phonebook.lookup("Bob")


def test_missing_name_raises_error(phonebook):
    phonebook.add("Bob", "1234")
    # This will test that any of the code below the "with" stmt throws a KeyError
    with pytest.raises(KeyError):
        phonebook.lookup("fake number")


def test_is_consistent_when_empty(phonebook):
    assert phonebook.is_consistent()


def test_is_consistent_when_all_nums_different(phonebook):
    phonebook.add("Bob", "1234567")
    phonebook.add("Sue", "6171830")
    assert phonebook.is_consistent()


def test_is_not_consistent_when_duplicates(phonebook):
    phonebook.add("Bob", "1234567")
    phonebook.add("Sue", "1234567")
    assert not phonebook.is_consistent()


def test_is_not_consistent_when_duplicate_prefixes(phonebook):
    phonebook.add("Bob", "1234567")
    phonebook.add("Sue", "123")
    assert not phonebook.is_consistent()


def test_phonebook_adds_names_and_numbers(phonebook):
    phonebook.add("Sue", "12345")
    phonebook.add("Bob", "1234567")
    assert "Sue" in phonebook.get_names()
    assert "12345" in phonebook.get_numbers()
    assert "Bob" in phonebook.get_names()
    assert "1234567" in phonebook.get_numbers()
