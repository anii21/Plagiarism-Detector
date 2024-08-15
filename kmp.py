def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = [0] * m
    j = 0
    
    compute_lps_array(pattern, m, lps)
    
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            
        if j == m:
            return True
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
                
    return False

def compute_lps_array(pattern, m, lps):
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
