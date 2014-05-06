#Momento1: Indo para o cliente


init:
    $ flagOption1 = False 
    $ flagOption2 = False
    $ flagOption3 = False
#    $ flagOption4 = False 
    $ flagOption5 = False 
    $ flagOption6 = False
    $ flagOption7 = False
    
label corrida1SceneMomento1:
    
    scene office
    $ renpy.music.stop(channel="music",fadeout=1.0) 
    $ renpy.music.play("A Journey Awaits.ogg", channel="music", loop=True, fadein=1.0)
    
    DP "{cps=40}Olá [nome].{w=2} Vi você conversando com o (NOMEDOSCRUMMASTER) quando chegou.{w=2} Meu nome é (NOMEDONODOPRODUTO).{/cps}"
    DP "{cps=40}(NOMESUPERVISOR) pediu para te acompanhar nesse projeto, já que você foi contratado há pouco tempo.{/cps}"
    DP "{cps=40}Atuarei, junto com você, como dono do produto, para que você possa ir treinando, aprendendo e se acostumando com a empresa.{/cps}"
    DP "{cps=40}Não se assuste, então, se eu fizer alguns questionamentos para ver se está aprendendo mesmo.{/cps}"
    DP "{cps=40}(NOMESUPERVISOR) que pediu para fazer isso, a culpa não é minha!{/cps}"
    DP "{cps=40}Como está trabalhando em outro projeto também, talvez terei que te substituir se em algum momento não puder trabalhar no projeto com a PadaOne.{/cps}"
    DP "{cps=40}Estamos indo para a confeitaria {b}{i}Mestre do Bolo{/i}{/b} agora para levantar o que precisam do primeiro módulo.{/cps}"
    DP "{cps=40}Você será responsável por escrever as histórias que conseguirmos levantar.{w=2} Você sabe o que é uma história?{/cps}"
    
    menu:
        with fastDissolve
        "Frases que capturam o que o usuário faz ou precisa fazer no sistema, escritas de modo informal.":
            DP "{cps=40}Exatamente!!!"
            jump historia_fim1
        "Frases que contam como o usuário deve interagir com o sistema, o que ele precisa que o sistema faça, escritas de modo formal, como um diagrama.":
            # aumenta stress em X
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
            with fastDissolve
            DP "{cps=40}Quase isso…{/cps}"
            DP "{cps=40}As frases idealmente devem ser escritas de modo mais informal, para serem mais fáceis de serem entendidas pelo cliente.{/cps}"
            jump historia_fim1
        "Não sei.":
            # aumenta stress em X
            $ strss = strss + 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
            with fastDissolve
            DP "{cps=40}Queria ser assim tranquilo, que nem você…{/cps}"
            DP "{cps=40}Histórias são frases que capturam o que o usuário faz ou precisa fazer no sistema, escritas de modo informal.{/cps}"
            jump historia_fim1
        
    label historia_fim1:
        DP "{cps=40}A partir das histórias que você escrever é que vamos depois definir as tarefas para os programadores.{/cps}"
        DP "{cps=40}Vamos descer que nosso taxi já deve estar chegando.{/cps}"
        show black
        with blinds
        jump momento2
        


label momento2: #Levantando requisitos no cliente - montando histórias

    scene bakery2
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    #Achar musica

    DP "{cps=40}Boa tarde, somos da empresa PadaSoft, conforme conversamos por telefone, viemos levantar os requisitos do primeiro módulo.{/cps}"
    DP "{cps=40}Eu sou o (NOMEDONOPRODUTO), esse aqui é o [nome].{/cps}"
    CL "{cps=40}Olá, sou o dono da confeitaria {i}{b}Mestre do Bolo{/b}{/i}, meu nome é (NOMECLIENTEAGIL).{/cps}"
    CL "{cps=40}Estamos querendo um software que possibilite um contato mais próximo com os nossos clientes.{/cps}"
