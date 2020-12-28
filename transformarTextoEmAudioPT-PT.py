from gtts import gTTS
from playsound import playsound

def tocarVoz(voz):
    playsound(voz)

def converterParaAudio(texto):
    voz = gTTS(texto, lang='pt')
    voz.save('voz.mp3')
    tocarVoz('voz.mp3')

vozParaConverter = input('Digite algo para virar audio: \n')
converterParaAudio(vozParaConverter)

