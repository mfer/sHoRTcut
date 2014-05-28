#cena gerente


image gr0 = "gr0.png"
image gr1 = "gr1.png"
image gr2 = "gr2.png"
image gr3 = "gr3.png"
image gr4 = "gr4.png"
image gr5 = "gr5.png"
image gr6 = "gr6.png"


image escritorioTrad = "office_room.png"


label gerenteScene:
    
    hide screen map
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("Am - E7 Backing Track (Minor I - V)_2.mp3", channel="music", loop=True, fadein=1.0) 
    
    scene escritorioTrad
    
    show gr2 at left
    with fastDissolve
    GR "{cps=40}Seja bem vindo, {b}{i}[nome]!{/i}{/b}{w=2} Muito prazer, eu sou o Gerente{/cps}"
    hide gr2
    show gr6 at left
    with fastDissolve
    GR "{cps=40}Sou o responsável pelo projeto da padaria {i}{b}Et Part Deux{/b}{/i} e utilizaremos o processo PadaTout.{/cps}"
    GR "{cps=40}O PadaTout é um processo já bem maduro, tradicional e bem testado. {w=2} Utilizamos há anos com sucesso aqui.{/cps}"
    hide gr6
    show gr5 at left
    with fastDissolve
    GR "{cps=40}Seu papel inicial será ajudar no levantamento de requisitos. Adianto que serão três módulos de CRUDs.{/cps}"
    GR "{cps=40}Já temos um JAD marcado com o cliente em breve e sua participação nessa reunião será muito bem vinda!{/cps}"
    hide gr5
    show gr0 at left
    with fastDissolve
    GR "{cps=40}Arrume suas coisas e volte aqui para ir junto com o {i}Analista de Requisitos Pleno{/i} da nossa equipe para a reunião.{/cps}" 
    hide gr0
    show gr4 at left
    with fastDissolve
    GR "{cps=40}Estou ciente de que está trabalhando em mais de um projeto, mas sua ajuda para a definição dos requisitos será de grande valia!{/cps}"
    hide gr4

    $ gerente = True

    if not mestreDoBolo:
        show gr4 at left
        with fastDissolve
        GR "{cps=40}Sem mais delongas, peço que agora conheça o Líder da equipe Ágil: também conhecido por \"Sr. Rapidinho\"...{/cps}"
        hide gr4 
    
        show black
        with blinds
       
        jump mestreDoBoloScene

    show black
    with blinds

    jump mapScene0
