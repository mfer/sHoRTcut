# Project Screen

init:
    $ variable = False
    
screen button: 
    if variable:    
        vbox xalign 0.98 yalign 0.0:
            textbutton "Escolha do Projeto" action ui.callsinnewcontext("label_call")

            imagebutton:
                idle "button_idle.png"
                hover "button_hover.png"
                action ui.callsinnewcontext("label_call")
                
                
screen projects_screen:
    frame:
        xfill True
        xmargin 50
        ypadding 25
        xalign .50
        yalign .50
        
        vbox:
            xfill True
            spacing 25
            
            text "Qual projeto vc quer fazer?": #arrumar
                text_align 0.5
                xalign 0.5
        #has vbox
            hbox:
                spacing 10
                xalign .5
                textbutton "Ágil" action Return() #Alterar
                textbutton "Tradicional" action Return() # Alterar
                textbutton "Retornar" action Return()

label label_call:
    call screen projects_screen
    return
