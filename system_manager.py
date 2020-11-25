# This script is used to manage all parts of the project modules.
# STT class used for using Google Speech-To-Text API  

import io
import os
from mic import main as micm # import from mic.py
from write import main as writem # import from write.py 

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.protobuf.json_format import MessageToDict, MessageToJson

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# Note,  the SpeechClassAPI-1612.json file (Google API credentials)
#  should be in the same folder as a current python script
credential_path = os.path.join(APP_ROOT, 'SpeechClassAPI-1612.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
tshift = 0.15

class STT():
    def __init__(self):        
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code='iw-IL',
            enable_word_time_offsets=True)            
        self.sttclient = speech.SpeechClient()

    def opensoundfile(self, file_name):    
        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = speech.RecognitionAudio(content=content)
        return audio

    def recognize(self,audio):
        # Detects speech in the audio file and return results to caller
        return self.sttclient.recognize(self.config, audio)

    def parse_result(self,result):
        data=''        
        for result in result.results:
            alternative = result.alternatives[0]
            print('Transcript: {}'.format(alternative.transcript))
            data = alternative.transcript           
        return data


def main(fname):
    # run mic.py module for recording 3 sec audio 
    micm(fname)
    # Init Google API supported class
    st= STT()
    audio=st.opensoundfile(fname)
    # Sending audio to STT API
    print('Opened request to Google API..')
    rz=st.recognize(audio)
    print('Received API responce')    
    data = st.parse_result(rz) 
    print(data) 
    # Sending recognized data to write module (write.py) 
    writem(data)


if __name__ == '__main__':
    print('Started Manager..')
    main('speech.wav')
    print('Manager stopped')
    