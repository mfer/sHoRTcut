# novo tipo de transicao
define fastDissolve = Dissolve (.2)

image bg ync = "ync.png"
image office = "office.png"
image corredor = "corredor.png"

image sylvie normal = "sylvie2_normal.png"
image sylvie giggle = "sylvie2_giggle.png"
image sylvie smile = "sylvie2_smile.png"
image sylvie surprised = "sylvie2_surprised.png" 

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
define P = Character('Player', color="#c8ffc8")

# The game starts here.
label start:    
    
    stop music fadeout 1.0
    
    jump supervisorScene
    

    return

