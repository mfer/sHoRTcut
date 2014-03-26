## Cena do help

define h = Character(
                    window_left_padding = 15,
                    window_right_padding = 10,
                    window_top_padding = 30,
                    what_slow_caps = 20,
                    show_side_image = Image ("Helper.png", xalign = 0.01, yalign = 0.81))

image dig = "dig.jpg"


label helps:
    
    stop music fadeout 1.0
    play music "test_sound.mp3" fadein 1.0
    scene dig
    
    show sylvie normal at left
    
    h "Deseja iniciar o Jogo?"
    menu:
        with dissolve
        "Sim":
            jump yesHelp
        "Não":
            jump noHelp
            
            label yesHelp:
                $ menu_flag = True
                jump doneHelp
            label noHelp:
                $ menu_flag = False
                jump doneHelp
            label doneHelp:
                    if menu_flag:
                        stop music fadeout 1.0
                        scene black
                        with blinds
                        
                        jump start
                    else:
                        stop music fadeout 1.0
                        scene black
                        with blinds

    return