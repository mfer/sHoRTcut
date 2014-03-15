# novo tipo de transicao
define rapTrans = Dissolve (.2)

image bg ync = "ync.png"
image bg lecturehall = "lecturehall.png"
image castiga = "castiga.jpg"

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
    
    play music "stavroz.ogg"
    
    scene bg lecturehall
    
    ## movimentacao de personagem
    ## show lucy:
    ##    ypos 100 xpos 180
    ##    linear 3 xpos 600
    
    show sylvie normal at left
    e "Introduzindo Engenharia de Requisitos"

    e "Imagem de fundo incluída!"
    # transicao entre sprites
    show sylvie surprised at left
    with rapTrans
    
    e "Menu funfou?"
    
    menu:
        with dissolve
        "Yep":
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
                        e "Nao fiz nada aki! =3"
        
    return
