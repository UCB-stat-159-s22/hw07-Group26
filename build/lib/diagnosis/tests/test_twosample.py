from diagnosis.twosample import two_sample_t_test
import numpy as np
import pandas as pd

dat = pd.read_csv('data/clean.csv')

def test_p_value_lower_a():
<<<<<<< HEAD
    """
    Asserts whether the p value of the area_worst feature is greater than zero 
    in the two sample t test.
    """
=======
>>>>>>> 13b7418971d57be2da2ed1b7cba28b3519c69ac5
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "area_worst", False)
    assert p_value > 0  
    
def test_p_value_upper_a():
<<<<<<< HEAD
    """
    Asserts whether the p value of the area_worst feature is less than zero 
    in the two sample t test.
    """
=======
>>>>>>> 13b7418971d57be2da2ed1b7cba28b3519c69ac5
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "area_worst", False)
    assert p_value < 1 
    
def test_p_value_lower_t():
<<<<<<< HEAD
    """
    Asserts whether the p value of the texture_se feature is greater than zero 
    in the two sample t test.
    """
=======
>>>>>>> 13b7418971d57be2da2ed1b7cba28b3519c69ac5
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "texture_se", True)
    assert p_value > 0  
    
def test_p_value_upper_t():
<<<<<<< HEAD
    """
    Asserts whether the p value of the texture_se feature is less than zero 
    in the two sample t test.
    """
=======
>>>>>>> 13b7418971d57be2da2ed1b7cba28b3519c69ac5
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "texture_se", True)
    assert p_value < 1  
    
def test_t_stat():
<<<<<<< HEAD
    """
    Asserts whether the t statistic of the texture_se feature is greater than zero 
    in the two sample t test.
    """
=======
>>>>>>> 13b7418971d57be2da2ed1b7cba28b3519c69ac5
    t_statistics, p_value = two_sample_t_test(dat, "diagnosis", "texture_se", True)
    assert t_statistics > 0  
    