# Project Screen

# Tentarei acrescentar o progresso tmb
init:
    $ variable = True #Variavel q faz esta janela aparecer
    $ agileProgress = 0
    $ tradProgress = 0
    
screen project: 
    if variable:    
        vbox xalign 0.98 yalign 0.0:
            textbutton "Progresso dos Projetos" action ui.callsinnewcontext("label_call")

            imagebutton:
                idle "button_idle.png"
                hover "button_hover.png"
                action ui.callsinnewcontext("label_call")
                
                
screen projects_screen:
    frame:
        has vbox
        hbox:
            label "{b}Ágil:           {/b}" xminimum 100
            bar range 100 value agileProgress xmaximum 400
        hbox:
            label "{b}Tradicional: {/b}" xminimum 100
            bar range 100 value tradProgress xmaximum 400
        textbutton "{i}Return{/i}" action Return()
        

label label_call:
    call screen projects_screen
    return
