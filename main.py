import os

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_vision_response,
                            gemini_pro_response)

# Get the working directory everytime we run file
working_dir = os.path.dirname(os.path.abspath(__file__))

# Setting page configuration
st.set_page_config(
    page_icon="💡",
    page_title="Custom Gemini AI",
    layout= "centered"
) 

with st.sidebar:
    selected = option_menu(
        menu_title="Gemini AI",
        options=["ChatBot", "Visual Storyteller","Question Hub"],
        menu_icon= "robot",
        icons=["chat-left-quote-fill", "file-earmark-image","code-square", "patch-question-fill"],
        default_index=0
    )

# Function to translate role betweem gemini pro and streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"  
    else:
        return user_role
   

# ChatBot Page 
if selected == "ChatBot":
    model = load_gemini_pro_model()
    
    # Initialize chat session in streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = model.start_chat(history=[])
    
    # Page title
    st.title("Custom Gemini ChatBot 🤖")
    
    #display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)
            
    # input field for user's message
    user_prompt = st.chat_input("Ask Gemini-Pro...")
    
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)
        
        gemini_resposne = st.session_state.chat_session.send_message(user_prompt)
        
        # Display response
        
        with st.chat_message("assistant"):
            st.markdown(gemini_resposne.text)
            



# Image Captioning Page
if selected == "Visual Storyteller":
    st.title("Visual Storyteller 📸")
    
    upload_image = st.file_uploader("Upload an Image..", type=["jpg", "png", "jpeg"])
    
    if st.button("Generate Caption"):
        
        image = Image.open(upload_image)
        
        col1 , col2 = st.columns(2)
        
        with col1:
            resized_image = image.resize((800, 500))
            st.image(resized_image)
            
        default_prompt = "Describe this image in a few words."
        
        # Getting the vision pro respone
        caption = gemini_pro_vision_response(default_prompt, image)
        
        with col2:
            st.info(caption)
            
            
# Text Embedding Page
#if selected == "Embed text":
    
    #st.title("Text Embeddings 🔠")
    
    # Text to embedding
    #input_text = st.text_area(
        #label="",
        #placeholder="Enter the text to get embeddings")
    
    #if st.button("Get Embeddings"):
        #response = embeddings_model_response(input_text)
        #st.markdown(response)
    
    
# Ask me anything Page
if selected == "Question Hub":
    
    st.title("Question Hub")
    
    user_prompt = st.text_area(
        label="",
        placeholder="Question Hub")
    
    if st.button("Get answer"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)
        