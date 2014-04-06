## Cena do help

define h = Character(
                    window_left_padding = 15,
                    window_right_padding = 10,
                    window_top_padding = 30,
                    what_slow_caps = 20,
                    show_side_image = Image ("Helper.png", xalign = 0.01, yalign = 0.81))

image dig = "dig.jpg"


label helps:
    
    stop music fadeout 1.0
    play music "bgmfum.wav" fadein 1.0 
    scene dig                           # alterar
    
    show sylvie smile at left
    h "{cps=40}Olá, eu me chamo Helper e irei lhe ensinar sobre o funcionamento do jogo ^-^{/cps}"
    show sylvie normal at left
    with fastDissolve
    h "{cps=40}Para avançar pelo jogo, use o botão esquerdo do mouse ou pressione as teclas espaço ou enter{/cps}"
    
    label testMenu:
        show sylvie normal at left
        with fastDissolve
        h "{cps=40}Em um menu, use o botão esquerdo do mouse para fazer uma escolha, ou use as setas do teclado para escolher uma opção e pressione enter para ativá-la{/cps}"
        h "{cps=40}Vamos fazer um teste{/cps}"
        
        h "{cps=40}Você compreendeu o funcionamento?{/cps}"
        
        menu:
            with fastDissolve
            "Sim":
                h "{cps=40}Parabéns!!!{/cps}" 
                
            "Não":
                show sylvie surprised at left
                with dissolve
                h "{cps=40}Que pena, leia atentamente as instruções ^-^{/cps}" 
                jump testMenu
                        
        h "{cps=40}Durante o jogo, use o botão direito do mouse ou pressione a tecla Esc para ir ao Menu de Jogo{/cps}" 
        h "{cps=40}O menu de jogo exibe as seguintes escolhas{/cps}"
        h "{cps=40}{b}Voltar:{/b} Retorna ao jogo.\n{b}Salvar Jogo:{/b} Permite que você salve o jogo.\n{b}Carregar Jogo:{/b} Permite que você carregue um jogo salvo anteriormente. Clicar em \"{i}Automáticos{/i}\" acessa os jogos salvos automaticamente{/cps}"


    return