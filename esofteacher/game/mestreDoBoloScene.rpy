
#Cena do mestre do bolo

image mb0 = "mb0.png"
image mb1 = "mb1.png"
image mb2 = "mb2.png"
image mb3 = "mb3.png"
image mb4 = "mb4.png"
image mb5 = "mb5.png"
image mb6 = "mb6.png"
image mb7 = "mb7.png"
image mb8 = "mb8.png"
image mb9 = "mb9.png"
image mb10 = "mb10.png"
image mb11 = "mb11.png"

image escritorioAgil = "Interior-banker.jpg"

label mestreDoBoloScene:
    
    hide screen map
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("Purple_Motion_-_Charts_overdrive.mp3", channel="music", loop=True, fadein=1.0) 
    
    scene escritorioAgil
    
    show mb2 at left
    with fastDissolve
    MB "{cps=40}Olá, {b}{i}[nome]!!!{/i}{/b}{w=2} Você é o novo contratado, não é?{/cps}"
    hide mb2
    show mb4 at left
    with fastDissolve
    MB "{cps=40}Prazer em conhecê-lo!{/cps}"
    hide mb4
    show mb2 at left
    with fastDissolve
    MB "{cps=40}Sou o líder do processo PadaOne, que utiliza uma metodologia ágil.{/cps}"
    hide mb2
    
        
    show mb1 at left
    with fastDissolve
    MB "{cps=40}Sua tarefa será participar do desenvolvimento do programa para atender à necessidade do nosso cliente.{/cps}" 
        
    show mb0 at left
    with fastDissolve
    MB "{cps=40}O projeto está bem no início, vamos planejar nossa primeira corrida daqui a pouco.{/cps}"
        
    show mb4 at left
    with fastDissolve
    MB "{cps=40}O sistema será desenvolvido em módulos.{w=2} Não sabemos ainda qual será o primeiro módulo, mas vamos no cliente em breve. {/cps}"
        
    show mb6 at left
    with fastDissolve
    MB "{cps=40}Sei que está trabalhando em outro projeto também, mas se puder ir conosco será ótimo!{/cps}"
        
    show mb7 at left
    with fastDissolve
    MB "{cps=40}Assim que tiver arrumado suas coisas, basta vir até a nossa equipe para colocarmos a {b}{i}“mão na massa”{/b}{/i}{/cps}"
    hide mb7
    
    show black
    with blinds

    $ mestreDoBolo = True

    if not gerente:
        show mb7 at left
        with fastDissolve
        MB "{cps=40}Então é isso, peço que agora conheça o Líder da equipe Tradicional. Conhecido também por \"Dr. Engessadinho\"...{/cps}"
        hide mb7
        jump gerenteScene

    jump mapScene