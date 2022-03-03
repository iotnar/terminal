import pygame as pg
import sys
import pyttsx3
tts = pyttsx3.init()



pg.mixer.pre_init
pg.init()
pg.mixer.music.load('elektro.wav')
pg.mixer.music.play()

zagruzka = pg.mixer.Sound('vkluchenie.wav')
#priv1 = pg.mixer.Sound('voxworker-voice-file.mp3')
priv2 = pg.mixer.Sound('fraza2.mp3')
priv3 = pg.mixer.Sound('fraza3.mp3')
klik = pg.mixer.Sound('klik.wav')

def count_lines(filename, chunk_size=1<<13):
    with open(filename) as file:
        return sum(chunk.count('\n')
                   for chunk in iter(lambda: file.read(chunk_size), ''))
j = count_lines('text.txt')+1
text = ['']*j
i = 0
with open('text.txt') as f :
    text = f.readlines()

tts.setProperty('voice', 'ru')
tts.setProperty('rate', 130)




#priv1 = pg.mixer.Sound('test.mp3')

pg.init()
screen_width = 840
screen_height = 566
screen = pg.display.set_mode([screen_width, screen_height])
zastavka = pg.image.load('zastavka2.jpg').convert()
screen.blit(zastavka, (0, 0))
pg.display.update()
clock = pg.time.Clock()
FPS = 120
#pg.time.wait(1000)
pg.font.init()
pg.font.get_fonts()

i = 0
x = 0
k = 0

def nadpis_text(x, y, i,  messeg):
    i = 0
    while i < int(len(messeg)):
        text1 = f.render(str(messeg1), False, (77, 157, 75))
        screen.blit(text1, (10, y))
        pg.display.update()
        klik.play(0, 0, 0).set_volume(0.05)
        #play_text_line(messeg[i])
        text = f.render(str(messeg[i]), True, (77, 157, 75))
        screen.blit(text, (150 + x, y))
        pg.display.update()
        pg.time.wait(60)
        i += 1
        x += 13


def play_text_line(messeg):
    tts.say(messeg)
    tts.runAndWait()

zagruzka.play(-1)

while True:
    for q in pg.event.get():
        if q.type == pg.QUIT:
            sys.exit()
    messeg1 = "18F000__//:"
    messeg = text[0]
    f = pg.font.Font('ConsolaMono.ttf', 18)

    for k in range(j):
        print(i , x )
        messeg = text[k]

        nadpis_text(x, 10+k*40, k, messeg)
        play_text_line(messeg)
        # tts.runAndWait()

        pg.time.wait(300)
