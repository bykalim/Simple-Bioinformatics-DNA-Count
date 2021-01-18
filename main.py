import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count("A")),
        ("T", seq.count("T")),
        ('G', seq.count("G")),
        ("C", seq.count("C")),
    ])
    return d


st.write("""
# DNA Nucleotide Count Web App

This app counts the nucleotide compositions of query DNA!
""")

sample = "DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
st.sidebar.header('Enter DNA Sequence')
sequence = st.sidebar.text_area('Sequence Input', sample, height=300)

st.subheader("**Inputted DNA**")
sequence = sequence.splitlines()
st.write(sequence)
sequence = sequence[1:]

st.subheader("**Clean Data**")
st.write(sequence)
sequence = "".join(sequence)

st.subheader("**Join Sequences**")
st.text_area("", sequence, height=150)

result = DNA_nucleotide_count(sequence)

st.subheader("**Dictionary**")
st.write("""
- There are {A} adenine (A) \n
- There are {T} thymine (T) \n
- There are {G} adenine (guanine) \n
- There are {C} thymine (cytosine  
""".format(
    A=result['A'],
    T=result['T'],
    C=result['C'],
    G=result['G'],
))

st.subheader("**DataFrame**")
dataFrame = pd.DataFrame.from_dict(result, orient='index')
dataFrame = dataFrame.rename({0: 'count'}, axis='columns')
dataFrame.reset_index(inplace=True)
dataFrame = dataFrame.rename(columns={"index": "nucleotide"})
st.write(dataFrame)
