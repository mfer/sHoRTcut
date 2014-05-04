#Momento1: Indo para o cliente

label corrida1SceneMomento1:
    
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

