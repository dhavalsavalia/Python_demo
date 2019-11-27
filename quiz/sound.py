from pydub import AudioSegment
from pydub.playback import play

fname = "fails.wav"
mysong = AudioSegment.from_wav(fname)
play(mysong)