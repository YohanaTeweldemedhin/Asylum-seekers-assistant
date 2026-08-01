import streamlit as st
from rag import ask_question

st.title("🇮🇪 Dublin Law Assistant")

question = st.text_input(
    "Ask a question about the Dublin Regulation"
)

if st.button("Ask"):

    answer, pages = ask_question(question)

    st.write("### Answer")
    st.write(answer)

    st.write("### Sources")

    for page in pages:
        st.write(f"Page {page}")