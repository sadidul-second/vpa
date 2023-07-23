from banglatts import BanglaTTS
import pygame

tts = BanglaTTS(save_location="save_model_location")
path = tts("এবাংলায় কথা বলতে পান্ড।", voice='female', filename='1.wav')  # voice can be male or female

pygame.mixer.init()
my_sound = pygame.mixer.Sound('1.wav')
my_sound.play()
pygame.time.wait(int(my_sound.get_length() * 1000))
