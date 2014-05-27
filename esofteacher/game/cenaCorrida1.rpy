#Momento1: Indo para o cliente


image cliente0 = "padeiro0.png"
image cliente1 = "padeiro1.png"
image cliente2 = "padeiro2.png"
image cliente3 = "padeiro3.png"
image cliente4 = "padeiro4.png"
image cliente5 = "padeiro5.png"

image donoDoProd0 = "aoi0.png"
image donoDoProd1 = "aoi1.png"
image donoDoProd2 = "aoi2.png"
image donoDoProd3 = "aoi3.png"
image donoDoProd4 = "aoi4.png"
image donoDoProd5 = "aoi5.png"
image donoDoProd6 = "aoi6.png"
image donoDoProd7 = "aoi7.png"
image donoDoProd8 = "aoi8.png"


init python:
    contador = 0
    flagOption5 = False
    flagOption6 = False
    flagOption7 = False
    perguntas = [   [u'{b}Caro Cliente, quais são as informações mais relevantes?{/b}','option0', True], 
                    [u'{b}Caro Cliente, como vocês gostariam de inserir essas informações?{/b}','option1', True],
                    [u'{b}Caro Cliente, como esse software vai ajudar a melhorar a qualidade dos seus serviços?{/b}','option2', True],
                    [u'{b}Quais informações você quer que sejam armazenadas para cada cliente?{/b}', 'option3', True],
                    [u'{b}Quais campos serão de preenchimento obrigatório?{/b}', 'option4', True],
                    [u'{b}Como você gostaria de poder pesquisar por clientes?{/b}', 'option5', True],
                ]


label corrida1SceneMomento1:
    
    scene office
    $ renpy.music.stop(channel="music",fadeout=1.0) 
    $ renpy.music.play("A Journey Awaits.ogg", channel="music", loop=True, fadein=1.0)
    
    show donoDoProd8 at right
    with fastDissolve
    DP "{cps=40}Olá [nome].{w=2} Vi você conversando com o Scrum Master quando chegou.{w=2} Eu sou o Dono do produto.{/cps}"
    hide donoDoProd8
    show donoDoProd0 at right
    with fastDissolve
    DP "{cps=40} O Supervisor pediu para te acompanhar nesse projeto, já que você foi contratado há pouco tempo.{/cps}"
    hide donoDoProd0
    show donoDoProd4 at right
    with fastDissolve
    DP "{cps=40}Atuarei, junto com você, como dono do produto, para que você possa ir treinando, aprendendo e se acostumando com a empresa.{/cps}"
    hide donoDoProd4
    show donoDoProd3 at right
    with fastDissolve
    DP "{cps=40}Não se assuste, então, se eu fizer alguns questionamentos para ver se está aprendendo mesmo.{/cps}"
    hide donoDoProd4
    show donoDoProd3 at right
    with fastDissolve
    DP "{cps=40}O Supervisor que pediu para fazer isso, a culpa não é minha!{/cps}"
    hide donoDoProd3
    show donoDoProd7 at right
    with fastDissolve
    DP "{cps=40}Como está trabalhando em outro projeto também, talvez terei que te substituir se em algum momento não puder trabalhar no projeto com a PadaOne.{/cps}"
    hide donoDoProd7
    show donoDoProd6 at right
    with fastDissolve
    DP "{cps=40}Estamos indo para a confeitaria {b}{i}Mestre do Bolo{/i}{/b} agora para levantar o que precisam do primeiro módulo.{/cps}"
    hide donoDoProd6
    show donoDoProd7 at right
    with fastDissolve
    DP "{cps=40}Você será responsável por escrever as histórias que conseguirmos levantar.{w=2} Você sabe o que é uma história?{/cps}"
    hide donoDoProd7
    $ minutes += 10

    menu:
        with fastDissolve

        
        "Frases que capturam o que o usuário faz ou precisa fazer no sistema, escritas de modo informal.":
            show donoDoProd3 at right
            with fastDissolve
            DP "{cps=40}Exatamente!!!{/cps}"
            $ minutes += 5
            hide donoDoProd3
            jump historia_fim1
        "Frases que contam como o usuário deve interagir com o sistema, o que ele precisa que o sistema faça, escritas de modo formal, como um diagrama.":
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
            with fastDissolve
            show donoDoProd0 at right
            with fastDissolve
            DP "{cps=40}Quase isso…{/cps}"
            hide donoDoProd0
            show donoDoProd6 at right
            with fastDissolve
            DP "{cps=40}As frases idealmente devem ser escritas de modo mais informal, para serem mais fáceis de serem entendidas pelo cliente.{/cps}"
            hide donoDoProd6
            $ minutes += 5
            jump historia_fim1
        "Não sei.":
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
            with fastDissolve
            show donoDoProd0 at right
            with fastDissolve
            DP "{cps=40}Queria ser assim tranquilo, que nem você…{/cps}"
            hide donoDoProd0
            show donoDoProd7 at right
            with fastDissolve
            DP "{cps=40}Histórias são frases que capturam o que o usuário faz ou precisa fazer no sistema, escritas de modo informal.{/cps}"
            hide donoDoProd7
            $ minutes += 5
            jump historia_fim1
        
    label historia_fim1:
        show donoDoProd7 at right
        with fastDissolve
        DP "{cps=40}A partir das histórias que você escrever é que vamos depois definir as tarefas para os programadores.{/cps}"
        hide donoDoProd7
        show donoDoProd6 at right
        with fastDissolve
        DP "{cps=40}Vamos descer que nosso taxi já deve estar chegando.{/cps}"
        hide donoDoProd6
        show black
        with blinds
        $ minutes += 5
        jump momento2
        

