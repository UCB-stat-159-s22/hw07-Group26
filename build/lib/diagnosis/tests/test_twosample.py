from diagnosis.twosample import two_sample_t_test
import nump as np
import pandas as pd

dat = pd.read_csv('../../data/clean.csv')

def test_p_value_lower_a():
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "area_worst", False)
    assert p_value > 0  
    
def test_p_value_upper_a():
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "area_worst", False)
    assert p_value < 1 
    
def test_p_value_lower_t():
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "texture_se", True)
    assert p_value > 0  
    
def test_p_value_upper_t():
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "texture_se", True)
    assert p_value < 1  
    
def test_t_stat():
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "texture_se", True)
    assert t_statistics > 0  
    