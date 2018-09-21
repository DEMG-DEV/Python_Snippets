# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that you want to convert to audio
mytext = 'Hola Nancy, Te Amo Muchisimo'

# Language in wich you want to convert
language = 'es'

# Passing the text and languages to the engine,
# here we have marked slow=False. Wich tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
#os.system("mpg321 welcome.mp3")

""" import vlc
import time

instance = vlc.Instance()

#Create a MediaPlayer with the default instance
player = instance.media_player_new()

#Load the media file
media = instance.media_new('welcome.mp3')

#Add the media to the player
player.set_media(media)

#Play for 10 seconds then exit
player.play()
time.sleep(10)
 """