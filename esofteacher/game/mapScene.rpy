#cena do mapa

screen map:
    fixed:
         text "Qual projeto vc deseja fazer?" xalign 0.5 yalign 0.3
         textbutton "Projeto 1" xalign 0.33 yalign 0.5 action Return() #alterar
         textbutton "Projeto 2" xalign 0.66 yalign 0.5 action Return() #alterar


label mapScene:
    
    $ renpy.music.stop(channel="music",fadeout=1.0)

    show corredor
    show screen map
    P "E agora o q?" #alterar
    
    