from pydub import AudioSegment
from pydub.playback import play








import glob

orig = AudioSegment.silent(duration=1000)
for wav in sorted(glob.glob("*.wav")):
    if not "6" in wav and not ("A" not in wav and "B" not in wav and "5" in wav):
        print(wav)
        audio_in_file = "in_sine.wav"
        audio_out_file = "out_sine.wav"

        # create 1 sec of silence audio segment
        one_sec_segment = AudioSegment.silent(duration=1000)  #duration in milliseconds

        #read wav file to an audio segment
        song = AudioSegment.from_wav(wav)

        #Add above two audio segments    
        orig += (song + one_sec_segment)

        #Either save modified audio
orig.export(audio_out_file, format="wav")

input()