import unittest

from app.text_analyzer import TextAnalyzer
import test_data

class TestTextAnalyzer(unittest.TestCase):
    def test_validate_paragraph_size01(self):
        actual = TextAnalyzer(test_data.validate_paragraph_size01).validate_paragraph_size()
        self.assertTrue(actual, 'The size of the paragraph is bigger than 500 words.')

    def test_validate_paragraph_size02(self):
        actual = TextAnalyzer(test_data.validate_paragraph_size02).validate_paragraph_size()
        self.assertFalse(actual, 'The size of the paragraph is bigger than 500 words.')

    def test_validate_paragraph_size03(self):
        actual = TextAnalyzer(test_data.validate_paragraph_size03).validate_paragraph_size()
        self.assertTrue(actual, 'The size of the paragraph is bigger than 500 words.')

    def test_validate_paragraph_size04(self):
        actual = TextAnalyzer(test_data.validate_paragraph_size04).validate_paragraph_size()
        self.assertFalse(actual, 'The paragraph should be only string and can not be empty.')

    def test_word_freq_count_unique01(self):
        actual = TextAnalyzer(test_data.word_freq_count_unique01).word_frequency_counter()
        expected = {'A': 1, 'count': 1, 'each': 1, 'function': 1, 'of': 1, 'repetition': 1, 'the': 1, 'to': 1, 'word': 2}
        self.assertEqual(actual, expected, 'The number of unique words is wrong.')

    def test_word_freq_count_unique02(self):
        actual = TextAnalyzer(test_data.word_freq_count_unique02).word_frequency_counter()
        expected = {'A': 3, 'count': 2, 'each': 3, 'function': 2, 'of': 3, 'repetition': 3, 't': 1, 'the': 1, 'to': 2, 'word': 5}
        self.assertEqual(actual, expected, 'The number of unique words is wrong.')

    def test_word_freq_count_unique03(self):
        actual = TextAnalyzer(test_data.word_freq_count_unique03).word_frequency_counter()
        expected = {'1': 2, '2': 1, '11': 1, '12': 1, '1425': 1, 'A': 3, 'count': 2, 'each': 3, 'function': 2, 'of': 3, 'repetition': 3, 't': 1, 'the': 1, 'to': 2, 'word': 5 }
        self.assertEqual(actual, expected, 'The order of unique words and numbers is wrong.')

    def test_word_counter01(self):
        actual = TextAnalyzer(test_data.word_counter01).word_counter()
        expected = 10
        self.assertEqual(actual, expected, 'The number of words is wrong.')

    def test_word_counter02(self):
        actual = TextAnalyzer(test_data.word_counter02).word_counter()
        expected = 25
        self.assertEqual(actual, expected, 'The number of words is wrong.')

    def test_char_counter01(self):
        actual = TextAnalyzer(test_data.char_counter01).char_counter()
        expected = (53,43)
        self.assertEqual(actual, expected, 'The number of characters is wrong.')

    def test_char_counter02(self):
        actual = TextAnalyzer(test_data.char_counter02).char_counter()
        expected = (132,108)
        self.assertEqual(actual, expected, 'The number of characters is wrong.')

    def test_char_counter03(self):
        actual = TextAnalyzer(test_data.char_counter03).char_counter()
        expected = (55,44)
        self.assertEqual(actual, expected, 'The number of characters is wrong.')

if __name__ == '__main__':
    unittest.main()