label momento2: #Levantando requisitos no cliente - montando histórias

    scene bakery2
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("School of Quirks.mp3", channel="music", loop=True, fadein=1.0)

    
    show donoDoProd8 at right
    with fastDissolve
    DP "{cps=40}Boa tarde, somos da empresa PadaSoft, conforme conversamos por telefone, viemos levantar os requisitos do primeiro módulo.{/cps}"
    hide donoDoProd8
    show donoDoProd6 at right
    with fastDissolve
    DP "{cps=40}Eu sou o Dono do Produto, esse aqui é o [nome].{/cps}"
    hide donoDoProd6
    show cliente0 at right
    with fastDissolve
    CL "{cps=40}Olá, sou o dono da confeitaria {i}{b}Mestre do Bolo{/b}{/i}, eu sou o Cliente.{/cps}"
    hide cliente0
    show cliente5 at right
    with fastDissolve
    CL "{cps=40}Estamos querendo um software que possibilite um contato mais próximo com os nossos clientes.{/cps}"
    hide cliente5

    label options:
    
        python:
            if (contador > 3):
                renpy.jump('optionfim')
        
        show donoDoProd7
        with fastDissolve
        DP "{cps=40}Então, meu caro [nome]. {w=2}Você quer perguntar algo?{/cps}"
        hide donoDoProd7
        

        python:
            perguntas2 = [x[:-1] for x in perguntas if x[2]]
            result = menu(perguntas2[:4] + [[u'{b}Não, tudo bem por mim agora.{/b}','optionfim']])
            contador += 1
            renpy.jump(result)
             
        
        label option0:
            $ perguntas[0][2] = False

            hide cliente5
            show cliente1 at right
            with fastDissolve
            CL "{cps=40}Apesar de sermos uma confeitaria renomada, ainda armazenamos as informações dos nossos clientes em arquivos de papel:{w=2} nomes, telefones, endereços, esse tipo de coisa...{/cps}"
            #img (http://www.arquivopublico.pr.gov.br/arquivos/Image/ArquivoSEOP3.jpg)
            hide cliente1
            show cliente3 at right
            with fastDissolve
            CL "{cps=40}Queremos mudar essa cultura e utilizar um programa de computador.{/cps}" 
            hide cliente3
            show cliente2 at right
            with fastDissolve
            CL "{cps=40}Ficará muito mais fácil fazer backup, encontrar e atualizar uma informação.{/cps}"
            hide cliente2
            #- aumentar a barra de escopo em X1
            #- setar flagOption1
            #$ flagOption = True
            $ minutes += 10
            jump options
            #- pula para options

        label option1:
            $ perguntas[1][2] = False

            show cliente5 at right
            with fastDissolve
            CL "{cps=40}Nós teremos um funcionário dentro da empresa que vai ficar responsável por isso.{/cps}"
            hide cliente5
            #- aumentar a barra de escopo em X2
            #- setar flagOption2
            #$ flagOption = True
            $ minutes += 10
            jump options
            #- pula para options

        label option2:
            $ perguntas[2][2] = False

            show cliente2 at right
            with fastDissolve
            CL "{cps=40}Ah! De diversas maneiras. Queremos, por exemplo, saber quais produtos mais vendidos. Quais clientes compram mais.{/cps}"
            hide cliente2
            #- aumentar a barra de escopo em X3
            #- setar flagOption3
            #$ flagOption = True
            $ minutes += 10
            jump options
            #- pula para options


        label option3:
            $ perguntas[3][2] = False

            show cliente3 at right
            with fastDissolve
            CL "{cps=40}Bom, é importante que tenha cadastrado o Nome, o CPF, o telefone e o endereço.{/cps}"
            hide cliente3
            show cliente2 at right
            with fastDissolve
            CL "{cps=40}Ah! Coloquem também data de nascimento! Não temos essa informação hoje no nosso arquivo, mas é legal saber quando o cliente está fazendo aniversário.{/cps}"
            hide cliente2
            $ minutes += 10
            $ flagOption5 = True
            jump options

        label option4:
            $ perguntas[4][2] = False

            show cliente5 at right
            with fastDissolve
            CL "{cps=40}Hmm… Coloca só o Nome e o CPF. Nem sempre tenho as outras informações.{/cps}"
            hide cliente5
            $ minutes += 10
            $ flagOption6 = True
            jump options

        label option5:
            $ perguntas[5][2] = False

            show cliente3 at right
            with fastDissolve
            CL "{cps=40}Quero poder buscar por todas as informações, mas deixe que a pesquisa por Nome e CPF sejam a opção padrão, a escolha mais fácil. É o que mais vamos usar.{/cps}"
            hide cliente3
            show cliente2 at right
            with fastDissolve
            CL "{cps=40}Quero poder digitar tanto o nome quanto o CPF para encontrar o cliente.{/cps}"
            hide cliente2
            show cliente5 at right
            with fastDissolve
            CL "{cps=40}Ah, coloque também uma caixinha que me avise quem são os aniversariantes do dia!{/cps}"
            hide cliente5
            $ flagOption7 = True
            $ minutes += 10
            jump options

        # DEIXAR NO FINAL
        label optionfim:
            P "{cps=40}Ok, acho que esta informação é suficiente para definirmos a primeira entrega.{/cps}" 
            show donoDoProd6 at right
            with fastDissolve
            DP "{cps=40}Obrigado pelas informações, caro Cliente.{/cps}"
            hide donoDoProd6
            
            show cliente0 at right
            with fastDissolve
            CL "{cps=40}Por nada. Espero ver isso funcionando em breve!{/cps}"
            hide cliente0
            show black
            with blinds
            jump momento3
            
