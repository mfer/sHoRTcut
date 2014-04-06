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
    play music "bgmfum.wav" fadein 1.0 
    scene dig                           # alterar
    
    show sylvie normal at left
    
    h "Olá, eu me chamo Helper e irei lhe ensinar sobre o funcionamento do jogo ^-^"
    h "Para avançar pelo jogo, use o botão esquerdo do mouse ou pressione as teclas espaço ou enter"
    
    label testMenu:
        h "Em um menu, use o botão esquerdo do mouse para fazer uma escolha, ou use as setas do teclado para escolher uma opção e pressione enter para ativá-la"
        h "Vamos fazer um teste:"
        
        h "Você compreendeu o funcionamento?"

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
                        h "Parabéns"                        
                    else:
                        h "Que pena, leia atentamente as instruções ^-^" # mudar as figuras
                        jump testMenu

    return