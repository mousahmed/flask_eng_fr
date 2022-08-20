import unittest

from translator import french_to_english, english_to_french


class TestTranslations(unittest.TestCase):
    def test_english_to_french_null_value(self):
        self.assertNotEqual(english_to_french(""), "Bonjour")

    def test_english_to_french(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_french_to_english_null_value(self):
        self.assertNotEqual(french_to_english(""), "Hello")

    def test_french_to_english(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
