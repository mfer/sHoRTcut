## Cena do help

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