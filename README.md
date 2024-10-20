# python-project-Jarvis
Jarvis - AI Virtual Assistant A Python-based virtual assistant inspired by Jarvis that listens to voice commands and performs tasks such as opening websites, playing music, reading news, and interacting with OpenAI's GPT model to answer user queries.

Features:
1) Voice Command Recognition: Listens for the wake word "Jarvis" and responds to commands.
2) Website Navigation: Opens websites like Google, YouTube, Facebook, LinkedIn, etc.
3) Music Player: Plays predefined songs from YouTube using voice commands.
4) News Reader: Fetches and reads the latest news headlines from Pakistan using NewsAPI.
5) OpenAI Integration: Handles queries using the OpenAI API (ChatGPT model).
6) Text-to-Speech (TTS): Uses Google Text-to-Speech (gTTS) and Pygame for audio output.

Prerequisites:
 Make sure you have the following installed on your system:
  1) Python 3.x
  2) Required Python libraries:
      Install the dependencies by running:
        bash
            pip install speechrecognition pyttsx3 requests openai gtts pygame
  3) Microphone Access: Ensure your microphone is working properly for speech recognition.
Usage Instructions:
  1) Wake the Assistant:
     Say "Jarvis" to activate the virtual assistant.
  2) Available Commands:
     "Open Google" - Opens Google in your browser.
     "Play song1" - Plays a predefined YouTube song.
     "News" - Reads the latest news from Pakistan.
     Other queries: Ask anything, and the response is generated using OpenAI GPT.
  3) Stop the Program:
  Use Ctrl + C in the terminal to exit.
