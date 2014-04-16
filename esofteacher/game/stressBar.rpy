init:
    $ lv = 0 
    $ stress = 0
    $ stressMax = 40
    $ nome = ""
    
init python:

    def stats_frame(nome, level, stress, stressMax, **properties):

        ui.frame(xfill=False, yminimum=None, **properties)

        ui.hbox() # (name, "HP", bar) from (level, hp, maxhp)
        ui.vbox() # name from ("HP", bar)

        ui.text(nome, size=20)

        ui.hbox() # "HP" from bar
        ui.text("Stress ", size=20)
        ui.bar(stressMax, stress,xmaximum=150)

        ui.close()
        ui.close()

        ui.vbox() # Level from (hp/maxhp)

        ui.text("Lv. %d" % level, xalign=0.5, size=20)
        ui.text("%d/%d" % (stress, stressMax), xalign=0.5, size=20)

        ui.close()
        ui.close()
        
    renpy.define_screen("stressBar", stats_frame, modal="False")