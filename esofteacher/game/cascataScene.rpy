image padeiro0 = "padeideux0.png"
image padeiro1 = "padeideux1.png"

image analista0 = "analista0.png"
image analista1 = "analista1.png"

image atendente0 = "atendente0.png"
image atendente1 = "atendente1.png"

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
    
    show analista at left
    with fastDissolve
    AR "{cps=40}Olá [nome].{w=2} Sei que você já conversou com o Gerente.{w=2} Eu sou a Analista de Requisitos.{/cps}"
    hide analista
    
    show analista at left
    with fastDissolve
    AR "{cps=40}{/cps}"
    hide analista
    
    
#JAD 

#Analista diz quais casos de uso foram ganhos





    jump pong
