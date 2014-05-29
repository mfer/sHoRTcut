image padeiro_bravo = "padeiro_bravo.png"
image padeiro_desapontado = "padeiro_desapontado.png"
image padeiro_feliz = "padeiro_feliz.png"
image padeiro_esperto = "padeiro_esperto.png"
image padeiro_pensativo = "padeiro_pensativo.png"

image analista_brava = "analista_brava.png"
image analista_decepcionada = "analista_decepcionada.png"
image analista_normal = "analista_normal.png"
image analista_seria = "analista_seria.png"
image analista_triste = "analista_triste.png"

image atendente_alegre = "atendente_alegre.png"
image atendente_brava = "atendente_brava.png"
image atendente_desafio = "atendente_desafio.png"
image atendente_normal = "atendente_normal.png"
image atendente_seria = "atendente_seria.png"
image atendente_timida = "atendente_timida.png"
image atendente_triste = "atendente_triste.png"

init python:
    contador = 0
    conducoes = [ [u'{b}Caro Cliente, quais são as informações mais relevantes?{/b}','conduction0', True],
                    [u'{b}Caro Cliente, como vocês gostariam de inserir essas informações?{/b}','conduction1', True],
                    [u'{b}Caro Cliente, como esse software vai ajudar a melhorar a qualidade dos seus serviços?{/b}','conduction2', True],
                    [u'{b}Quais informações você quer que sejam armazenadas para cada cliente?{/b}', 'conduction3', True],
                    [u'{b}Quais campos serão de preenchimento obrigatório?{/b}', 'conduction4', True],
                    [u'{b}Como você gostaria de poder pesquisar por clientes?{/b}', 'conduction5', True],
                ]
#momento com a Analista de Requisitos dentro da empresa
label cascataScene:
    scene office
    $ renpy.music.stop(channel="music",fadeout=1.0)     
    $ renpy.music.play("Delusion.ogg", channel="music", loop=True, fadein=1.0)
    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Olá [nome].{w=2} Sei que você já conversou com o Gerente.{w=2} Eu sou a Analista de Requisitos.{/cps}"
    hide analista_normal
    
    show analista_seria at right
    with fastDissolve
    AR "{cps=40} O Supervisor pediu para te acompanhar nesse projeto, já que você foi contratado há pouco tempo.{/cps}"
    hide analista_seria
    
    show analista_seria at right
    with fastDissolve
    AR "{cps=40} Estamos indo para a padaria {b}{i}Et Part Deux{/i}{/b} agora para levantar o que eles desejam à respeito do produto.{/cps}"
    hide analista_seria
    
    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Você será o relator da nossa oficina de requisitos, ficará responsável por redigir a ata.{/cps}"
    hide analista_normal
    
    show analista_brava at right
    with fastDissolve
    AR "{cps=40}Essas oficinas são inspiradas no JAD.{w=2} Você sabe o que é JAD?{/cps}"
    hide analista_brava
    
    $ minutes += 10
    
    menu:
        with fastDissolve

        "Reuniões formatadas":
            $ strss = strss - 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)
            with fastDissolve
            
            show analista_normal at right
            with fastDissolve
            AR "{cps=40}Isso mesmo!{/cps}"
            hide analista_normal
            
            show analista_normal at right
            with fastDissolve
            AR "{cps=40}Modéstia à parte eu sou uma ótima condutora de JADs...{/cps}"
            hide analista_normal
            
            $ minutes += 5
            jump jad_answer
        "Jogos Aleatórios Direcionados":
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)
            with fastDissolve
            
            show analista_decepcionada at right
            with fastDissolve
            AR "{cps=40}Como assim! Totalmente Errado. Não faça isso com você mesmo.{/cps}"
            hide analista_decepcionada
            
            $ minutes += 5
            jump jad_answer
        
        "Não sei.":
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)
            with fastDissolve
            
            show analista_triste at right
            with fastDissolve
            AR "{cps=40}Não acredito! Deve ser nervosismo…{/cps}"
            hide analista_triste
            
            $ minutes += 5
            jump jad_answer
            
    label jad_answer:
        show analista_normal at right
        with fastDissolve
        AR "{cps=40}JAD são reuniões com diversos grupos de participantes, um líder neutro e um processo estruturado.{/cps}"
        hide analista_normal
        
        show analista_seria at right
        with fastDissolve
        AR "{cps=40}Aplicáveis a diversos problemas: engenharia de requisitos, desenho de produto ou desenho de processos.{/cps}"
        hide analista_seria

    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Há um transporte da empresa para nos levar até a {i}{b}Et Part Deux{/b}{/i}. Vamos?{/cps}"
    hide analista_normal


