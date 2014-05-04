#Momento1: Indo para o cliente

label corrida1SceneMomento1:
    
    scene office
    
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

    scene baker2
    
    DP "{cps=40}Boa tarde, somos da empresa PadaSoft, conforme conversamos por telefone, viemos levantar os requisitos do primeiro módulo.{/cps}"
    DP "{cps=40}Eu sou o (NOMEDONOPRODUTO), esse aqui é o [nome].{/cps}"
    CL "{cps=40}Olá, sou o dono da confeitaria {i}{b}Mestre do Bolo{/b}{/i}, meu nome é (NOMECLIENTEAGIL).{/cps}"
    CL "{cps=40}Estamos querendo um software que possibilite um contato mais próximo com os nossos clientes.{/cps}"
#    - pula para [options]

#    
    label [options]:
        DP "{cps=40}Então, meu caro [nome]. {w=2}Você quer perguntar algo?{/cps}"
        
        menu:
            with fastDissolve
            "(NOMECLIENTEAGIL), quais são as informações mais relevantes?":
                jump [opetion.1]
            "(NOMECLIENTEAGIL), quais são as informações mais relevantes?":
                jump []
            "Quais informações você quer que sejam armazenadas para cada cliente?":
                jump []
            "Quais campos serão de preenchimento obrigatório?":
                jump []
            "Como você gostaria de poder pesquisar por clientes?":
                jump []
            "(NOMECLIENTEAGIL), como vocês gostariam de inserir essas informações?": 
                jump []
            "(NOMECLIENTEAGIL), como esse software vai ajudar a melhorar a qualidade dos seus serviços?":
                jump []
            "Não, tudo bem por mim agora.":
                jump []

        label [option.1]:
            CL "{cps=40}Apesar de sermos uma confeitaria renomada, ainda armazenamos as informações dos nossos clientes em arquivos de papel:{w=2} nomes, telefones, endereços, esse tipo de coisa...{/cps}"
            #img (http://www.arquivopublico.pr.gov.br/arquivos/Image/ArquivoSEOP3.jpg)
            CL "{cps=40}Queremos mudar essa cultura e utilizar um programa de computador.{/cps}" 
            CL "{cps=40}Ficará muito mais fácil fazer backup, encontrar e atualizar uma informação.{/cps}"
            - aumentar a barra de escopo em X1
            - setar flagOption1
            jump [options]
            #- pula para options

    [option.2]:
    cl: Nós teremos um funcionário dentro da empresa que vai ficar responsável por isso. 
    - aumentar a barra de escopo em X2
    - setar flagOption2
    - pula para options

    [option.3]
    cl: Ah! De diversas maneiras. Queremos, por exemplo, saber quais produtos mais vendidos. Quais clientes compram mais. 
    - aumentar a barra de escopo em X3
    - setar flagOption3
    - pula para options

    [option.4]:
    - aumentar barra de stress de acordo com as flagOption’s que não foram setadas.
    -pula para option.fim

    [option.5]:
    cl: Bom, é importante que tenha cadastrado o Nome, o CPF, o telefone e o endereço.
    cl: Ah! Coloquem também data de nascimento! Não temos essa informação hoje no nosso arquivo, mas é legal saber quando o cliente está fazendo aniversário.
    - aumentar a barra de escopo em X5
    - setar flagOption5
    - pula para options

    [option.6]:
    cl: Hmm… Coloca só o Nome e o CPF. Nem sempre tenho as outras informações.
    - aumentar a barra de escopo em X6
    - setar flagOption6
    - pula para options

    [option.7]:
    cl: Quero poder buscar por todas as informações, mas deixe que a pesquisa por Nome e CPF sejam a opção padrão, a escolha mais fácil. É o que mais vamos usar.
    cl: Quero poder digitar tanto o nome quanto o CPF para encontrar o cliente.
    cl: Ah, coloque também uma caixinha que me avise quem são os aniversariantes do dia!
    - aumentar barra de escopo em X7
    - setar flagOption7
    - pula para options.

    [option.fim]
    jg: Ok, acho que esta informação o suficiente para definirmos a primeira entrega.    
    dp: Obrigado pelas informações, (NOMECLIENTEAGIL).
    cl: Por nada. Espero ver isso funcionando em breve!

        
        
        
