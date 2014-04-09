#CenaDoSupervisor

image xp = "Extreme_Programming.png"
image rup = "Development-iterative.gif"

label supervisorScene:
    $ imagepos = Position(xpos=.25, xanchor=0, ypos=50, yanchor=0)
    
    scene office
    
    show supervisor normal1 at right 
    S "{cps=40}Olá, então você é o novo contratado?{/cps}"
    menu:
        
        "Sim":
            show supervisor normal3 at right
            with fastDissolve
            P "{cps=40}Sim, meu nome é{/cps}"  
            $nome = renpy.input("",length=20)
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Muito prazer, {b}{color=ff0000}[nome]{/color}{/b}!\nSeja bem vindo! Não quero te assutar mas…{w=3} Temos muito trabalho por aqui. Vou explicar o que você vai fazer.{/cps}"
        "Não":
            show supervisor anger at right
            with fastDissolve
            S "{cps=40}Então o que você está fazendo aqui?{/cps}"
            return
  
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}Nossa empresa é referência no desenvolvimento de {b}{i}CRUDs{/i}{/b} para gerenciamento de Padarias.{/cps}"
    
    S "{cps=40}A {b}{i}PadaSoft{/i}{/b} é uma empresa que seguia apenas a metodologia tradicional. Você entende do que eu estou falando?{/cps}"

    menu:
        "Sim":
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Que bom, você ganhou um ponto comigo."
        "Não":
            show supervisor disappointed at right
            with fastDissolve
            P "{cps=40}Quando digo metodologia tradicional, estou falando do UP – {i}{b}Unified Process{/b}{/i}, ou do IRUP – {i}{b}IBM Rational Unified process{/b}{/i}, da IBM.{/cps}"
            show rup at imagepos behind supervisor:
                alpha 0.0
                time 0
                linear 1.0 alpha 1.0
            P "{cps=40}Se você quiser se dar bem aqui, sugiro que aprenda mais sobre o {i}{b}RUP{/b}{/i}.{/cps}"
            hide rup            

    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}No entanto, há pouco tempo, estamos experimentando outras metodologias… Você já ouviu falar do{i}{b} XP{/b}{/i}?{/cps}"
    
    menu:
        "Sim":
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Estou gostando de ver. Vejo que vem da {b}UFMG{/b}. Você deve ter estudado com o Professor {b}Rodolfo{b}.{/cps}"
        "Não":
            show supervisor disappointed at right
            with fastDissolve
            P "{cps=40}Então não poderá dizer que não aprendeu nada aqui.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            show xp at imagepos behind supervisor:
                alpha 0.0
                time 0
                linear 1.0 alpha 1.0
            P "{cps=40}Basicamente, o {b}{i}XP{/i}{/b} auxilia a desenvolver software com requisitos vagos e em constante mudança.{/cps}"
            hide xp

    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Sendo assim, a {b}{i}PadaSoft{/i}{/b} desenvolve produtos de qualidade nessas duas vertentes.{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}No método ágil seguimos o processo {b}{i}PadaOne{/i}{/b}{image=sabre.png}, enquanto no tradicional, o processo é o {b}{i}PadaTout{/i}{/b}{image=baguette.png}.{/cps}"
    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Com qual método você se identifica mais?{/cps}"

    menu:
        "Ágil":
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Que sorte a sua.{/cps}"
            show supervisor normal3 at right
            with fastDissolve
            S "{cps=40}Estamos desenvolvendo um projeto com esta metodologia.{/cps}"
            S "{cps=40}Se trata de um software para a padaria {b}{i}Mestre do Bolo{/i}{/b}.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}O cliente é muito exigente e muda de ideia a todo momento.{/cps}"
            S "{cps=40}Então abrace as mudanças.{w=2} Dedique-se a entregas contínuas.{/cps}"

        "Tradicional":
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Hmm, ok.{/cps}"
            S "{cps=40}Então, você é {b}{i}lerdo{/i}{/b}?!{w=2} Brincadeira...{/cps}"
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Temos muitos iguais a você.{/cps}" 
            S "{cps=40}Até resolvemos montar uma equipe para os seus semelhantes.{/cps}" 
            show supervisor normal3 at right
            with fastDissolve
            S "{cps=40}Vocês trabalharão com o projeto para a padaria {b}{i}Et part deux{/i}{/b}.{/cps}"      
            S "{cps=40}O cliente sabe exatamente o que ele quer.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Então não se preocupe com as mudanças.{w=2} Dediquem-se ao levantamento de requisitos eficiente.{/cps}"

    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Meu caro, {color=ff0000}{b}[nome]{/color}{/b}.{w=2} Adotar essas duas abordagens de desenvolvimento, Tradicional e Ágil, trouxe-nos muitas vantagens como você irá perceber.{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}Por outro lado, um clima de competição (algumas vezes exagerado e não muito saudável) emergiu entre as duas equipes: {b}{i}PadaTout{/i}{/b} e {b}{i}PadaOne{/i}{/b}.{/cps}"
    show supervisor smile at right
    with fastDissolve
    S "{cps=40}Então, esteja preparado!!!{/cps}"
    
    $ renpy.music.stop(channel="music",fadeout=1.0)
    show black
    
    with blinds
    #transição proxima cena...
