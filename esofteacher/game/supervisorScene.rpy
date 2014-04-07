#CenaDoSupervisor

label supervisorScene:
    
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
    S "{cps=40}Nossa empresa, {b}{i}PadaSoft{/i}{/b}, é referência no desenvolvimento de {b}{i}CRUDs{/i}{/b} para gerenciamento de Padarias.{/cps}"
        
    S "{cps=40}Somos uma empresa que seguia apenas a metodologia tradicional. Você entende do que eu estou falando?{/cps}"

    menu:
        "Sim":
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Que bom, você ganhou um ponto comigo."
        "Não":
            show supervisor7 at right
            with fastDissolve
            P "{cps=40}Quando digo metodologia tradicional, estou falando do UP – {i}{b}Unified Process{/b}{/i}, ou do IRUP – {i}{b}IBM Rational Unified process{/b}{/i}, da IBM.{/cps}"
            P "{cps=40}Se você quiser se dar bem aqui, sugiro que aprenda mais sobre o {i}{b}RUP{/b}{/i}.{/cps}"

    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}No entanto, há pouco tempo, estamos experimentando outras metodologias… Você já ouviu falar do{i}{b} XP{/b}{/i}?{/cps}"
    
    menu:
        "Sim":
            show supervisor smile at right
            with fastDissolve
            S "{cps=40}Estou gostando de ver. Vejo que vem da {b}UFMG{/b}. Você deve ter estudado com o Professor Rodolfo.{/cps}"
        "Não":
            show supervisor7 at right
            with fastDissolve
            P "{cps=40}Então não poderá dizer que não aprendeu nada aqui.{/cps}"
            show supervisor pensive at right
            with fastDissolve
            P "{cps=40}Basicamente, o {b}{i}XP{/i}{/b} auxilia a desenvolver software com requisitos vagos e em constante mudança.{/cps}"

    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Sendo assim a {b}{i}PadaSoft{/i}{/b} desenvolve produtos de qualidade nessas duas vertentes.{/cps}"
    show supervisor pensive at right
    with fastDissolve
    S "{cps=40}No método ágil seguimos o processo {b}{i}PadaOne{/i}{/b}, enquanto no tradicional, o processo é o {b}{i}PadaTout{/i}{/b}.{/cps}"
    show supervisor normal3 at right
    with fastDissolve
    S "{cps=40}Com qual método você se identifica mais?{/cps}"

    menu:
        "Ágil":
            S "{cps=40}Que sorte a sua.{/cps}"
            S "{cps=40}Estamos desenvolvendo um projeto com esta metodologia.{/cps}"
            S "{cps=40}Se trata de um software para a padaria {b}{i}Mestre do Bolo{/i}{/b}.{/cps}"
            S "{cps=40}O cliente é muito exigente e muda de ideia a todo momento.{/cps}"
            S "{cps=40}Então abrace as mudanças.{w=2} Dedique-se a entregas contínuas.{/cps}"

        "Tradicional":
            S "{cps=40}Hmm, ok.{/cps}"
            S "{cps=40}Então, você é um lerdo.{/cps}"
            S "{cps=40}Temos muitos iguais a você.{/cps}" 
            S "{cps=40}Até resolvemos montar uma equipe para os seus semelhantes.{/cps}" 
            S "{cps=40}Vocês trabalharão com o projeto para a padaria {b}{i}Et part deux{/i}{/b}.{/cps}"      
            S "{cps=40}O cliente sabe exatamente o que ele quer.{/cps}"
            S "{cps=40}Então não se preocupe com as mudanças.{w=2} Dediquem-se para fazer um bom levantamento de requisitos.{/cps}"

    S "{cps=40}Meu caro, {color=ff0000}{b}[nome]{/color}{/b}.{w=2} Veja bem. Adotar essas duas abordagens de desenvolvimento trouxe-nos muitas vantagens como você irá perceber.{/cps}"
    S "{cps=40}Por outro lado, clima de competição (muitas vezes não muito saudável) emergiu entre as duas equipes: {b}{i}PadaOne{/i}{/b} e {b}{i}PadaTout{/i}{/b}.{/cps}"
    S "{cps=40}So, be ready!{/cps}" 
    #transição proxima cena...