# novo tipo de transicao
define fastDissolve = Dissolve (.2)

image bg ync = "ync.png"
image office = "office.png"
image corredor = "corredor.png"
image bakery2 = "bakery2.png"
image bakery1 = "bakery1.png"
image supervisor normal0 = "supervisor0.png" 
image supervisor normal1 = "supervisor1.png"
image supervisor anger = "supervisor2.png"
image supervisor normal3 = "supervisor3.png"
image supervisor pensive = "supervisor4.png"
image supervisor smile = "supervisor5.png"
image supervisor6 = "supervisor6.png"
image supervisor disappointed = "supervisor7.png"

# Declare characters used by this game.
define e = Character('ESOFteacher', color="#c8ffc8")
define S = Character('Supervisor', color="#c8ffc8")

define P = Character('Jogador', color="#c8ffc8")        

define MB = Character('Mestre do Bolo', color="#c8ffc8") #mestredobolo as mb
define GR = Character ('Gerente', color="#c8ffc8") #define gerente as gr

define DP = Character ('Dono do Produto', color="#c8ffc8") 

define CL = Character ('Confeiteiro da Mestre do Bolo', color="#c8ffc8")


# The game starts here.
label start:    
    
    stop music fadeout 1.0
    
    show screen stressBar(nome="[nome]",level=0,stress=strss,stressMax=strMax)     # Barra de stress e lv.
    
    #jump momento4
    jump supervisorScene
    
    label rSupervisorScene:
        $ variableProjectScreen = True
        jump mapScene

    return

