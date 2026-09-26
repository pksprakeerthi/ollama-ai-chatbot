import streamlit as st
import ollama

st.title("Welcome AI Chatbot")

question = st.text_input("Enter a prompt")

if st.button("Send"):

    if question.strip() == "":
        st.warning("Please enter a question")

    else:
        st.success("Entered successfully")

        try:
            response = ollama.generate(
                model="llama3.2",
                prompt=question
            )

            st.write("### AI Response")
            st.write(response["response"])

        except Exception as e:
            st.error("Something went wrong!")
            st.exception(e)