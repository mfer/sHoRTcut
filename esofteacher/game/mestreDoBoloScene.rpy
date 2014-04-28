
#background

image mb0 = "mb0.gif"
image mb1 = "mb1.gif"
image mb2 = "mb2.gif"
image mb3 = "mb3.gif"
image mb4 = "mb4.gif"
image mb5 = "mb5.gif"
image mb6 = "mb6.gif"
image mb7 = "mb7.gif"
image mb8 = "mb8.gif"
image mb9 = "mb9.gif"
image mb10 = "mb10.gif"
image mb11 = "mb11.gif"

label mestreDoBoloScene:
    
    $ renpy.music.stop(channel="music",fadeout=1.0)    
    $ renpy.music.play("Purple_Motion_-_Charts_overdrive.mp3", channel="music", loop=True, fadein=1.0) 
    
    
    MB "{cps=40}Olá, {b}{i}[nome]!!!{/i}{/b}{w=2} Você é o novo contratado, não é?{/cps}"
    MB "{cps=40}Prazer em conhecê-lo!{/cps}" 
    MB "{cps=40}Sou o líder do processo PadaOne, que utiliza uma metodologia ágil.{/cps}"
    
    MB "{cps=40}Sua tarefa será participar do desenvolvimento do programa para atender à necessidade do nosso cliente.{/cps}" 
    MB "{cps=40}O projeto está bem no início, vamos planejar nossa primeira corrida daqui a pouco.{/cps}"
    MB "{cps=40}O sistema será desenvolvido em módulos.{w=2} Não sabemos ainda qual será o primeiro módulo, mas vamos no cliente em breve. {/cps}"
    
    MB "{CPS=40}Sei que está trabalhando em outro projeto também, mas se puder ir conosco será ótimo!{/cps}"
    MB "{cps=40}Assim que estiver arrumado suas coisas, basta vir até a nossa equipe para colocarmos a {b}{i}“mão na massa”{/b}{/i}{/cps}"