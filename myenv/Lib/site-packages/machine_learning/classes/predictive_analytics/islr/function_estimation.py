# -*- coding: utf-8 -*-

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

class function_estimation:
    __num_threads = 0
    __thread_started = False
    __lock = allocate_lock()
    __data = None
    __list_methods = []
    
    @classmethod
    def thread_1(cls):
        cls.__lock.acquire()
        cls.__thread_started = True
        text = """The Advertising data set consists of the sales of that product in 200 different markets, along with advertising budgets for the product in each of those markets for three different media: TV, radio, and newspaper."""
        text += '\n'
        cls.__data = pd.read_csv('http://www-bcf.usc.edu/~gareth/ISL/Advertising.csv', index_col=0)
        #print(data.columns.values) check columns of a dataframe
        # plot data with seaborb and include a "regression line"
        while cls.__data is None:
            pass
        print(text)
        print(cls.__data.head())
        cls.__lock.release()
        
        return True
    
    @classmethod    
    def thread_2(cls):       
        cls.__lock.acquire() 
        while cls.__data is None:
            pass
        sns.pairplot(cls.__data, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=6, aspect=0.7, kind='reg')
        plt.show()
        text = """The Advertising data set. The plot displays sales, in thousands of units, as a function of TV, radio, and newspaper budgets, in thousands of
dollars, for 200 different markets. In each plot we show the **Simple Least Squares** fit of sales to that variable. In other words, each
line represents a simple model that can be used to predict sales using TV, radio, and newspaper, respectively."""
        #print("check:" + dic_gs['estimation_reasons'])
        # scatter plot in Pandas
        printmd(text)
        while cls.__data is None:
            pass
        fig, axs = plt.subplots(1, 3, sharey=True)
        cls.__data.plot(kind='scatter', x='TV', y='sales', ax=axs[0], figsize=(16, 6))
        cls.__data.plot(kind='scatter', x='radio', y='sales', ax=axs[1])
        cls.__data.plot(kind='scatter', x='newspaper', y='sales', ax=axs[2])
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
        try:
            for key, value in cls.__dict__.items():
                if isinstance(value , classmethod):
                    cls.__list_methods.append(key)
            if len(cls.__list_methods) > 0:
                m = map(str, cls.__list_methods)
                j = ', '.join(m)
                printmd('**Search Methods**')
                print(j)
        except:
            print("This is an error message!")
        cls.__lock.release()
        
        
    