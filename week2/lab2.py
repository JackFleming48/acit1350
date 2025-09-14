import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Load dataset
data = pd.read_csv('Lab2.txt', sep='\t')

def mean(data):
    return data['Score'].mean()

def median(data):
    return data['Score'].median()

def std_dev(data):
    return data['Score'].std()

def variance(data):
    return data['Score'].var()

def rnge(data):
    return data['Score'].max() - data['Score'].min()

def intquart(data):

    q_one = data.quantile(0.25)
    q_three = data.quantile(0.75)

    return q_three - q_one
    

def set1(data):
    print("Set 1")
    scores = data[data['Set'] == 1]['Score']
    print(f"{scores.mean()}")
    print(f"{scores.median()}")
    print(f"{scores.std()}")
    print(f"{scores.var()}")
    print(f"{scores.max() - scores.min()}")

def set2(data):
    print("Set 2")
    scores = data[data['Set'] == 2]['Score']
    print(f"{scores.mean()}")
    print(f"{scores.median()}")
    print(f"{scores.std()}")
    print(f"{scores.var()}")
    print(f"{scores.max() - scores.min()}")

def quart_set1(data):

    scores = data[data['Set'] == 1]['Score']

    q_one = scores.quantile(0.25)
    q_three = scores.quantile(0.75)

    return q_three - q_one

def quart_set2(data):

    scores = data[data['Set'] == 2]['Score']

    q_one = scores.quantile(0.25)
    q_three = scores.quantile(0.75)

    return q_three - q_one

def side_by_side(set1, set2):
    bins = range(30, 81, 5)

    plt.hist([set1, set2], bins=bins, 
             label=['Set 1', 'Set 2'], 
             edgecolor='black', 
             alpha=0.7, 
             histtype='bar', 
             rwidth=0.9)

    plt.xlabel('Score')
    plt.ylabel('Frequency')
    plt.title('Set 1 vs. Set 2')
    plt.legend()
    plt.show()


sns.boxplot(x='Set', y='Score', data=data)
plt.title('Boxplot of Score by Set')
plt.show()



print(f"The mean score is: {mean(data)}")
print(f"The median score is: {median(data)}")
print(f"The standard deviation is: {std_dev(data)}")
print(f"The variance of the scores is: {variance(data)}")
print(f"The range of the scores is: {rnge(data)}")
print(f"The interquartile range of the data is: {intquart(data)}")
set1(data)
set2(data)
print(f"Quantile Set 1: {quart_set1(data)}")
print(f"Quantile Set 2: {quart_set2(data)}")
side_by_side(data[data['Set'] == 1]['Score'], data[data['Set'] == 2]['Score'])

plt.hist(
    data['Score'],
        bins=10, 
        weights=np.ones_like(data['Score']) / len(data['Score'])*100,
        color='skyblue',
        edgecolor='black'
    )
plt.title('Percent Frequency Histogram of Score')
plt.xlabel('Score')
plt.ylabel('Percent')
plt.show()





