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
    
    show analista_normal at left
    with fastDissolve
    AR "{cps=40}Olá [nome].{w=2} Sei que você já conversou com o Gerente.{w=2} Eu sou a Analista de Requisitos.{/cps}"
    hide analista_normal
    
    show analista_seria at left
    with fastDissolve
    AR "{cps=40} O Supervisor pediu para te acompanhar nesse projeto, já que você foi contratado há pouco tempo.{/cps}"
    hide analista_seria
    
    show analista_seria at left
    with fastDissolve
    AR "{cps=40} Estamos indo para a padaria {b}{i}Et Part Deux{/i}{/b} agora para levantar o que precisam do primeiro módulo.{/cps}"
    hide analista_seria
    
    show analista_normal at left
    with fastDissolve
    AR "{cps=40}Você será o relator da nossa oficina de requisitos, ficará responsável por redigir a ata.{/cps}"
    hide analista_normal
    
    show analista_brava at left
    with fastDissolve
    AR "{cps=40}Essas oficinas são inspirdadas no JAD.{w=2} Você sabe o que é JAD?{/cps}"
    hide analista_brava
    
    
#JAD 

#Analista diz quais casos de uso foram ganhos





    jump pong
