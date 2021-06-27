import streamlit as st
import numpy as np

arr = np.random.randint(1,10, size=[3,3,3])

for a in arr:
    for b in a:
        for c in b:
            print(c,end=' ')
        print()
    print()
