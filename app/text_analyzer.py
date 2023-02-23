import re

class TextAnalyzer:
    def __init__(self, string: str):
        self.string = string
    
    @classmethod 
    def text_tokenizer(cls, string: str) -> dict:
        if isinstance(string, str):
            words = re.sub('[^A-Za-z0-9 ]+', '', string).split()
            chars = (word for word in string.split() if word.isascii())
            whitespaces = re.sub('[^ ]+', '', string)

            result = {'words': words, 'chars': chars, 'whitespaces': whitespaces}
        
            return result
   
    def validate_paragraph_size(self) -> bool:
        """Return True or False

        A function to check that the size of the input paragraph is not be more than 500 words. Accept only a words parameter from the object.
        """
        tokens = self.text_tokenizer(self.string)

        if tokens is not None:
            paragraph_size = len(tokens['words'])
            
            return paragraph_size <= 500
        else:
            return False

    def word_frequency_counter(self) -> dict:
        """Return a dict, with alphabetically ordered keys

        A function to count the repetition of each word (alphanumeric).
        """
        tokens = self.text_tokenizer(self.string)
        words = tokens['words']
        
        counts = {}

        for word in words:      
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

        result = {k:counts[k] for k in sorted(counts)}

        return result
    
    def word_counter(self) -> int:
        """Return an int

        A function to count the total number of words. 
        """
        tokens = self.text_tokenizer(self.string)
        words = tokens['words']

        result = len(words)

        return result
    
    def char_counter(self) -> tuple:
        """Return a tuple

        A function to count the total number of characters, a) with whitespaces, b) without whitespaces. 
        """
        tokens = self.text_tokenizer(self.string)
        chars = list(tokens['chars'])
        whitespaces = tokens['whitespaces'].count(' ')

        chars_wo_whitespaces = len("".join(chars))
        chars_w_whitespaces = chars_wo_whitespaces + whitespaces

        result = (chars_w_whitespaces, chars_wo_whitespaces)

        return result