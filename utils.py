from preprocessing import preprocess
from kmp import kmp_search
from bm import bm_search
from rk import rk_search
import time

def detect_plagiarism(text, pattern):
    preprocessed_text = preprocess(text)
    preprocessed_pattern = preprocess(pattern)
    
    kmp_result = kmp_search(preprocessed_text, preprocessed_pattern)
    bm_result = bm_search(preprocessed_text, preprocessed_pattern)
    rk_result = rk_search(preprocessed_text, preprocessed_pattern)
    
    return kmp_result or bm_result or rk_result

def efficiency_matrix(text, pattern):
    preprocessed_text = preprocess(text)
    preprocessed_pattern = preprocess(pattern)
    
    results = {}
    
    start_time = time.time()
    kmp_search(preprocessed_text, preprocessed_pattern)
    results['KMP'] = time.time() - start_time
    
    start_time = time.time()
    bm_search(preprocessed_text, preprocessed_pattern)
    results['Boyer-Moore'] = time.time() - start_time
    
    start_time = time.time()
    rk_search(preprocessed_text, preprocessed_pattern)
    results['Rabin-Karp'] = time.time() - start_time
    
    return results


