import streamlit as st
import numpy as np
import pandas as pd

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]

    for i, h in enumerate(concepts):
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "No":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'

    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    
    return specific_h, general_h

def main():
    st.title("Candidate Elimination Algorithm")

    # File uploader for training data
    st.sidebar.header("Upload Training Data")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.write("### Training Data :")
        st.write(data)

        # Separating concept features from Target
        concepts = np.array(data.iloc[:, :-1])
        target = np.array(data.iloc[:, -1])

        # Apply learn function
        s_final, g_final = learn(concepts, target)

        # Display final hypotheses
        st.write("### Final Hypotheses :")
        st.write("Final Specific hypotheses :", s_final)
        st.write("Final General hypotheses :", g_final)

if __name__ == "__main__":
    main()
