import json
import streamlit as st
from streamlit_lottie import st_lottie
col1, col2 = st.columns(2)
with col1:

    st.markdown("""## Linear Search by Sudhanshu""")


def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)



with col1:
    lottie_now = load_lottiefile("file/code.json")
st_lottie(
    lottie_now,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    height=400,
    key=None,

)
st.success(
    "Enter the element of list separated by spaces ")
Sudhuu = list(map(int, st.text_input("").strip().split()))
st.success("Enter the element you want to find ")
key = int(st.text_input(" "))

for i in range(len(Sudhuu)):
    if Sudhuu[i] == key:
        st.success(f"Searched element found at Possition {i+1}.")
        break
else:
    st.success("Searched element is not found in the list.")
