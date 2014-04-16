# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")

init python:
    def time_callback():#constantly calculate the time
        if (hasattr(store, 'minutes')):
            if (store.minutes > 1440):
                store.minutes = store.minutes - 1440
                store.theweekday = store.theweekday + 1
                store.theday = store.theday + 1
                store.dayofyear = dayofyear + 1
                
        if (hasattr(store, 'theweekday')):#setweekday
            if store.theweekday > 7:
                store.theweekday = store.theweekday - 7
            if store.theweekday == 1:
                store.stringweekday = "Sunday"
            elif store.theweekday == 2:
                store.stringweekday = "Monday"
            elif store.theweekday == 3:
                store.stringweekday = "Tuesday"
            elif store.theweekday == 4:
                store.stringweekday = "Wednesday"
            elif store.theweekday == 5:
                store.stringweekday = "Thursday"
            elif store.theweekday == 6:
                store.stringweekday = "Friday"
            elif store.theweekday == 7:
                store.stringweekday = "Saturday"
            else:
                store.stringweekday = "Error"
                
        if (hasattr(store, 'theday')):#monthlim
            if store.theday > store.daylim:
                store.theday = store.theday - store.daylim
                
        if (hasattr(store, 'themonth')):#setmonth
            if store.themonth == 1:
                store.stringmonth = "January"
                store.daylim = 31
            if store.themonth == 2:
                store.stringmonth = "February"
                if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                    store.daylim = 29
                else:
                    store.daylim = 28
            if store.themonth == 3:
                store.stringmonth = "March"
                store.daylim = 31
            if store.themonth == 4:
                store.stringmonth = "April"
                store.daylim = 30
            if store.themonth == 5:
                store.stringmonth = "May"
                store.daylim = 31
            if store.themonth == 6:
                store.stringmonth = "June"
                store.daylim = 30
            if store.themonth == 7:
                store.stringmonth = "July"
                store.daylim = 31
            if store.themonth == 8:
                store.stringmonth = "August"
                store.daylim = 31
            if store.themonth == 9:
               store.stringmonth = "September"
               store.daylim = 30
            if store.themonth == 10:
               store.stringmonth = "October"
               store.daylim = 31
            if store.themonth == 11:
               store.stringmonth = "November"
               store.daylim = 30
            if store.themonth == 12:
               store.stringmonth = "December"
               store.daylim = 31
            
            if (hasattr(store, 'dayofyear') and hasattr(store, 'yearlim')):#yearstuff
               if store.dayofyear > store.yearlim:
                   store.dayofyear = store.dayofyear - store.yearlim
                   store.theyear = store.theyear + 1
               if ((((int(store.theyear) / 4)*4) - store.theyear) == 0):
                   store.yearlim = 366
               else:
                   store.yearlim = 365
    config.python_callbacks.append(time_callback)
    
    def Calendar():
        ui.frame(xfill=False, xminimum = 400, yminimum=None, xalign=1.0, yalign = 0.805)
        ui.vbox()
        ui.text("(%s) - %s %d %d" % (stringweekday, stringmonth, theday, theyear), xalign=1.0, size=20)
        ui.close()
        
    def Clocks():
        ui.frame(xfill=False, xminimum = 110, yminimum=None, xalign=1.0, yalign = 0.76)
        ui.vbox()
        if (minutes > 719):
            if ((minutes - (int(minutes/60))*60) < 10):
                if((int(minutes/60)) == 12):
                    ui.text("12:0%d PM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
                else:
                    ui.text("%d:0%d PM" % ((int(minutes/60)-12), (minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
            else:
                if((int(minutes/60)) == 12):
                    ui.text("12:%d PM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
                else:
                    ui.text("%d:%d PM" % ((int(minutes/60)-12), (minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
        else:
            if ((minutes - (int(minutes/60))*60) < 10):
                if((int(minutes/60)) == 0):
                    ui.text("12:0%d AM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
                else:
                    ui.text("%d:0%d AM" % ((int(minutes/60)), (minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
            else:
                if((int(minutes/60)) == 0):
                    ui.text("12:%d AM" % ((minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
                else:
                    ui.text("%d:%d AM" % ((int(minutes/60)), (minutes - (int(minutes/60))*60)), xalign=1.0, size=20)
        ui.close()

            
# The game starts here.
label start:
    
    
    $ minutes = 750#must be initially defined.
    $ clock = True#make false to hide the calendar
    $ theweekday = 3#tuesday, the number of the weekday, this automatically changes but must be initially assigned
    $ themonth = 9#september, the number of the month, this automatically changes but must be initially assigned
    $ theday = 21#this automatically changes but must be initially assigned
    $ theyear = 2010#this automatically changes but must be initially assigned
    $ dayofyear = 264#you must calculate this properly, this automatically changes
    $ yearlim = 365#initially define it as 265 or 366, whichever is correct, this gets changed automatically later
    $ daylim = 30#initially define it as 28, 29, 30, or 31, whichever is correct, this gets changed automatically later
    $ stringweekday = "Tuesday"#3, the string of the weekday, this automatically changes but must be initially assigned
    $ stringmonth = "September"#9, the string of the month, this automatically changes but must be initially assigned
       
            
    $ minutes = minutes + 112 #or whatever
    
    $ Calendar()
    $ Clocks()

    e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    return
