#CenaDoSupervisor

image xp = "Extreme_Programming.png"
image waterfall = "800px-Waterfall_model.png"

image supervisor normal0 = "supervisor0.png" 
image supervisor normal1 = "supervisor1.png"
image supervisor anger = "supervisor2.png"
image supervisor normal3 = "supervisor3.png"
image supervisor pensive = "supervisor4.png"
image supervisor smile = "supervisor5.png"
image supervisor6 = "supervisor6.png"
image supervisor disappointed = "supervisor7.png"


label supervisorScene:


    $ renpy.music.play("A Journey Awaits.ogg", channel="music", loop=True, fadein=1.0)
      
    define imagepos = Position(xpos=.25, xanchor=0, ypos=50, yanchor=0)
    define imagepos2 = Position(xpos=.05, xanchor=0, ypos=50, yanchor=0)

    $ strss += 5
    show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
    
    scene office
    
    show supervisor normal1 at right 
    S "{cps=40}Olá, então você é o novo contratado?{/cps}"
    menu:
        
        "Sim":
            show supervisor normal3 at right
            with fastDissolve
            P "{cps=40}Sim, eu me chamo...{/cps}"
            $ nome = renpy.input("{b}{i}Por favor digite o seu nome:{/i}{/b}", "", length=20) or _("Jogador Tímido")
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Muito prazer, {b}{color=ff0000}[nome]{/color}{/b}!\nSeja bem vindo! Não quero te assustar mas…{w=3} Temos muito trabalho por aqui. Vou explicar o que você vai fazer.{/cps}"
        "Não":
            show supervisor anger at right
            with fastDissolve
            S "{cps=40}Então o que você está fazendo aqui?{/cps}"
            return
  
    $ strss += 5
    show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente

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
            $ strss = strss - 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Que bom, você ganhou um ponto comigo.{/cps}"
        "Não":
            $ strss += 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
            show supervisor disappointed at right
            with fastDissolve
            P "{cps=40}Quando digo metodologia Tradicional, estou falando do modelo de Desenvolvimento em Cascata.{/cps}"
            show waterfall at imagepos2 behind supervisor:
                alpha 0.0
                time 0
                linear 1.0 alpha 1.0
            show supervisor normal3 at right
            P "{cps=40}No qual concepção, iniciação, análise, desenho, construção, teste, produção/implementação e manutenção ocorrem linearmente sem realimentações ou iterações.{/cps}"
            P "{cps=40}Se você quiser se dar bem aqui, sugiro que aprenda mais sobre ele. Inclusive a controversa história de como ele surgiu!{/cps}"
            hide waterfall

    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}E quanto as metodologias ágeis: Você já ouviu falar do{i}{b} XP{/b}{/i}?{/cps}"
    
    menu:
        "Sim":
            $ strss = strss - 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Estou gostando de ver. Vejo que formou-se na {b}UFMG{/b}. Você deve ter estudado com o Professor {b}Rodolfo{/b}.{/cps}"
        "Não":
            $ strss += 5
            show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)  #não consegui fazer atualizar automaticamente
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
            S "{cps=40}Que sorte a sua!{/cps}"
            show supervisor normal3 at right
            with fastDissolve
            S "{cps=40}A PadaOne está desenvolvendo um projeto incrível!{w=2} Trata-se de um software para a confeitaria {b}{i}Mestre do Bolo{/i}{/b}.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}O cliente é muito exigente e muda de ideia a todo momento.{/cps}"
            S "{cps=40}Então abracem as mudanças.{w=2} Dediquem-se às histórias do cliente e às entregas contínuas.{/cps}"

        "Tradicional":
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Hum, o.k. Não identifica-se com os ágeis...{/cps}"
            show supervisor smile at right
            S "{cps=40}Então, você é {b}{i}lerdo{/i}{/b}?!{w=2} Brincadeira...{/cps}"
            with fastDissolve
            S "{cps=40}A PadaTout está dedicando-se ao projeto para a padaria {b}{i}Et Part Deux{/i}{/b}.{/cps}"      
            show supervisor normal3 at right
            with fastDissolve
            S "{cps=40}O cliente sabe exatamente o que ele quer.{w=2} Então não se preocupe com as mudanças.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            S "{cps=40}Dediquem-se ao levantamento de requisitos eficiente.{w=2} E muito cuidado com os não-funcionais...{/cps}"

    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Meu caro, {color=ff0000}{b}[nome]{/b}{/color}.{w=2} Adotar essas duas abordagens de desenvolvimento, Tradicional e Ágil, trouxe-nos muitas vantagens como você irá perceber.{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}Por outro lado, um clima de competição saudável emergiu entre a {b}{i}PadaTout{/i}{/b} e a {b}{i}PadaOne{/i}{/b}.{/cps}"
    show supervisor smile at right
    with fastDissolve
    S "{cps=40}Esteja preparado! Você irá participar dos dois projetos...{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}Peço que agora você decida com qual equipe começará.{w=5} Ah! {w=2}Estarei aqui para o que você precisar desde que não faça barulho enquanto come.{/cps}"
    
    $ renpy.music.stop(channel="music",fadeout=1.0)
    #show black
    
    #with blinds
    jump rSupervisorScene
    #transição proxima cena...
