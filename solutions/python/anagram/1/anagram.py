def find_anagrams(word, candidates):
    result = []
    sorted_word = sorted(word.lower())
    
    for candidate in candidates:
        # Skip if same word (case-insensitive)
        if candidate.lower() == word.lower():
            continue
        
        # Check if sorted letters match
        if sorted(candidate.lower()) == sorted_word:
            result.append(candidate)
    
    return result