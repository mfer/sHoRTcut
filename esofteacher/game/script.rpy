# novo tipo de transicao
define fastDissolve = Dissolve (.2)

image bg ync = "ync.png"
image bg lecturehall = "lecturehall.png"
image corredor = "corredor.png"

image sylvie normal = "sylvie2_normal.png"
image sylvie giggle = "sylvie2_giggle.png"
image sylvie smile = "sylvie2_smile.png"
image sylvie surprised = "sylvie2_surprised.png"   

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('ESOFteacher', color="#c8ffc8")
define S = Character('Supervisor', color="#c8ffc8")
define P = Character('Player', color="#c8ffc8")

# The game starts here.
label start:    
    
    stop music fadeout 1.0
    
    jump scene1
    

    return

