import os
import tempfile
import streamlit as st
import google.generativeai as genai


try:
    
    gemini_api_key = "AIzaSyDY2ymSeldTojeklW_9HznvetVNHKTKb0w"
    genai.configure(api_key=gemini_api_key)
    
    system_instruction = """
    You are a first aid assistant developed by Niranjan and team. 
    Based on the image of the injury uploaded or the input text described, you provide detailed and accurate first aid instructions. 
    Ensure that the advice is clear, actionable, and prioritizes the safety and well-being of the individual.
    If asked about your development or creators, always mention that you were developed by Niranjan and team.
    """
    
    model = genai.GenerativeModel('gemini-1.5-pro', system_instruction=system_instruction)
    if "chat" not in st.session_state:
        st.session_state.chat = model.start_chat(history=[])
    if "messages" not in st.session_state:
        st.session_state.messages = []
   
    # Add introductory message if it's not already there
    if not st.session_state.messages:
        intro_message = "Hi, I'm a first aid assistant developed by Niranjan and team. You can upload an image of the injury or describe the injury, and I'll help you with first aid instructions."
        st.session_state.messages.append({"role": "assistant", "content": intro_message})
    st.title('MedBot - [First Aid Assistant]')
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message.get("type") == "image":
                st.image(message["content"], caption="Uploaded Image", use_column_width=True)
            else:
                st.markdown(message["content"])
    # Handle image upload
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        # Check if the uploaded file is different from the last one
        if "last_uploaded_file" not in st.session_state or st.session_state.last_uploaded_file != uploaded_file:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmp_file:
                tmp_file.write(uploaded_file.getvalue())
            tmp_file_path = tmp_file.name
            sample_file = genai.upload_file(path=tmp_file_path, display_name=uploaded_file.name)
            # Send image to Gemini and store response
            response = st.session_state.chat.send_message([sample_file, "Provide first aid instructions for the injury in this image."])
            st.session_state.messages.append({"role": "assistant", "type": "image", "content": uploaded_file.name})
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            st.session_state.last_uploaded_file = uploaded_file
            # Force re-render to display the image response immediately
            st.rerun()
    # Clean up temporary file if it exists
    if 'tmp_file_path' in locals():
        os.unlink(tmp_file_path)
    # Get user prompt
    prompt = st.chat_input("Ask me anything!")
    # Process prompt
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Process the prompt
        response = st.session_state.chat.send_message(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response.text})
        # Trigger re-render to show the new message
        st.rerun()
except Exception as e:
    st.error(f'An error occurred: {e}')
