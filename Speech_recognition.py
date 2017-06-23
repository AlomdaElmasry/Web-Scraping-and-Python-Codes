import speech_recognition as sr
import pyaudio
import wave
from bs4 import BeautifulSoup
import urllib2
import os

def record_audio():

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 6
    WAVE_OUTPUT_FILENAME = "text.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print "recording..."
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print "finished recording"

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    return WAVE_OUTPUT_FILENAME


def get_text():

    x = record_audio()
    AUDIO_FILE = x

    # use the audio file as the audio source
    r = sr.Recognizer()

    with sr.AudioFile(AUDIO_FILE) as source:
        audio = r.record(source)  # read the entire audio file

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"


def play_song():
    text = get_text().split()
    final_text = ' '.join(text[1:])
    print final_text

    query = final_text.lower()
    quoted_query = urllib2.quote(query)

    url = "https://www.youtube.com/results?search_query=" + quoted_query
    # print url

    # add header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}

    request = urllib2.Request(url, headers=headers)
    data_file = urllib2.urlopen(request)
    data_html = data_file.read()
    data_file.close()

    soup = BeautifulSoup(data_html, 'html.parser')

    title = []
    ref = []

    h3 = soup.find("h3", attrs={"class": "yt-lockup-title"})
    link = h3.find('a')['href']
    video_url = "https://www.youtube.com" + link
    print video_url
    os.system("vlc " + video_url)


if __name__ == "__main__":
    play_song()