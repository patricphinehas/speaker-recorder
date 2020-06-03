from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.output
import os

import librosa.display

music_path = os.environ["HOME"]
music_path = music_path + "/Music"
# mp3file = "audio.mp3"
mp3file = music_path + "/" + str(input("enter the song name")) +".mp3"

y, sr = librosa.load(mp3file, duration=120)


# And compute the spectrogram magnitude and phase
S_full, phase = librosa.magphase(librosa.stft(y))

S_filter = librosa.decompose.nn_filter(S_full, aggregate=np.median, metric='cosine', width=int(librosa.time_to_frames(2, sr=sr)))

S_filter = np.minimum(S_full, S_filter)

margin_i, margin_v = 2, 10
power = 2

mask_i = librosa.util.softmask(S_filter, margin_i * (S_full - S_filter), power=power)

mask_v = librosa.util.softmask(S_full - S_filter, margin_v * S_filter, power=power)

S_foreground = mask_v * S_full
S_background = mask_i * S_full


new_y = librosa.istft(S_foreground*phase)
music= librosa.istft(S_background*phase)
librosa.output.write_wav("./voice.wav", new_y, sr)
librosa.output.write_wav("./music.wav", music, sr)