#    - pula para [options]
#    
    label options:
        DP "{cps=40}Então, meu caro [nome]. {w=2}Você quer perguntar algo?{/cps}"
        
        menu:
            with fastDissolve
            "{b}(NOMECLIENTEAGIL), quais são as informações mais relevantes?{/b}":
                jump opetion1
            "{b}Quais informações você quer que sejam armazenadas para cada cliente?{/b}":
                jump option5
            "{b}Quais campos serão de preenchimento obrigatório?{/b}":
                jump option6
            "{b}Como você gostaria de poder pesquisar por clientes?{/b}":
                jump option7
            "{b}(NOMECLIENTEAGIL), como vocês gostariam de inserir essas informações?{/b}": 
                jump option2
            "{b}(NOMECLIENTEAGIL), como esse software vai ajudar a melhorar a qualidade dos seus serviços?{/b}":
                jump option3
            "{b}Não, tudo bem por mim agora.{/b}":
                jump option4

        label option1:
            CL "{cps=40}Apesar de sermos uma confeitaria renomada, ainda armazenamos as informações dos nossos clientes em arquivos de papel:{w=2} nomes, telefones, endereços, esse tipo de coisa...{/cps}"
            #img (http://www.arquivopublico.pr.gov.br/arquivos/Image/ArquivoSEOP3.jpg)
            CL "{cps=40}Queremos mudar essa cultura e utilizar um programa de computador.{/cps}" 
            CL "{cps=40}Ficará muito mais fácil fazer backup, encontrar e atualizar uma informação.{/cps}"
            #- aumentar a barra de escopo em X1
            #- setar flagOption1
            $ flagOption = True
            jump options
            #- pula para options

        label option2:
            CL "{cps=40}Nós teremos um funcionário dentro da empresa que vai ficar responsável por isso.{/cps}"
            #- aumentar a barra de escopo em X2
            #- setar flagOption2
            $ flagOption = True
            jump options
            #- pula para options

        label option3:
            CL "{cps=40}Ah! De diversas maneiras. Queremos, por exemplo, saber quais produtos mais vendidos. Quais clientes compram mais.{/cps}"
            #- aumentar a barra de escopo em X3
            #- setar flagOption3
            $ flagOption = True
            jump options
            #- pula para options

        label option4:
            jump optionfim
            #- aumentar barra de stress de acordo com as flagOption’s que não foram setadas.
            #-pula para option.fim

        label option5:
            CL "{cps=40}Bom, é importante que tenha cadastrado o Nome, o CPF, o telefone e o endereço.{/cps}"
            CL "{cps=40}Ah! Coloquem também data de nascimento! Não temos essa informação hoje no nosso arquivo, mas é legal saber quando o cliente está fazendo aniversário.{/cps}"
            #- aumentar a barra de escopo em X5
            #- setar flagOption5
            $ flagOption5 = True
            jump options
            #- pula para options

        label option6:
            CL "{cps=40}Hmm… Coloca só o Nome e o CPF. Nem sempre tenho as outras informações.{/cps}"
            #- aumentar a barra de escopo em X6
            #- setar flagOption6
            $ flagOption6 = True
            jump options
            #- pula para options

        label option7:
            CL "{cps=40}Quero poder buscar por todas as informações, mas deixe que a pesquisa por Nome e CPF sejam a opção padrão, a escolha mais fácil. É o que mais vamos usar.{/cps}"
            CL "{cps=40}Quero poder digitar tanto o nome quanto o CPF para encontrar o cliente.{/cps}"
            CL "{cps=40}Ah, coloque também uma caixinha que me avise quem são os aniversariantes do dia!{/cps}"
            #- aumentar barra de escopo em X7
            #- setar flagOption7
            $ flagOption7 = True
            jump options
            #- pula para options.

        label optionfim:
            P "{cps=40}Ok, acho que esta informação o suficiente para definirmos a primeira entrega.{/cps}"    
            DP "{cps=40}Obrigado pelas informações, (NOMECLIENTEAGIL).{/cps}"
            CL "{cps=40}Por nada. Espero ver isso funcionando em breve!{/cps}"
            show black
            with blinds
            jump momento3
            
