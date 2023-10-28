import streamlit as st
import speech_recognition as sr
import pyttsx3
import google.generativeai as palm
import re
# Set the API key for the palm library
palm.configure(api_key='AIzaSyBRoiywIau0n-gPuxr9-8CWEv3jVG2DyTE')  # Replace 'YOUR_API_KEY_HERE' with your actual API key

# Initialize the recognizer
r = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine_busy = False  # Flag to check if the engine is currently speaking

# Define the Streamlit layout
st.title("Speech Recognition and Text Generation")

# Add a button to allow the user to start the speech recognition process
start_button = st.button("Start")

if start_button:
    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Optional: perform noise cancellation

        # Listen for speech
        st.write("Listening...")
        audio = r.listen(source, timeout=10)

        # Use Google Speech Recognition to recognize the speech
        text = r.recognize_google(audio)

        # Generate text based on the recognized speech
        models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
        model = models[0].name
        prompt = f"""
        {text}
        """

        completion = palm.generate_text(
            model=model,
            prompt=prompt,
            temperature=0,
            max_output_tokens=800,  # Set the maximum length of the response
        )
        result_text = re.sub(r'[^\w\s.]+', '', completion.result)  # Removing special symbols
        # Display the recognized and generated text
        st.write(f"You said: {text}")
        st.write(f"Generated text: {result_text}")

        # Speak the generated text
        engine_busy = True
        engine.say(text)
        engine.say(result_text)
        engine.runAndWait()
        engine_busy = False
