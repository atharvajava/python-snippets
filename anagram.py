def anagram(s1,s2):
    s1=list(s1.replace(" ","").lower())
    s2=list(s2.replace(" ","").lower())
    
    if len(s1) != len(s2):
        return False
    return True

print(anagram('Paa','aap'))