import unittest
from translator import englishToFrench, frenchToEnglish

class TestTranslationMethods(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench(''), 'Error: No text provided for translation')
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')

    def test_frenchToEnglish(self):
        self.assertEqual(frenchToEnglish(''), 'Error: No text provided for translation')
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()