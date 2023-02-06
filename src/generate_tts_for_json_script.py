import json
import time

from src.app.config import Config
from src.app.tts_file_generator import TTSFileGenerator


def generate_next_file(filename):
    if len(data) == 0:
        return

    # This delay is necessary so we don't hit request limits for Azure
    time.sleep(2.5)

    item = data.pop(0)
    text = item['text']
    sound = item['sound']

    # call the generate_file_for_text function and pass the text and sound value as old_json_file
    tts_generator = TTSFileGenerator(config)
    tts_generator.generate_file_for_text(text, generate_next_file, filename=sound)


config = Config('test')
json_file = '.\\content\\script-test.json'

# Read in the content of the .json file
with open(json_file, 'r') as json_file:
    data = json.load(json_file)

generate_next_file("")
