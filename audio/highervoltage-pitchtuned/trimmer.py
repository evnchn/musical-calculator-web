
from pydub import AudioSegment
from pydub.silence import detect_leading_silence

def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=1):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms
#sound = AudioSegment.from_file(file_path_here)
#stripped = strip_silence(sound)
        
        
import glob

for waves in glob.glob("*.wav"):
    sound = AudioSegment.from_file(waves)
    start_trim = detect_leading_silence(sound)
    print(start_trim)
    
    #remove_sil(waves, f"fixed-{waves}")
    #stripped = strip_silence(sound)
    trimmed_sound = sound[start_trim:]
    trimmed_sound.export(f"fixed-{waves}", format='wav')
    

    