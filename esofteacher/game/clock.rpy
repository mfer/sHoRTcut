image clock = "clock.png" # Short Clockhand
image clock_1 = "clock_1.png" # Long Clockhand
image clock_2 = "clock_2.png" # Clockface

init:
    $ minutes = 0

transform rotateshort:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5
    rotate (minutes*6)
    
transform rotatelong:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5
    rotate (minutes*0.5)

transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade in the clock.

style transparente:
    background "a.png"
    
screen clock:
       
    frame at alpha_dissolve:
        style "transparente"
        xmaximum 150 # X size of clock graphic
        ymaximum 150 # Y size of clock graphic
        xalign 0.99 # X placement on screen
        yalign 0.02 # Y placement on screen
        add "clock_2"
        add "clock_1" at rotatelong
        add "clock" at rotateshort