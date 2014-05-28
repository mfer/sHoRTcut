image padeiro0 = "padeideux0.png"
image padeiro1 = "padeideux1.png"

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
    flagOption5 = False
    flagOption6 = False
    flagOption7 = False
    perguntas = [ [u'{b}Caro Cliente, quais são as informações mais relevantes?{/b}','option0', True],
                    [u'{b}Caro Cliente, como vocês gostariam de inserir essas informações?{/b}','option1', True],
                    [u'{b}Caro Cliente, como esse software vai ajudar a melhorar a qualidade dos seus serviços?{/b}','option2', True],
                    [u'{b}Quais informações você quer que sejam armazenadas para cada cliente?{/b}', 'option3', True],
                    [u'{b}Quais campos serão de preenchimento obrigatório?{/b}', 'option4', True],
                    [u'{b}Como você gostaria de poder pesquisar por clientes?{/b}', 'option5', True],
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
    AR "{cps=40} Estamos indo para a padaria {b}{i}Et Part Deux{/i}{/b} agora para levantar o que precisam do primeiro módulo.{/cps}"
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
            
            show analista_brava at right
            with fastDissolve
            AR "{cps=40}Isso mesmo!{/cps}"
            hide analista_brava
            
            show analista_normal at right
            with fastDissolve
            AR "{cps=40}Modéstia à parte eu sou uma ótima condutora de JADs...{/cps}"
            hide analista_normal
            
            $ minutes += 5
            jump jad_end
        "Jogos Aleatórios Direcionados":
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)
            with fastDissolve
            
            show analista_brava at right
            with fastDissolve
            AR "{cps=40}Como assim! Totalmente Errado. Não faça isso com você mesmo.{/cps}"
            hide analista_brava
            
            $ minutes += 5
            jump jad_answer
        
        "Não sei.":
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)
            with fastDissolve
            
            show analista_brava at right
            with fastDissolve
            AR "{cps=40}Não acredito! Deve ser nervosismo…{/cps}"
            hide analista_brava
            
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
        
    label jad_end:       
        jump pong
            
#TODO
#JAD 

#TODO
#Analista diz quais casos de uso foram ganhos
