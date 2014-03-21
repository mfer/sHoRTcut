# novo tipo de transicao
define rapTrans = Dissolve (.2)

image bg ync = "ync.png"
image bg lecturehall = "lecturehall.png"
image dig = "dig.jpg"
image castiga = "castiga.jpg"

image sylvie normal = "sylvie2_normal.png"
image sylvie giggle = "sylvie2_giggle.png"
image sylvie smile = "sylvie2_smile.png"
image sylvie surprised = "sylvie2_surprised.png"   

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('ESOFteacher', color="#c8ffc8")
define h = Character(
                    window_left_padding = 15,
                    window_right_padding = 10,
                    window_top_padding = 30,
                    what_slow_caps = 20,
                    show_side_image = Image ("Helper.png", xalign = 0.01, yalign = 0.81))

# The game starts here.
label start:    
    
    stop music fadeout 1.0
    play music "stavroz.ogg" fadein 1.0
    
    scene bg lecturehall
    
    ## movimentacao de personagem
    ##show lucy:
    ##    ypos 100 xpos 180
    ##    linear 3 xpos 600
    
    show sylvie normal at left
    e "Introduzindo Uma Inovação!"

    e "Pelo JP deveria ser sobre Trânsito."
    # transicao entre sprites
    show sylvie surprised at left
    with rapTrans
    
    e "Menu funcionou?"
    
    menu:
        with dissolve
        "Sim":
            jump sim
        "Não":
            jump nao
            
            label sim:
                $ menu_flag = True
                jump done
            label nao:
                $ menu_flag = False
                jump done
            label done:
                    if menu_flag:
                        scene black
                        with blinds
                        scene castiga
                        e "=D"
                    else:
                        scene black
                        e "Não fiz nada aqui! =3"
        
    return

## Quem for alterar a historia do help
## Faça-o neste espaço
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