import streamlit as st
import subprocess

# Language mapping dictionary
LANGUAGE_MAPPING = {
    'bn-IN': 'Bengali',
    'en-IN': 'English',
    'gu-IN': 'Gujarati',
    'hi-IN': 'Hindi',
    'kn-IN': 'Kannada',
    'ml-IN': 'Malayalam',
    'mr-IN': 'Marathi',
    'od-IN': 'Odia',
    'pa-IN': 'Punjabi',
    'ta-IN': 'Tamil',
    'te-IN': 'Telugu'
}

# Streamlit app title
st.title("LiveKit Call Interface")

# Phone number input
phone_number = st.text_input("Enter Phone Number", placeholder="+91XXXXXXXXXX")

# Language selection dropdown
language_options = list(LANGUAGE_MAPPING.keys())
language_display = [f"{LANGUAGE_MAPPING[lang]} ({lang})" for lang in language_options]
selected_language_display = st.selectbox("Select Language", language_display)
selected_language = language_options[language_display.index(selected_language_display)]

# Call button
if st.button("Call"):
    if phone_number and selected_language:
        # Construct the command
        command = f'lk dispatch create --new-room --agent-name "teliphonic-rag-agent" --metadata "{phone_number},{selected_language}"'
        
        try:
            # Execute the command
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            
            if process.returncode == 0:
                st.success("Call initiated successfully!")
                st.text("Command output:")
                st.text(stdout.decode())
            else:
                st.error("Error initiating call:")
                st.text(stderr.decode())
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter both phone number and select a language.") 