import azure.cognitiveservices.speech as speechsdk
from src.app.config import Config


class TTSFileGenerator:

    def __init__(self, config: Config):
        self.text = ""

        # Speech config
        self.language = "en"
        self.speech_config = speechsdk.SpeechConfig(subscription=config.get("azure-tts-key"), region='eastus')
        self.speech_config.speech_synthesis_voice_name = 'en-GB-RyanNeural'
        self.default_ssml = """<speak version='1.0' xml:lang='en-US' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts'>
            <voice name='en-GB-RyanNeural'>
                <prosody rate="{speech_rate}%" pitch="{speech_pitch}%">
                    <mstts:express-as style="{speech_style}" styledegree="1">
                        {text}
                    </mstts:express-as>
                </prosody>
            </voice>
        </speak>"""

        self.on_complete_callback = None

    def on_complete(self, result, filename):
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            # print("Speech synthesized for text [{}]".format(text))
            print("Created: " + filename)
        elif result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = result.cancellation_details
            print(filename + " Failed")
            print(filename + " Speech synthesis canceled: {}".format(cancellation_details.reason))
            if cancellation_details.reason == speechsdk.CancellationReason.Error:
                if cancellation_details.error_details:
                    print(filename + " Error details: {}".format(cancellation_details.error_details))
        else:
            print(filename + " Failed")
            print(str(result.reason))

        self.on_complete_callback(filename)

    def generate_file_for_text(self, text, on_complete_callback, filename, speech_rate=-13, speech_pitch=-5.5, speech_style="neutral"):
        self.text = text

        self.on_complete_callback = on_complete_callback

        audio_config = speechsdk.audio.AudioOutputConfig(filename=filename)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=audio_config)

        text = text.replace('&', " and ")
        ssml_string = self.default_ssml.replace("{text}", text)
        ssml_string = ssml_string.replace("{speech_rate}", str(speech_rate))
        ssml_string = ssml_string.replace("{speech_pitch}", str(speech_pitch))
        ssml_string = ssml_string.replace("{speech_style}", speech_style)
        result = speech_synthesizer.speak_ssml_async(ssml_string).get()
        self.on_complete(result, filename)

        return filename



