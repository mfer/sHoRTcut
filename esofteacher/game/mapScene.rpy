#cena do mapa

screen map:
    
    modal True
    
    frame:
        style_group "yesno"
        
        xmargin .05
        ypos .3
        xpos .3
        yanchor 0
        ypadding .05
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        
        text "{b}{i}O que irei fazer agora?!{/i}{/b}" xalign 0.5
        
        hbox:
            
            xalign 0.5
            spacing 100

            textbutton "Projeto 1" action Jump("gerenteScene") #alterar
            textbutton "Projeto 2" action Jump("mestreDoBoloScene") #alterar


label mapScene:
    
    $ renpy.music.stop(channel="music",fadeout=1.0)

    show corredor
    show screen map
    show screen clock
    
    "" #alterar
    
    