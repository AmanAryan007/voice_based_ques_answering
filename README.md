# voice_based_ques_answering
# Speech Recognition and Text Generation App

This application uses Google's speech recognition and text-to-speech technology, along with the Generative AI from Google, to recognize the user's speech, generate text based on the speech, and then speak the generated text.

## Setup

1. Install the required Python packages by running:
pip install streamlit speech_recognition pyttsx3 google

2. Get the necessary API key for the palm library from Google. Replace 'YOUR_API_KEY_HERE' with your actual API key in the code.

## Running the Application

You can run the application using the following command:
streamlit run your_script_name.py


## Functionality

1. Click the "Start" button to begin the speech recognition process.

2. Speak into the microphone when prompted.

3. The application will recognize your speech, generate text based on it, and then read the generated text aloud.

4. The special characters in the generated text, except for periods and commas, are removed for better readability.

## Additional Information

- The application includes a stop button to terminate all running processes.
- Ensure that your microphone is working properly and that you are in a quiet environment for accurate speech recognition.

## Requirements

- Python 3.6+
- Streamlit
- SpeechRecognition
- pyttsx3
- google