label momento3:
    
    scene escritorioAgil
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("Purple_Motion_-_Charts_overdrive.mp3", channel="music", loop=True, fadein=1.0) 
    
    MB "{cps=40}Bom que já voltaram!{/cps}"
    MB "{cps=40}(NOMEDONOPRODUTO) me falou que vocês levantaram como deve ser o módulo (PRIMEIROMODULO).{/cps}"
    MB "{cps=40}Estamos indo planejar agora a primeira corrida. Você sabe o que é uma corrida?{/cps}"

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
        MB "{cps=40}É… em outro contexto.{/cps}"
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        #- Pula para sprint.explicacao
        jump sprintExplicacao
    
    label sprint2:
        MB "{cps=40}Isso! Mas o que é uma sprint?{/cps}"
        menu:
            with fastDissolve
            "{i}{b}Não sei.{/i}{/b}":
                jump sprint2_1
            "{i}{b}Reunião de uma metodologia ágil.{/i}{/b}":
                jump sprint2_2
            "{i}{b}Unidade de tempo de desenvolvimento do projeto.{/i}{/b}":
                jump sprint2_3
       
    label sprint3:
        #- aumentar a barra de stress em X
        MB "{cps=40}Não fique triste, irei te explicar agora…{/cps}"
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        #- pula para sprint.explicacao
        jump sprintExplicacao
    
    label sprint2_1:
        #- aumentar a barra de stress em X
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        #- pula para sprint.explicacao
        jump sprintExplicacao
    
    label sprint2_2:
        #- aumentar a barra de stress em X
        $ strss = strss + 5
        show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax) #não consegui fazer atualizar automaticamente
        with fastDissolve
        MB "{cps=40}Não, não é isso…{/cps}"
        #- pula para sprint.explicacao
        jump sprintExplicacao
    
    label sprint2_3:
        MB "{cps=40}Isso!{/cps}"
        #- pula para sprint.explicacao
        jump sprintExplicacao
    
    label sprintExplicacao:
        MB "{cps=40}A corrida é a unidade básica de desenvolvimento em Scrum. Corridas tendem a durar entre uma semana e um mês, e são um esforço dentro de uma faixa de tempo (ou seja, restrito a uma duração específica) de comprimento constante.{/cps}"
        MB "{cps=40}O conjunto de funcionalidades que entram em uma corrida é um conjunto de prioridades de requisitos de alto nível definidos pelo Dono do Produto.{/cps}"
        MB "{cps=40}Vamos então para a reunião.{/cps}"
        show black
        with blinds
        jump momento4
        
label momento4:
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    
    #scene sala de reunião
    DP "{cps=40}(NOMEJOGADOR), fale para a gente quais são as histórias levantadas com o cliente.{/cps}"
    if (flagOption6 and flagOption7):
        jump historiasClienteFull
    #- se flagOption6 igual a 1, pula para [historiasCliente.obrigatórios]
    if (flagOption6 and not flagOption7):
        jump historiasClienteObrigatorias
    #- se flagOption7 igual a 1, pula para [historiasCliente GT.pesquisa]
    if (flagOption7 and not flagOption6):
        jump historiasClienteCampos
    #- se flagOption5 igual a 1, pula para [historiasCliente.campos]
    jump historiasClienteSimples
    #- pula para [historiasCliente.simples]

    label historiasClienteFull:
        P "{cps=40}Temos três histórias:"
        P "{cps=40}“Eu, como dono da empresa, quero cadastrar clientes com Nome, CPF, telefone, endereço e data de nascimento, sendo que apenas Nome e CPF são obrigatórios.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero encontrar meus clientes com base em qualquer campo, mas principalmente por Nome e CPF.”{/cps}"
        P "{cps=40}“Eu, como dono da empresa, quero ser avisado de quais clientes fazem aniversário no dia.”{/cps}"
        jump historiasClienteFim

    label historiasClienteObrigatorios:
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
        DP "{cps=40}Ok.{w=2} Quais serão implementadas nessa primeira sprint?{/cps}" 
        DP "{cps=40}Lembre-se que o importante é termos software funcionando no prazo de até duas semanas.{/cps}"
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
    