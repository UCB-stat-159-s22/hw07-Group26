import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib import rcParams

def plot_three_figs_horizontally(file_list):
    """
    Display three figures horizontally
    ---
    Arguments:
    file_list (list): a list includes file names of three figures in order
   
    Returns:
    three horizontally displayed images
    """
    # figure size in inches optional
    rcParams['figure.figsize'] = 30 ,8

    # read images
    img_cm = mpimg.imread(file_list[0])
    img_prc = mpimg.imread(file_list[1])
    img_roc =  mpimg.imread(file_list[2])

    # display images
    fig, ax = plt.subplots(1,3)
    ax[0].imshow(img_cm)
    ax[1].imshow(img_prc)
    ax[2].imshow(img_roc)
    ax[0].axis('off') 
    ax[1].axis('off') 
    ax[2].axis('off');
