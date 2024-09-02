# your code goes here!
class Anagram:
    def __init__(self, word: str):
        # Initialize with the word and normalize it
        self.original_word = word
        self.normalized_word = ''.join(sorted(word))
        
    def match(self, possible_anagrams: list) -> list:
        # Create a list to hold matching anagrams
        matches = []
        
        # Check each word in the possible anagrams
        for candidate in possible_anagrams:
            # Normalize the candidate word
            if ''.join(sorted(candidate)) == self.normalized_word:
                matches.append(candidate)
        
        return matches
