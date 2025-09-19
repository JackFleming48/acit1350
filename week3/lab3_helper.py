import pandas as pd


trump = "trump.txt"
trud = "trud.txt"

with open(trud, "r") as f:
    data_trud = f.read().split(",")

with open(trump, "r") as f:
    data_trump = f.read().split(",")

jus = pd.Series([float(x) for x in data_trud])
don = pd.Series([float(x) for x in data_trump])


def mean(data):
    return data.mean()

def median(data):
    return data.median()

def std_dev(data):
    return data.std()

def variance(data):
    return data.var()

def rnge(data):
    return data.max() - data.min()

def intquart(data):

    q_one = data.quantile(0.25)
    q_three = data.quantile(0.75)

    return q_three - q_one

def sandi_cameron_cv():
    sandi_pph = 23
    sandi_dev = 1.91
    cameron_pph = 41
    cameron_dev = 2.12

    print(f"Sandi: {(sandi_dev/sandi_pph)*100}")
    print(f"Cameron: {(cameron_dev/cameron_pph)*100}")

sandi_cameron_cv()