#JAD 
    scene bakery2
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("School of Quirks.mp3", channel="music", loop=True, fadein=1.0)

    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Bom dia, somos da empresa PadaSoft, viemos realizar a reunião formatada.{/cps}"
    hide analista_normal

    show padeiro_esperto at right
    with fastDissolve
    PA "{cps=40}Bom dia! Sou Pierre, o padeiro.{/cps}"
    hide padeiro_esperto

    show atendente_alegre at left
    with fastDissolve
    AT "{cps=40}Olá! Sou Ana, trabalho aqui como atendente.{/cps}"
    hide atendente_alegre

    show atendente_normal at left
    show padeiro_feliz at right
    with fastDissolve
    PA "{cps=40}Ana conhece bem a {i}{b}Et Part Deux{/b}{/i}.{w=2} Espero que consigamos bons resultados.{/cps}"
    hide padeiro_feliz
    hide atendente_normal

    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Ah sim. Eu também! {w=2} Vamos começar? {w=10} Peço para que desliguem os celulares.{/cps}"
    hide analista_normal

    show padeiro_desapontado at right
    show atendente_triste at left
    PA "{cps=40}Vamos... Vamos...{/cps}"
    AT "{cps=40}Ah...{/cps}"
    hide padeiro_desapontado
    hide atendente_triste

    label conductions:
    
        python:
            if (contador > 3):
                renpy.jump('conduction_end')
        
        show analista_normal at right
        with fastDissolve
        AR "{cps=40}Então, [nome]. {w=2}Como você conduziria esse JAD?{/cps}"
        hide analista_normal

        python:
            conducoes2 = [x[:-1] for x in conducoes if x[2]]
            result = menu(conducoes2[:4] + [[u'{b}Não, tudo bem por mim agora.{/b}','conductionfim']])
            contador += 1
            renpy.jump(result)
             
        
        label conduction0:
            $ conducoes[0][2] = False
            jump figurinha0

        label conduction1:
            $ conducoes[1][2] = False
            jump figurinha1

        label conduction2:
            $ conducoes[2][2] = False
            jump figurinha2

        label conduction3:
            $ conducoes[3][2] = False
            jump figurinha3

        label conduction4:
            $ conducoes[4][2] = False
            jump figurinha4                        


    label figurinha0:
        show padeiro_esperto at right
        with fastDissolve
        PA "{cps=40}Ficará muito mais fácil fazer backup, encontrar e atualizar uma informação.{/cps}"
        hide padeiro_esperto
        $ minutes += 10
        jump conductions

    label figurinha1:
        show padeiro_esperto at right
        with fastDissolve
        PA "{cps=40}Ainda Não teho o que Dizer mas logo terei...{/cps}"
        hide padeiro_esperto
        $ minutes += 10
        jump conductions

    label figurinha2:
        show padeiro_esperto at right
        with fastDissolve
        PA "{cps=40}Ficará muito mais fácil fazer backup, encontrar e atualizar uma informação.{/cps}"
        hide padeiro_esperto
        $ minutes += 10
        jump conductions

    label figurinha3:
        show padeiro_esperto at right
        with fastDissolve
        PA "{cps=40}Ainda Não teho o que Dizer mas logo terei...{/cps}"
        hide padeiro_esperto
        $ minutes += 10
        jump conductions

    label figurinha4:
        show padeiro_esperto at right
        with fastDissolve
        PA "{cps=40}Ainda Não teho o que Dizer mas logo terei...{/cps}"
        hide padeiro_esperto
        $ minutes += 10
        jump conductions

    label conduction_end:
        show analista_normal at right
        with fastDissolve
        AR "{cps=40}Bom. Por Hoje é só! {w=2} Vamos voltar para a Padasoft.{/cps}"
        hide analista_normal

#TDOD
#De volta à empresa Gerente comenta

    scene escritorioTrad
    
    show gr2 at left
    with fastDissolve
    GR "{cps=40}Nossa, {b}{i}[nome]!{/i}{/b}{w=2} Vocês demoraram! Mas conte-me como foi?{/cps}"
    hide gr2

    show gr2 at left
    with fastDissolve
    GR "{cps=40}Espero que tenha coletado tudo! Desde funcional a não funcional.{/cps}"
    hide gr2

    show gr2 at left
    with fastDissolve
    GR "{cps=40}O seu trabalho para amanhã de manhã será transformar os funcionais em casos de uso.{/cps}"
    hide gr2

    show gr2 at left
    with fastDissolve
    GR "{cps=40}Você sabe o que é um caso de uso?{/cps}"
    hide gr2

    show gr2 at left
    with fastDissolve
    GR "{cps=40}Agora, descanse. Amanhã reuniremos logo após o almoço.{/cps}"
    hide gr2

#TODO
#Analista diz quais casos de uso foram ganhos
    scene salaDeReuniao
    
    $ renpy.music.stop(channel="music",fadeout=1.0) 
    $ renpy.music.play("Teach_me_master.mp3", channel="music", loop=True, fadein=1.0)

    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Os Requisitos foram levantados no JAD. Agora espero que seja capaz de transformá-los em casos de uso.{/cps}"
    hide analista_normal

    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Diga-me quais são?{/cps}"
    hide analista_normal

#TODO
#Analista diz que comecem os jogos!
    scene office
    $ renpy.music.stop(channel="music",fadeout=1.0) 
    $ renpy.music.play("A Journey Awaits.ogg", channel="music", loop=True, fadein=1.0)      

    show analista_normal at right
    with fastDissolve
    AR "{cps=40}Chegou a hora de implementarmos todos os módulos! A medida que for terminando o Desenvolvimento encaminhe para Teste.{/cps}"
    hide analista_normal
#TODO
#Aumentar a duração desse PONG
    jump pong