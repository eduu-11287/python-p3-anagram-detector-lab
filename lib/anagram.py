class Anagram:
    def __init__(self, word):
        self.sorted_word = sorted(word)
    
    def match(self, possible_anagram):
        matches = []
        
        for word in possible_anagram:
            if sorted(word) == self.sorted_word:
                matches.append(word)
        
        return matches  

listen = Anagram("enlist")
results = listen.match(['listen', 'poison', 'hello'])
print(results)  
