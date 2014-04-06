# novo tipo de transicao
define fastDissolve = Dissolve (.2)

image bg ync = "ync.png"
image bg lecturehall = "lecturehall.png"
image corredor = "corredor.png"

image sylvie normal = "sylvie2_normal.png"
image sylvie giggle = "sylvie2_giggle.png"
image sylvie smile = "sylvie2_smile.png"
image sylvie surprised = "sylvie2_surprised.png"   

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('ESOFteacher', color="#c8ffc8")


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
    
    $ nome = renpy.input("Qual o seu nome?", length=20)

    e "Estamos Introduzindo Uma Inovação, %(nome)s!"

    e "Pelo JP deveria ser sobre Trânsito."
    # transicao entre sprites
    show sylvie surprised at left
    with fastDissolve
    
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
                        scene corredor
                        e "=D"
                    else:
                        scene black
                        e "Não fiz nada aqui! =3"
    return

