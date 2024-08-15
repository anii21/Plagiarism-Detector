def bm_search(text, pattern):
    m = len(pattern)
    n = len(text)
    bad_char = [-1] * 256
    
    for i in range(m):
        bad_char[ord(pattern[i])] = i
    
    s = 0
    while s <= n - m:
        j = m - 1
        
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        
        if j < 0:
            return True
            s += (m - bad_char[ord(text[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    
    return False


