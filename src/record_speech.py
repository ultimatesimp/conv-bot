import pyaudio
import wave
import msvcrt
import time

chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 3
filename = "wav_files/output.wav"

p = pyaudio.PyAudio()  # Create an interface to PortAudio

print('Recording')

stream = p.open(format=sample_format,
                channels=channels,
                rate=fs,
                frames_per_buffer=chunk,
                input=True)

frames = []  # Initialize array to store frames

""" # Store data in chunks for 3 seconds
for i in range(0, int(fs / chunk * seconds)):
    data = stream.read(chunk)
    frames.append(data) """

print("Press Enter to start recording. Press Enter again to stop...")

# Wait for the first Enter key press to start recording
while True:
    if msvcrt.getch() == b'\r':
        break

print("Recording. Press Enter to stop...")

# Record audio until Enter is pressed again
start_time = time.time()
while True:
    data = stream.read(chunk)
    frames.append(data)
    if msvcrt.kbhit() and msvcrt.getch() == b'\r':
        break

# Stop and close the stream 
stream.stop_stream()
stream.close()
# Terminate the PortAudio interface
p.terminate()

print('Finished recording')

# Save the recorded data as a WAV file
wf = wave.open(filename, 'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()