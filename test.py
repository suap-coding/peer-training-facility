import streamlit as st
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np

arr = np.random.randint(1,10, size=[3,3,3])

a = np.array ([1,2,3,4,5])
print (a)



for a in arr:
    for b in a:
        for c in b:
            print(c,end=' ')
        print()
    print()
