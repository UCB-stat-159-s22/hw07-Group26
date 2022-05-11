from scipy import stats
import matplotlib.pyplot as plt
from scipy.stats import ranksums

def plt_by_diagnosis(dat, column, name):
    """
    Plot the comparitive count distribution of the column specified for those 
    diagnosed vs. those not.
    ---
    Arguments: 
    dat (pandas dataframe): the dataframe which contains two columns, a diagnosis 
                            column and a column to plot the distribution of. 
    column (str): name of the column, which is a int, float type, to plot the 
                  distribution of.
    name (str): label the title of the plot
    ---
    Returns 
    None, plots the figure.
    Additionally, saves the figure under the figures folder.
    """
    cols = dat["diagnosis"].unique()
    plt.hist([dat.loc[dat["diagnosis"] == x, column] for x in cols], label=cols);
    plt.legend()
    plt.title(name + " by Diagnosis");
    plt.xlabel(name)
    plt.ylabel("Count");
    plt.savefig('../figures/' + column)


def two_sample_t_test(dat, by, feature, var, param):
    """
    Conducts the two sample t-test for two populations.
    ---
    Arguments: 
    dat (pandas dataframe): the dataframe which contains two columns, a 'by' 
                            column and a 'feature' column.
    by (str): name of the column, which is of binary type (0, 1), to segregate 
              the two populations by. 
    feature (str): name of the column, which is a int, float type, to compute the 
                   population parameter difference.
    var (boolean): 'True' or 'False' as to whether the two populations have the same
                    population variance or not.
    param (boolean): conduct parametric two sample t test, otherwise conducts 
                     Wilcoxon rank-sum test, which is a non-parametric test.
    ---
    Returns tuple containing the (t-statistic, p-value)
    Prints the conclusion of the hypothesis test.
    """

    
    dat_0 = dat.loc[dat[by] == 0]
    dat_1 = dat.loc[dat[by] == 1]
    
    results = stats.ttest_ind(dat_0[feature], dat_1[feature], equal_var=var)
    results_n_param = ranksums(dat_0[feature], dat_1[feature])
    
    
    if param == True:
        p = results[1]
        if p < 0.01:
            print("Statistically Highly Significant, Reject Null Hypohesis")
            return results
        elif p < 0.05:
            print("Statistically Significant, Reject Null Hypohesis")
            return results
        else:
            print("Fail to Reject Null Hypohesis")
            return results
    else: 
        p = results_n_param[1]
        if p < 0.01:
            print("Statistically Highly Significant, Reject Null Hypohesis")
            return results_n_param
        elif p < 0.05:
            print("Statistically Significant, Reject Null Hypohesis")
            return results_n_param
        else:
            print("Fail to Reject Null Hypohesis")
            return results_n_param