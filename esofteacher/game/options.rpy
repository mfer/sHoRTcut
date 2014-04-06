## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = True

    ## These control the width and height of the screen.

    config.screen_width = 1280
    config.screen_height = 720

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"ESofTeacher"

    # These control the name and version of the game, that are reported
    # with tracebacks and other debugging logs.
    config.name = "ESofTeacher"
    config.version = "0.0"

    #########################################
    # Themes

    ## We then want to call a theme function. theme.roundrect is
    ## a theme that features the use of rounded rectangles. 
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.regal(
        ## Theme: Regal
        ## Color scheme: Easter Baby

        ## The color of an idle widget face.
        widget = "#F5D4EE",

        ## The color of a focused widget face.
        widget_hover = "#F0DDFF",

        ## The color of the text in a widget.
        widget_text = "#698071",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#000000",

        ## The color of a disabled widget face.
        disabled = "#DDE9FF",

        ## The color of disabled widget text.
        disabled_text = "#A6AFBF",

        ## The color of informational labels.
        label = "#698071",

        ## The color of a frame containing widgets.
        frame = "#CCF8DC",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.

        mm_root = "school2.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.

        gm_root = "school1.png",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    ## style.window.background = Frame("gtathrones.jpg", 12, 12)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is
    ## drawn.

    # style.window.left_padding = 6
    # style.window.right_padding = 6
    # style.window.top_padding = 6
    # style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins
    ## and padding.

    # style.window.yminimum = 250


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    ##style.mm_menu_frame.xpos = 0.5
    ##style.mm_menu_frame.xanchor = 0.5
    ##style.mm_menu_frame.ypos = 0.75
    ##style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    # style.default.font = "DejaVuSans.ttf"

    ## The default size of text.

    # style.default.size = 22

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to True if the game has voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    style.button.activate_sound = "click_sound.mp3"
    ## style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    ## config.enter_sound = "click_sound.mp3"
    ## config.exit_sound = "click_sound.mp3"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "test_sound.mp3"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "illurock.ogg"
    
    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.
    ## config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = None

    ## Used when exiting the game menu to the game.
    config.exit_transition = None

    ## Used between screens of the game menu.
    config.intra_transition = None

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = None

    ## Used when returning to the main menu from the game.
    config.game_main_transition = None

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = None

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = None

    ## Used when a game is loaded.
    config.after_load_transition = None

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None

    ## Used when showing NVL-mode text directly after ADV-mode text.
    config.adv_nvl_transition = dissolve

    ## Used when showing ADV-mode text directly after NVL-mode text.
    config.nvl_adv_transition = dissolve

    ## Used when yesno is shown.
    config.enter_yesno_transition = None

    ## Used when the yesno is hidden.
    config.exit_yesno_transition = None

    ## Used when entering a replay
    config.enter_replay_transition = None

    ## Used when exiting a replay
    config.exit_replay_transition = None

    ## Used when the image is changed by a say statement with image attributes.
    config.say_attribute_transition = None

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persistent information can be found by the init code.)
python early:
    config.save_directory = "a-1394747942"

