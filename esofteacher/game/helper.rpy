## Cena do help

image sylvie normal = "sylvie2_normal.png"
image sylvie giggle = "sylvie2_giggle.png"
image sylvie smile = "sylvie2_smile.png"
image sylvie surprised = "sylvie2_surprised.png" 

define h = Character(
                    window_left_padding = 15,
                    window_right_padding = 10,
                    window_top_padding = 30,
                    what_slow_caps = 20,
                    show_side_image = Image ("Helper.png", xalign = 0.01, yalign = 0.81))

image help = "help.jpg"


label helps:
    
    stop music fadeout 1.0
    $ renpy.music.play("bgmfum.wav", channel="music", loop=True, fadein=1.0)
    scene help                           # alterar
    
    show sylvie smile at left
    
    h "{cps=40}Olá, eu me chamo Helper e irei lhe ensinar sobre o funcionamento do jogo. ^-^{/cps}"
    
    show sylvie normal at left
    with fastDissolve
    h "{cps=40}Para avançar pelo jogo, use o botão esquerdo do mouse ou pressione as teclas espaço ou enter.{/cps}"
    
    label testMenu:
        
        show sylvie normal at left
        with fastDissolve
        
        h "{cps=40}Em um menu, use o botão esquerdo do mouse para fazer uma escolha, ou use as setas do teclado para escolher uma opção e pressione enter para ativá-la.{/cps}"
        h "{cps=40}Vamos fazer um teste.{/cps}"
        
        h "{cps=40}Você compreendeu o funcionamento?{/cps}"
        
        menu:
            with fastDissolve
            "Sim":
                show sylvie giggle at left
                with fastDissolve
                h "{cps=40}Parabéns!{/cps}" 
            "Não":
                show sylvie surprised at left
                with dissolve
                h "{cps=40}Que pena, leia atentamente as instruções. ^-^{/cps}" 
                jump testMenu
                
            
        show sylvie normal at left
        with fastDissolve                
        h "{cps=40}Durante o jogo, use o botão direito do mouse ou pressione a tecla Esc para ir ao Menu de Jogo.{/cps}" 
        h "{cps=40}O menu de jogo exibe as seguintes escolhas.{/cps}"
        "{cps=40}{b}Voltar:{/b} Retorna ao jogo.\n{b}Salvar Jogo:{/b} Permite que você salve o jogo.\n{b}Carregar Jogo:{/b} Permite que você carregue um jogo salvo anteriormente. Clicar em \"{i}Automáticos{/i}\" acessa os jogos salvos automaticamente\n{b}Preferências:{/b} Altera as preferências (opções/configuração) do jogo\n{b}Menu Principal:{/b} Volta ao menu principal, e termina o jogo atual.\n{b}Ajuda:{/b} Exibe esta tela.\n{b}Sair:{/b} Sai do jogo; o jogo será terminado.{/cps}"
        show sylvie smile at left
        with fastDissolve
        h "{cps=40}Agora você pode começar a jogar e aprender sobre e engenharia de software. *-*{/cps}"
        h "{cps=40}Deseja começar a jogar?{/cps}"
        
        menu:
            with fastDissolve
            "Sim":
                h "{cps=40}Até a próxima! =D{/cps}"
                jump start
            "Não":
                show sylvie giggle at left
                with fastDissolve
                h "{cps=40}Você será levado ao Menu Principal, até a próxima! =D{/cps}" 
    return
