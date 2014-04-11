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
            P "{cps=40}Sim, eu me chamo...{/cps}"
            #"{cps=40}{b}{i}Por favor ensira o seu nome:{/i}{/b}{/cps}"
            $ nome = renpy.input("{b}{i}Por favor insira o seu nome:{/i}{/b}", "", length=20)
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Muito prazer, {b}{color=ff0000}[nome]{/color}{/b}!\nSeja bem vindo! Não quero te assustar mas…{w=3} Temos muito trabalho por aqui. Vou explicar o que você vai fazer.{/cps}"
        "Não":
            show supervisor anger at right
            with fastDissolve
            S "{cps=40}Então o que você está fazendo aqui?{/cps}"
            return
  
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}Nossa empresa dedica-se ao desenvolvimento de {b}{i}CRUDs{/i}{/b} para gerenciamento de Padarias.{/cps}"
    show supervisor smile at right
    with fastDissolve    
    S "{cps=40}Apesar do pouco tempo, a {b}{i}PadaSoft{/i}{/b} já possui uma ótima reputação!{/cps}"
    with fastDissolve
    S "{cps=40}Contamos com você para manter e melhorar essa imagem, inicialmente atuando com o {b}Levantamento de Requisitos{/b}.{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}A propósito, por muito tempo, a {b}{i}PadaSoft{/i}{/b} adotou somente a metodologia Tradicional.{/cps}"
    with fastDissolve
    S "{cps=40}No entanto, percebemos que, mesmo no nicho bem previsível das Padarias, existem projetos que exigem um alto grau de adaptação às mudanças...{/cps}"    
    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}O que você acha? Quando digo Tradicional, você entende do que eu estou falando?{/cps}"

    menu:
        "Sim":
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Que bom, você ganhou um ponto comigo."
        "Não":
            show supervisor disappointed at right
            with fastDissolve
            P "{cps=40}Quando digo metodologia Tradicional, estou falando do UP – {i}{b}Unified Process{/b}{/i}, ou do IRUP – {i}{b}IBM Rational Unified process{/b}{/i}, da IBM.{/cps}"
            show rup at imagepos behind supervisor:
                alpha 0.0
                time 0
                linear 1.0 alpha 1.0
            show supervisor normal3 at right
            P "{cps=40}Se você quiser se dar bem aqui, sugiro que aprenda mais sobre o {i}{b}RUP{/b}{/i}.{/cps}"
            hide rup            

    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}E quanto as metodologias ágeis: Você já ouviu falar do{i}{b} XP{/b}{/i}?{/cps}"
    
    menu:
        "Sim":
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Estou gostando de ver. Vejo que formou-se na {b}UFMG{/b}. Você deve ter estudado com o Professor {b}Rodolfo{b}.{/cps}"
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
    S "{cps=40}Portanto, agora você já sabe. A {b}{i}PadaSoft{/i}{/b} desenvolve produtos de qualidade nessas duas vertentes. Temos duas grandes famílias aqui!{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}No lado Ágil, seguimos o processo {b}{i}PadaOne{/i}{/b}{image=sabre.png}, e no Tradicional, o processo {b}{i}PadaTout{/i}{/b}{image=baguette.png}.{/cps}"
    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Com qual deles você se identifica mais?{/cps}"

    menu:
        "Ágil":
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Que sorte a sua.{/cps}"
            show supervisor normal3 at right
            with fastDissolve
            S "{cps=40}A PadaOne está desenvolvendo um projeto incrível!{/cps}"
            S "{cps=40}Trata-se de um software para a padaria {b}{i}Mestre do Bolo{/i}{/b}.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}O cliente é muito exigente e muda de ideia a todo momento.{/cps}"
            S "{cps=40}Então abracem as mudanças.{w=2} Dediquem-se às histórias do cliente e às entregas contínuas.{/cps}"

        "Tradicional":
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Hmm, ok. Não identifica-se com os ágeis...{/cps}"
            show supervisor smile at right
            S "{cps=40}Então, você é {b}{i}lerdo{/i}{/b}?!{w=2} Brincadeira...{/cps}"
            with fastDissolve
            S "{cps=40}A PadaTout está dedicando-se ao projeto para a padaria {b}{i}Et part deux{/i}{/b}.{/cps}"      
            show supervisor normal3 at right
            with fastDissolve
            S "{cps=40}O cliente sabe exatamente o que ele quer.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Então não se preocupe com as mudanças.{w=2} Dediquem-se ao levantamento de requisitos eficiente.{/cps}"

    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Meu caro, {color=ff0000}{b}[nome]{/color}{/b}.{w=2} Adotar essas duas abordagens de desenvolvimento, Tradicional e Ágil, trouxe-nos muitas vantagens como você irá perceber.{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}Por outro lado, um clima de competição saudável emergiu entre a {b}{i}PadaTout{/i}{/b} e a {b}{i}PadaOne{/i}{/b}.{/cps}"
    show supervisor smile at right
    with fastDissolve
    S "{cps=40}Então, esteja preparado!!!{/cps}"
    
    $ renpy.music.stop(channel="music",fadeout=1.0)
    #show black
    
    #with blinds
    jump rSupervisorScene
    #transição proxima cena...
