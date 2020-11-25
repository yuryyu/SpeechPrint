
# reference: https://makersportal.com/blog/2018/8/23/recording-audio-on-the-raspberry-pi-with-python-and-a-usb-microphone
# This script used for recording 3 sec of speech.
# Matched  for usb connected Paspberry Pi mic 

import pyaudio
import wave

form_1 = pyaudio.paInt16 # 16-bit resolution
chans = 1 # 1 channel
samp_rate = 44100 # 44.1kHz sampling rate
chunk = 4096 # 2^12 samples for buffer
record_secs = 3.0 # seconds to record
# TODO: add check for device index for current OS (Raspberry Pi)
# >>> for ii in range(p.get_device_count()):
# >>>     print(p.get_device_info_by_index(ii).get('name')) 
# find with "USB" start patern 
dev_index = 0 # device index found by p.get_device_info_by_index(ii)

def main(wav_output_filename):
    audio = pyaudio.PyAudio() # create pyaudio instantiation

    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    print("recording..")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()

if __name__=='__main__':
    # This part of code is used for module debugging 
    wav_output_filename = 'speech.wav' # name of .wav file
    print('Start recording for 3 seconds')
    main(wav_output_filename)
    print('Recorded speech.wav file')