label momento3:
    
    scene escritorioAgil
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("Purple_Motion_-_Charts_overdrive.mp3", channel="music", loop=True, fadein=1.0) 
    
    show mb2 at left
    with fastDissolve
    MB "{cps=40}Bom que já voltaram!{/cps}"
    hide mb2
    show mb4 at left
    with fastDissolve
    MB "{cps=40} O Dono do Produto me falou que vocês levantaram como deve ser o módulo CLIENTE.{/cps}"
    hide mb4
    show mb7 at left
    with fastDissolve
    MB "{cps=40}Estamos indo planejar agora a primeira corrida. Você sabe o que é uma corrida?{/cps}"
    hide mb7
    
    menu:
        with fastDissolve
        "{b}{i}Chegar rápido de um lugar até outro?{/i}{/b}":
            jump sprint1
        "{b}{i}Uma tradução de sprint?{/i}{/b}":
            jump sprint2
        "{b}{i}Não sei.{/i}{/b}":
            jump sprint3

    label sprint1:
        #- aumentar a barra de stress em X
        show mb5 at left
        with fastDissolve
        MB "{cps=40}É… em outro contexto.{/cps}"
        hide mb5
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        $ minutes += 5
        #- Pula para sprint.explicacao
        jump sprintExplicacao
    
    label sprint2:
        show mb10 at left
        with fastDissolve
        MB "{cps=40}Isso! Mas o que é uma sprint?{/cps}"
        hide mb10
        menu:
            with fastDissolve
            "{i}{b}Não sei.{/b}{/i}":
                jump sprint2_1
            "{i}{b}Reunião de uma metodologia ágil.{/b}{/i}":
                jump sprint2_2
            "{i}{b}Unidade de tempo de desenvolvimento do projeto.{/b}{/i}":
                jump sprint2_3
       
    label sprint3:
        #- aumentar a barra de stress em X
        show mb8 at left
        with fastDissolve
        MB "{cps=40}Não fique triste, irei te explicar agora…{/cps}"
        hide mb8
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        #- pula para sprint.explicacao
        $ minutes += 5
        jump sprintExplicacao
    
    label sprint2_1:
        #- aumentar a barra de stress em X
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        #- pula para sprint.explicacao
        $ minutes += 5
        jump sprintExplicacao
    
    label sprint2_2:
        #- aumentar a barra de stress em X
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        show mb5 at left
        MB "{cps=40}Não, não é isso…{/cps}"
        hide mb5
        #- pula para sprint.explicacao
        $ minutes += 5
        jump sprintExplicacao
    
    label sprint2_3:
        show mb9 at left
        MB "{cps=40}Isso!{/cps}"
        hide mb9
        #- pula para sprint.explicacao
        $ minutes += 5
        jump sprintExplicacao
    
    label sprintExplicacao:
        show mb9 at left
        with fastDissolve
        MB "{cps=40}A corrida é a unidade básica de desenvolvimento em Scrum. Corridas tendem a durar entre uma semana e um mês, e são um esforço dentro de uma faixa de tempo (ou seja, restrito a uma duração específica) de comprimento constante.{/cps}"
        hide mb9
        show mb2 at left
        with fastDissolve
        MB "{cps=40}O conjunto de funcionalidades que entram em uma corrida é um conjunto de prioridades de requisitos de alto nível definidos pelo Dono do Produto.{/cps}"
        hide mb2
        show mb0 at left
        with fastDissolve
        MB "{cps=40}Vamos então para a reunião.{/cps}"
        hide mb0
        show black
        with blinds
        $ minutes += 5
        jump momento4
        
