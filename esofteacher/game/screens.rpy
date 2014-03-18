﻿# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say:

    # Defaults for side_image and two_window
    default side_image = None
    default two_window = False

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input:

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl:

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu:

    tag menu
    window:
        style "mm_root"
    
    imagebutton idle "main_play_idle.png" hover "main_play_hover.png" xpos 450 ypos 340 focus_mask True activate_sound "click_sound.mp3" action Start()
    imagebutton idle "main_load_idle.png" hover "main_load_hover.png" xpos 700 ypos 450 focus_mask True activate_sound "click_sound.mp3" action ShowMenu("load")
    imagebutton idle "main_settings_idle.png" hover "main_settings_hover.png" xpos 190 ypos 450 focus_mask True activate_sound "click_sound.mp3" action ShowMenu("preferences")
    imagebutton idle "main_quit_idle.png" hover "main_quit_hover.png" xpos 450 ypos 550 focus_mask True  activate_sound "click_sound.mp3" action Quit(confirm = False)

init -2 python:

    # Make all the menu buttons the same size.
    style.mm_button.size_group = "mm"
    

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Voltar") action Return()
        textbutton _("Preferências") action ShowMenu("preferences")
        textbutton _("Salvar Jogo") action ShowMenu("save")
        textbutton _("Carregar Jogo") action ShowMenu("load")
        textbutton _("Menu Principal") action MainMenu()
        textbutton _("Ajuda") action Help()
        textbutton _("Sair") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker:

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Página Anterior"):
                action FilePagePrevious()

            textbutton _("Automáticos"):
                action FilePage("auto")

            textbutton _("Rápidos"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Pŕoxima Página "):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Vazio."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

screen load:

    # This ensures that any other menu screen is replaced.
    tag menu

    use navigation
    use file_picker

init -2:
    style file_picker_frame is menu_frame
    style file_picker_nav_button is small_button
    style file_picker_nav_button_text is small_button_text
    style file_picker_button is large_button
    style file_picker_text is large_button_text


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences:

    tag menu

    # Include the navigation.
    use navigation

    # Put the navigation columns in a three-wide grid.
    grid 3 1:
        style_group "prefs"
        xfill True

        # The left column.
        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Modo de Exibição")
                textbutton _("Janela") action Preference("display", "window")
                textbutton _("Tela cheia") action Preference("display", "fullscreen")

            frame:
                style_group "pref"
                has vbox

                label _("Transições")
                textbutton _("Todas") action Preference("transitions", "all")
                textbutton _("Nenhuma") action Preference("transitions", "none")

            frame:
                style_group "pref"
                has vbox

                label _("Velocidade do Texto")
                bar value Preference("text speed")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Joystick...") action Preference("joystick")


        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Pular mensagens")
                textbutton _("Apenas as já vistas") action Preference("skip", "seen")
                textbutton _("Todas") action Preference("skip", "all")

            frame:
                style_group "pref"
                has vbox

                textbutton _("Pule mensagens agora") action Skip()

            frame:
                style_group "pref"
                has vbox

                label _("Após Escolhas")
                textbutton _("Pare de pular mensagens") action Preference("after choices", "stop")
                textbutton _("Continue pulando mensagens") action Preference("after choices", "skip")

            frame:
                style_group "pref"
                has vbox

                label _("Atraso de auto-avanço")
                bar value Preference("auto-forward time")

                if config.has_voice:
                    textbutton _("Esperar Voz") action Preference("wait for voice", "toggle")

        vbox:
            frame:
                style_group "pref"
                has vbox

                label _("Volume de Música")
                bar value Preference("music volume")

            frame:
                style_group "pref"
                has vbox

                label _("Volume de Som")
                bar value Preference("sound volume")

                if config.sample_sound:
                    textbutton _("Testar"):
                        action Play("sound", config.sample_sound)
                        style "soundtest_button"

            if config.has_voice:
                frame:
                    style_group "pref"
                    has vbox

                    label _("Volume de Voz")
                    bar value Preference("voice volume")

                    textbutton _("Sustentar Voz") action Preference("voice sustain", "toggle")
                    if config.sample_voice:
                        textbutton _("Testar"):
                            action Play("voice", config.sample_voice)
                            style "soundtest_button"

init -2:
    style pref_frame:
        xfill True
        xmargin 5
        top_margin 5

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 192
        xalign 1.0

    style soundtest_button:
        xalign 1.0


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    modal True

    window:
        style "gm_root"

    frame:
        style_group "yesno"

        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Sim") action yes_action
            textbutton _("Não") action no_action

    # Right-click and escape answer "no".
    key "game_menu" action no_action

init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:

    # Add an in-game quick menu.
    hbox:
        style_group "quick"

        xalign 1.0
        yalign 1.0

        textbutton _("Voltar") action Rollback()
        textbutton _("Salvar") action ShowMenu('save')
        textbutton _("Salve R.") action QuickSave()
        textbutton _("Carrege R.") action QuickLoad()
        textbutton _("Pular") action Skip()
        textbutton _("Pular Rápido") action Skip(fast=True, confirm=True)
        textbutton _("Auto-Avanço") action Preference("auto-forward", "toggle")
        textbutton _("Preferências") action ShowMenu('preferences')

init -2:
    style quick_button:
        is default
        background None
        xpadding 5

    style quick_button_text:
        is default
        size 12
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