init -3 python:
    if persistent.lang is None:
        persistent.lang = "portuguese"

    lang = persistent.lang

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = True

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 20

    ## The default auto-forward time setting.

    config.default_afm_time = 10

    #########################################
    ## More customizations can go here.


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-alpha', the windows distribution will be in the
    ## directory 'mygame-alpha-win', in the 'mygame-alpha-win.zip' file.
    build.directory_name = "esofteacher-prototype"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "esofteacher"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    
    # Translatable strings found in common/00developer.rpy

    config.translations[u'Developer Menu'] = u'Menu de Desenvolvedor'
    config.translations[u'Return to the developer menu'] = u'Voltar para o menu de desenvolvedor'

    # Translatable strings found in common/00library.rpy

    config.translations[u'Skip Mode'] = u'Modo Avanço'
    config.translations[u'Fast Skip Mode'] = u'Modo Avanço Rápido'
    config.translations[u"While Ren'Py games may be playable without the renpy module, some features may be disabled. For more information, read the module/README.txt file or go to http://www.bishoujo.us/renpy/."] = u"Apesar de que jogos Ren'Py podem ser jogados sem o módulo renpy alguns recursos podem ser desabilitados. Para mais informação, leia o arquivo module/README.txt ou vá para http://www.bishoujo.us/renpy/."
    config.translations[u'renpy module not found.'] = u'módulo renpy não encontrado.'
    config.translations[u'The renpy module could not be loaded on your system.'] = u'O módulo renpy não pôde ser carregado em seu sistema.'
    config.translations[u'Old renpy module found.'] = u'Módulo renpy antigo encontrado.'
    config.translations[u"An old version (%d) of the Ren'Py module was found on your system, while this game requires version %d."] = u"Uma versão antiga (%d) do módulo Ren'Py foi encontrada em seu sistema, mas este jogo requer a versão %d."
    config.translations[u'Please click to continue.'] = u'Por favor, clique para continar.'

    # Translatable strings found in common/00menus.rpy

    config.translations[u'Start Game'] = u'Iniciar Jogo'
    config.translations[u'Continue Game'] = u'Continuar Jogo'
    config.translations[u'Preferences'] = u'Preferências'
    config.translations[u'Quit'] = u'Sair'
    config.translations[u'Return'] = u'Retornar'
    config.translations[u'Save Game'] = u'Salvar Jogo'
    config.translations[u'Load Game'] = u'Carregar Jogo'
    config.translations[u'Main Menu'] = u'Menu Principal'
    config.translations[u'Are you sure you want to quit?'] = u'Tem certeza de que você deseja sair?'
    config.translations[u'Are you sure you want to return to the main menu?\nThis will lose unsaved progress.'] = u'Tem certeza de que você quer retornar ao menu principal?\nVocê perderá qualquer progresso que ainda não tenha sido salvo.'

    # Translatable strings found in common/_layout/one_column_preferences.rpym

    config.translations[u'Display'] = u'Exibição'
    config.translations[u'Transitions'] = u'Transições'
    config.translations[u'Skip'] = u'Avanço'
    config.translations[u'Begin Skipping'] = u'Iniciar Avanço'
    config.translations[u'After Choices'] = u'Depois das Escolhas'
    config.translations[u'Text Speed'] = u'Velocidade de Texto'
    config.translations[u'Auto-Forward Time'] = u'Auto-Avançar Tempo'
    config.translations[u'Music Volume'] = u'Volume de Música'
    config.translations[u'Sound Volume'] = u'Volume de Som'
    config.translations[u'Voice Volume'] = u'Volume de Voz'
    config.translations[u'Joystick...'] = u'Joystick...'

    # Translatable strings found in common/_layout/classic_yesno_prompt.rpym

    config.translations[u'Yes'] = u'Sim'
    config.translations[u'No'] = u'Não'

    # Translatable strings found in common/_layout/scrolling_load_save.rpym

    config.translations[u'Empty Slot.'] = u'Espaço Vazio.'
    config.translations[u'Are you sure you want to overwrite your save?'] = u'Tem certeza de que você deseja sobrescrever o jogo salvo?'
    config.translations[u'Loading will lose unsaved progress.\nAre you sure you want to do this?'] = u'Carregar fará você perder qualquer progresso que ainda não tenha salvo.\nTem certeza de que quer fazer isso?'
    config.translations[u'Are you sure you want to delete this save?'] = u'Tem certeza de que você deseja deletar o jogo salvo?'
    config.translations[u'q'] = u'q' # Prefixo para nomes dos 'quick saves'
    config.translations[u'a'] = u'a'# Prefixo para nomes dos 'auto saves'

    # Translatable strings found in common/_layout/classic_joystick_preferences.rpym

    config.translations[u'Not Assigned'] = u'Não Atribuído'
    config.translations[u'Joystick Mapping'] = u'Mapeamento de Joystick'
    config.translations[u'Left'] = u'Esquerda'
    config.translations[u'Right'] = u'Direita'
    config.translations[u'Up'] = u'Cima'
    config.translations[u'Down'] = u'Baixo'
    config.translations[u'Select/Dismiss'] = u'Selecionar/Recusar'
    config.translations[u'Rollback'] = u'Voltar'
    config.translations[u'Hold to Skip'] = u'Segure para Avançar'
    config.translations[u'Toggle Skip'] = u'Avançar ligado/desligado'
    config.translations[u'Hide Text'] = u'Esconder Texto'
    config.translations[u'Menu'] = u'Menu'
    config.translations[u'Move the joystick or press a joystick button to create the mapping. Click the mouse to remove the mapping.'] = u'Mova o joystick ou pressione um botão do joystick para criar um mapeamento. Clique o mouse para remover o mapeamento.'

    # Translatable strings found in common/_layout/classic_preferences_common.rpym

    config.translations[u'Test'] = u'Testar'
    config.translations[u'Window'] = u'Janela'
    config.translations[u'Fullscreen'] = u'Tela Cheia'
    config.translations[u'All'] = u'Todos(as)'
    config.translations[u'Some'] = u'Alguns(umas)'
    config.translations[u'None'] = u'Nenhum(a)'
    config.translations[u'Seen Messages'] = u'Mensagens já vistas'
    config.translations[u'All Messages'] = u'Todas as Mensagens'
    config.translations[u'Stop Skipping'] = u'Parar de Avançar'
    config.translations[u'Keep Skipping'] = u'Continuar a Avançar'

    # Translatable strings found in common/_layout/classic_load_save.rpym

    config.translations[u'Auto'] = u'Automático'
    config.translations[u'Quick'] = u'Rápido'
    config.translations[u'Previous'] = u'Anterior'
    config.translations[u'Next'] = u'Próximo'

    # Translatable strings found in common/_compat/gamemenu.rpym

    config.translations[u'The error message was:'] = u'A mensagem de erro era:'
    config.translations[u'You may want to try saving in a different slot, or playing for a while and trying again later.'] = u'Você pode tentar salvar em um espaço diferente, ou jogar um pouco e tentar novamente mais tarde.'
    config.translations[u'Save Failed.'] = u'Salvamento Falhou.'

    # Translatable strings found in common/_compat/preferences.rpym

    config.translations[u'Joystick Configuration'] = u'Configuração do Joystick'

