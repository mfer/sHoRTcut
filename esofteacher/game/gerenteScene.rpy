
#background

image gr0 = "gr0.gif"
image gr1 = "gr1.gif"
image gr2 = "gr2.gif"
image gr3 = "gr3.gif"
image gr4 = "gr4.gif"
image gr5 = "gr5.gif"
image gr6 = "gr6.gif"



label gerenteScene:
    
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("Am - E7 Backing Track (Minor I - V)_2.mp3", channel="music", loop=True, fadein=1.0) 
    show gr2 at left
    with fastDissolve
    GR "{cps=40}Seja bem vindo, {b}{i}[nome]!!!{/i}{/b}{w=2} Muito prazer, meu nome é NOME_DO_GERENTE.{/cps}"
    show gr6 at left
    with fastDissolve
    GR "{cps=40}Sou o gerente do projeto da padaria {i}{b}Et Part Deux{/b}{/i} e utilizaremos o processo PadaTout.{/cps}"
    GR "{cps=40}O PadaTout é um processo já bem maduro, tradicional e bem testado. {w=2} Utilizamos há anos com sucesso aqui.{/cps}"
    show gr5 at left
    with fastDissolve
    GR "{cps=40}Seu papel inicial será ajudar no levantamento de requisitos e te adianto que será 3 módulos de CRUDs.{/cps}"  # ta certo isso?
    GR "{cps=40}Já temos um JAD marcado com o cliente em breve e sua participação nessa reunião será muito bem vinda!{/cps}"
    show gr0 at left
    with fastDissolve
    GR "{cps=40}Arrume suas coisas e volte aqui para que você possa ir junto com o {i}Analista de Requisitos Pleno{/i} da nossa equipe para a reunião.{/cps}" 
    show gr4 at left
    with fastDissolve
    GR "{cps=40}Estou ciente de que está trabalhando em mais de um projeto, mas sua ajuda para a definição dos requisitos será de grande valia!{/cps}"
