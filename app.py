


import streamlit as st 
import os 
import google.generativeai as genai

G_KEY="AIzaSyDBEODtIR1Xgf61j-TXjhJe9QAmGp-9dUY"
genai.configure(api_key="G_KEY")

##FUNCTION TO LOAD GEMINI PRO MODEL AND GET RESPONSE
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
  response=model.generate_content(question)
  return response


##INITIALIZE OUR STREAMLIT APP
st.set_page_config(page_title="Q&A Demo", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
st.header("Gemini LLM Application")

input=st.text_input("input:",key="input")
submit=st.button("Ask the question")

##WHEN SUBMIT BUTTON IS CLICKED

if submit:
  response=get_gemini_response(input)
  st.subheader("The Response is")
  st.write(response)