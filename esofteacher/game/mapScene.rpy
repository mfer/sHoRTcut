#cena do mapa

label mapScene:

    $ renpy.music.stop(channel="music",fadeout=1.0)
    $ renpy.music.play("level1-step1-evil.wav", channel="music", loop=True, fadein=1.0)

    show corredor


    menu:
        "Tradicional":
            show screen clock
            jump gerenteScene
        "Ágil":
            show screen clock
            jump mestreDoBoloScene




    "" #alterar


