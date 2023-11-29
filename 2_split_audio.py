from pydub import AudioSegment
import os

# PyDub handles time in milliseconds
ten_minutes = 10 * 60 * 1000

print("start analyzing song:")
song = AudioSegment.from_file(os.path.join(os.getcwd(), 'tmp', 'output.mp4'))

audio_length = len(song)
for i in range(0, audio_length, ten_minutes):
	if i + ten_minutes > audio_length:
		print(f"last chunk started from {i/(ten_minutes / 10)}min")
		part = song[i:]
	else:
		print(f"chunk started from {i/(ten_minutes / 10)}min to {(i+ten_minutes)/(ten_minutes / 10)}")
		part = song[i:i+ten_minutes]

	print("chunk exporting")
	part.export(os.path.join(os.getcwd(), "tmp", f"part_output_{i}.mp3"), format="mp3")
	print("chunk exported")
