# Azure_TTS_Script_Reader
Generates a bunch of .wav files based off of the text you want to turn into speech.

Setup using the steps here: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech?tabs=windows%2Cterminal&pivots=programming-language-python

This library handles the Azure key by putting it into config\passwords.json

Make sure to copy passwords.example.json and create a passwords.json from it

Usage:  python -m src.generate_tts_for_json_script

