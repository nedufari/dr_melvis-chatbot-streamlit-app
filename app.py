import openai
import streamlit as st
import requests
import json
from streamlit_chat import message
import os 



# Set your API key
api_key=openai.api_key ='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'





def generate_response(prompt):
    # Set the API endpoint
    api_endpoint = "https://api.openai.com/v1/completions"
    # api_key = openai.api_key
    
    # Set the headers for the request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Set the payload for the request
    data = {
        "model":"text-davinci-003",
        "prompt": prompt,
        "max_tokens": 1024,
        "temperature": 0.5,
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        # "top_p":1,
        # "frequency_penalty":0
    }
    
    # Send the request
    response = requests.post(api_endpoint, headers=headers, json=data)
    
    # Check the status code of the response
    if response.status_code == 200:
        # Parse the response
        response_json = response.json()
        # Get the completion from the response
        completion = response_json["choices"][0]["text"]
        return completion
    else:
        # Return the error message
        return response.text



st.title("Dr Melvis Health Diagnostic Chatbot")

DEFAULT_RESPONSE = "Hello, my name is Dr. Melvis, i am a health diagnonistic chatbot bult by Anolue Francis and Zainab. i am here to help with all your healthcare service and also help dianoise a well detailed symptom explaination to the best of my ability?"

# Display the default response in the chat interface
message(DEFAULT_RESPONSE, key='message_default')

# Storing the chat
if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []

# Get user input


st.empty()
def get_text():
    input_text = st.text_input("patient", key="input")
    return input_text

user_input = get_text()


if user_input:
    output = generate_response(user_input)
    # Store the output
    st.session_state["past"].append(user_input)
    st.session_state["generated"].append(output)
    st.empty()

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key='message'+str(i))
        message(st.session_state["past"][i], is_user=True, key=str(i) + "user")