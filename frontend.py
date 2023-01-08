# import openai
# import streamlit as st
# import requests
# import json
# from streamlit_chat import message
# from dotenv import dotenv_values
# import requests
# from streamlit_option_menu import option_menu

# dotenv=dotenv_values()
# api_key=dotenv.get("API_KEY")
# api_endpoint1="http://localhost:8000/login"
# api_endpoint2="http://localhost:8000/signup"



# # Set your API key
# openai.api_key = api_key

# import streamlit as st

# expiration_time = 3600  # 1 hour





# def generate_response(prompt):
#     # Set the API endpoint
#     api_endpoint = "https://api.openai.com/v1/completions"
#     # api_key = openai.api_key
    
#     # Set the headers for the request
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {api_key}"
#     }
    
#     # Set the payload for the request
#     data = {
#         "model":"text-davinci-003",
#         "prompt": prompt,
#         "max_tokens": 1024,
#         "temperature": 0.5,
#         "top_p": 1,
#         "frequency_penalty": 0,
#         "presence_penalty": 0,
#         # "top_p":1,
#         # "frequency_penalty":0
#     }
    
#     # Send the request
#     response = requests.post(api_endpoint, headers=headers, json=data)
    
#     # Check the status code of the response
#     if response.status_code == 200:
#         # Parse the response
#         response_json = response.json()
#         # Get the completion from the response
#         completion = response_json["choices"][0]["text"]
#         return completion
#     else:
#         # Return the error message
#         return response.text




# def signup(email,password):
#     api_endpoint=api_endpoint2
#     headers={"Content-Type": "application/json"}
#     data={
#         "email":email,
#         "password":password,
        
#     }
#     response = requests.post(api_endpoint,headers=headers, data=json.dumps(data))
#     if response.status_code==200:
#         # return response.json()["id"]
#         return st.success("you have created an account with us , please kindly sign in ")
        
#     else:
#         return st.error(response.text)



# login_successful=False

# # check if user is logged in
# @st.cache
# def get_access_token():
#     return ('access_token')
# if get_access_token() is not None:
#     login_successful=True

# # Display login/signup form until form is completed


# while not login_successful:
#     with st.container():
#         st.write(""" 
#     # Welcome to Dr Melvis,  a smart health diagonistic chatbot .

#     we made this bot to meet your everyday health diagnoinsis. to use the bot, you would have to sign in or create an account with us 

#     """)
#         email = st.text_input("Email", type="default", key="email",)
#         password = st.text_input("Password", type="password", key="password")
#         bet1 = st.button("Sign In", key="sign_in_key")
#         if bet1:
#             headers={"content-Type":"application/json"}
#             data={
#                 "username":email,"password":password
#             }
#             response=requests.post(api_endpoint1,headers=headers,json=data)
#             login_successful=True if response.status_code ==200 else False
#             if login_successful:
                
#                 access_token =response.json()["access_token"]
#                 cookie_params=f"access_token={access_token}; Expires={expiration_time}"
                
#             else:
#                 st.write(response.text)
                


        
#         with st.sidebar:
#             st.write( """ # SIGN UP TO HAVE AN ACCOUNT WITH US """)
#             email = st.text_input("Email", type="default", key="email1")
#             password = st.text_input("Password", type="password", key="pwd")
#             comfirm_password = st.text_input("Confirm Password", type="password", key="pwd2")
#             signup_button = st.button("Register")
#             if signup_button:
#                 signup_result = signup(email=email, password=password)
#                 if signup_result != "Success":
#                     st.write(signup_result)
#                 else:
                    
#                     form_completed = True 
#     break 
                                     
                

# ########################### main bot interface ###############################33
# if login_successful:
#     st.title("Dr Melvis Health Diagnostic Chatbot")

#     DEFAULT_RESPONSE = "Hello, my name is Dr. Melvis, i am a health diagnonistic chatbot bult by Anolue Francis and Zainab. i am here to help with all your healthcare service and also help dianoise a well detailed symptom explaination to the best of my ability?"

# # Display the default response in the chat interface
#     message(DEFAULT_RESPONSE, key='message_default')

# # Storing the chat
#     if "generated" not in st.session_state:
#         st.session_state["generated"] = []

#     if "past" not in st.session_state:
#         st.session_state["past"] = []

# # Get user input


#     st.empty()
#     def get_text():
#         input_text = st.text_input("you: Enter a text", key="input")
#         return input_text

#     user_input = get_text()


#     if user_input:
#         output = generate_response(user_input)
#     # Store the output
#         st.session_state["past"].append(user_input)
#         st.session_state["generated"].append(output)
#         st.empty()

#     if st.session_state["generated"]:
#         for i in range(len(st.session_state["generated"]) - 1, -1, -1):
#             message(st.session_state["generated"][i], key='message'+str(i))
#             message(st.session_state["past"][i], is_user=True, key=str(i) + "user")



# #option menu

