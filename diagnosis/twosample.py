from scipy import stats
import matplotlib.pyplot as plt


def plt_by_diagnosis(dat, column, name):
    # Plots the count distribution of the column specified for those with cancer vs. 
    # those without. 
    # The input data must have a diagnosis column. 
    # The output is a plot.
    cols = dat["diagnosis"].unique()
    plt.hist([dat.loc[dat["diagnosis"] == x, column] for x in cols], label=cols);
    plt.legend()
    plt.title(name + " by Diagnosis");
    plt.xlabel(name)
    plt.ylabel("Count");
    plt.savefig('../figures/' + column)


def two_sample_t_test(dat, by, feature, var):
    # Conducts the two sample t test for the data where the two populations are
    # segregated by the "by" input. The input feature is the featuree that we
    # want to test whether it has the sample value or not in the two populations.
    # The var is boolean signalling whether the two populations have the
    # same variance or not. 
    # # The output is the t statistics, p value.
    
    dat_0 = dat.loc[dat[by] == 0]
    dat_1 = dat.loc[dat[by] == 1]
    results = stats.ttest_ind(dat_0[feature], dat_1[feature], equal_var=var)
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