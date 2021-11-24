def sort_sentence(sentence):
    
    sentence = sentence.lower().split(' ')
    
    for i in range(1, len(sentence)):
        key = sentence[i]
        j = i-1
        while j >= 0 and len(key) < len(sentence[j]):
            sentence[j+1] = sentence[j]
            j -= 1
        sentence[j+1] = key
    
    sentence[0] = sentence[0][0].upper() + sentence[0][1:]
    
    return ' '.join(sentence)
