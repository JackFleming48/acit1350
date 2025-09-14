import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def serv1():
    s1 = pd.read_csv(
        'Server1Data.txt',
        sep='\t',
        skiprows=3
    )

    return s1

def serv2():
    s2 = pd.read_csv( 'Server2Data.txt', sep='\t', skiprows=3)

    return s2

print(serv1().head())
print(serv2().head())

def create_histogram(server1, server2):
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    sns.histplot(server1['Time'], bins=20)
    plt.title('Server 1 Download Times')
    plt.xlabel('Time (seconds)')

    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    sns.histplot(server2['Time'], bins=20)
    plt.title('Server 2 Download Times')
    plt.xlabel('Time (seconds)')

    plt.tight_layout()
    plt.show()

def compute_mean(server1, server2):
    mean1 = server1['Time'].mean()
    mean2 = server2['Time'].mean()
    
    print(f'Server 1 mean: {mean1:.2f} seconds \nServer 2 mean: {mean2:.2f} seconds')

create_histogram(serv1(), serv2())
print(compute_mean(serv1(), serv2()))