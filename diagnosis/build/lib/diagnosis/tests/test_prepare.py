import pandas as pd
from diagnosis.prepare import *

def test_clean_data():
    """
    Test clean_data function in diagnosis.prepare
    """
    test_input = pd.DataFrame(data={"a":[1.0, np.nan, 3.0, 1.0],
                                    "b":[1.0, 3.0, 3.0, 1.0],
                                    "c":[2.0, 4, 1, 4]})
    test_output = pd.DataFrame(data={"a":[1.0, 3.0],
                                     "b":[1.0, 3.0]})
    out = clean_data(test_input)
    assert test_output.equals(out)
    
def test_load_data():
    """
    Test load_data function in diagnosis.prepare
    """
    val_size = 0.2
    test_size = 0.2
    train, val, test = load_data('data/raw_data.csv', val_size=val_size, test_size=test_size)
    assert train.shape == (round(569 * 0.8 * 0.8), 32) and val.shape == (round(569 * 0.8 * 0.2), 32) and test.shape == (round(569 * 0.2), 32)
