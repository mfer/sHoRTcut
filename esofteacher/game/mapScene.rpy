#cena do mapa


init:
    $ gerente = False
    $ mestreDoBolo = False

label mapScene:

    $ renpy.music.stop(channel="music",fadeout=1.0)
    $ renpy.music.play("level1-step1-evil.wav", channel="music", loop=True, fadein=1.0)

    show corredor

    if not gerente and not mestreDoBolo:
        menu:
            "Tradicional - PadaTout":
                show black
                with blinds
                show screen clock
                jump gerenteScene
            "Ágil - PadaOne":
                show black
                with blinds
                show screen clock
                jump mestreDoBoloScene

    if gerente and mestreDoBolo:
        menu:
            "Tradicional - PadaTout":
                show black
                with blinds
                show screen clock
                #jump 
            "Ágil - PadaOne":
                show black 
                with blinds
                show screen clock
                jump corrida1SceneMomento1




    "" #alterar


