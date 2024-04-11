# -*- coding: utf-8 -*-
from _thread import allocate_lock
import pandas as pd
import seaborn as sns
from IPython.display import Latex
from IPython.display import display, Markdown
import matplotlib.pyplot as plt
plt.style.use('ggplot') # emulate R's ggplot package style

def printmd(string):
    display(Markdown(string))

def hello_world():
    print("here")

def function_estimation():
    text = """The Advertising data set consists of the sales of that product in 200 different markets, along with advertising budgets for the product in each of those markets for three different media: TV, radio, and newspaper."""
    text += '\n'
    data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
    print(text)
    print(data.head())
    sns.pairplot(data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=6, aspect=0.7, kind='reg')
    plt.show()
    text = """The Advertising data set. The plot displays sales, in thousands of units, as a function of TV, radio, and newspaper budgets, in thousands of
dollars, for 200 different markets. In each plot we show the **Simple Least Squares** fit of sales to that variable. In other words, each
line represents a simple model that can be used to predict sales using TV, radio, and newspaper, respectively."""
    #print("check:" + dic_gs['estimation_reasons'])
    # scatter plot in Pandas
    printmd(text)
    fig, axs = plt.subplots(1, 3, sharey=True)
    data.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16, 6))
    data.plot(kind='scatter', x='radio', y='sales', ax=axs[1])
    data.plot(kind='scatter', x='newspaper', y='sales', ax=axs[2])
    plt.show()
    text = """Our goal is to develop an accurate model that can be used to predict sales on the basis of the three media budgets. """
    text += """Suppose that we observe a quantitative response Y and p
different predictors, X1,X2, . . .,Xp. We assume that there is some
relationship between Y and X = (X1,X2, . . .,Xp), which can be written
in the very general form"""
    print(text)
    latex_formula = Latex(r"""$Y= X+ \text{ε}$""")
    display(latex_formula)
    text = """Here f is some fixed but unknown function of X 1 , . . . , X p , 
        and \u03B5 is a random *error term*, which is independent of X and has mean zero. In this formulation,
        f represents the *systematic* information that X provides about Y ."""
    printmd(text)
    text = """In general, the function f may involve more than one input variable. 
        Here f is a two-dimensional surface that must be estimated based on the observed data.
        In essence, statistical learning refers to a **set of approaches** for estimating
        f . In this chapter we outline some of the key theoretical concepts that arise
        in estimating f , as well as tools for evaluating the estimates obtained."""
    printmd(text)