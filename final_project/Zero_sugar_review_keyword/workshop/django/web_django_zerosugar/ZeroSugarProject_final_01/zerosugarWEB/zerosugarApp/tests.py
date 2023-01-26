from django.test import TestCase

# Create your tests here.
# pip install pandas
import pandas as pd


zerosugar = pd.read_csv('C:/Users/ohans/Desktop/multicampus/big data/class/project/final project/cider/bootstrap/zerosugar.csv', encoding='cp949')

print(zerosugar)