label momento4:
    
    $ renpy.music.stop(channel="music",fadeout=1.0) 
    $ renpy.music.play("Teach_me_master.mp3", channel="music", loop=True, fadein=1.0)

    scene salaDeReuniao
    
    show donoDoProd6 at right
    with fastDissolve
    DP "{cps=40}[nome], fale para a gente quais são as histórias levantadas com o cliente.{/cps}"
    hide donoDoProd6
    
    if (flagOption6 and flagOption7):
        jump historiasClienteFull
    #- se flagOption6 igual a 1, pula para [historiasCliente.obrigatórios]
    if (flagOption6):
        jump historiasClienteObrigatorias
    #- se flagOption7 igual a 1, pula para [historiasCliente GT.pesquisa]
    if (flagOption7):
        jump historiasClientePesquisa
    if (flagOption5):
        jump historiasClienteCampos
    #- se flagOption5 igual a 1, pula para [historiasCliente.campos]
    jump historiasClienteSimples
    #- pula para [historiasCliente.simples]

    label historiasClienteFull:
        P "{cps=40}Temos três histórias:{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento, sendo que apenas Nome e CPF são obrigatórios.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero encontrar meus clientes com base em qualquer campo, mas principalmente por Nome e CPF.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero ser avisado de quais clientes fazem aniversário no dia.”{/cps}"
        jump historiasClienteFim

    label historiasClienteObrigatorias:
        P "{cps=40}Temos duas histórias:{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento, sendo que apenas Nome e CPF são obrigatórios.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero pesquisar meus clientes cadastrados.”{/cps}"
        jump historiasClienteFim
            
    label historiasClientePesquisa:
        P "{cps=40}Temos três histórias:{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero encontrar meus clientes com base em qualquer campo, mas principalmente por Nome e CPF.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero ser avisado de quais clientes fazem aniversário no dia.”{/cps}"
        jump historiasClienteFim
        
    label historiasClienteCampos:
        P "{cps=40}Temos duas histórias:{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero pesquisar meus clientes cadastrados.”{/cps}"
        jump historiasClienteFim

    label historiasClienteSimples:
        P "{cps=40}Temos duas histórias:{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero cadastrar clientes.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero pesquisar meus clientes cadastrados.”{/cps}"
        jump historiasClienteFim

    label historiasClienteFim:
        
        show donoDoProd7 at right
        with fastDissolve
        DP "{cps=40}Ok.{w=2} Quais serão implementadas nessa primeira sprint?{/cps}" 
        hide donoDoProd7
        show donoDoProd6 at right
        with fastDissolve
        DP "{cps=40}Lembre-se que o importante é termos software funcionando no prazo de até duas semanas.{/cps}"
        hide donoDoProd6
        
        show black
        with blinds
        jump momento5
        
label momento5:
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    
    show black
    with blinds
    jump momento6
    
label momento6:
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    
