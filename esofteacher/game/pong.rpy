init:

    image bg pong field = "pong_field.png"

    python:

        class PongDisplayable(renpy.Displayable):

            def __init__(self):

                renpy.Displayable.__init__(self)

                # number o "bounces"
                self.count = 0
                self.aux = 0
                # Some displayables we use.
                self.paddle = Image("pong.png")
                self.ball = Image("pong_ball.png")
                self.player = Text(_("[nome]"), size=36)
                self.showCount = Text(_(str(self.count)), size=36)
                self.test = Text(_("Teste"), size=36)
                self.ctb = Text(_("Clique para Começar"), size=36)

                # The sizes of some of the images.
                self.PADDLE_WIDTH = 10
                self.PADDLE_HEIGHT = 79
                self.BALL_WIDTH = 15
                self.BALL_HEIGHT = 15
                self.COURT_TOP = 125
                self.COURT_BOTTOM = 610

                # If the ball is stuck to the paddle.
                self.stuck = True

                # The positions of the two paddles.
                self.playery = (self.COURT_BOTTOM - self.COURT_TOP) / 2
                self.computery = self.playery

                # The speed of the computer.
                self.computerspeed = 350.0

                # The position, dental-position, and the speed of the
                # ball.
                self.bx = 120
                self.by = self.playery
                self.bdx = .5
                self.bdy = .5
                self.bspeed = 300.0

                # The time of the past render-frame.
                self.oldst = None

                # The winner.
                self.winner = None

            def visit(self):
                return [ self.paddle, self.ball, self.player, self.test, self.ctb ]

            # Recomputes the position of the ball, handles bounces, and
            # draws the screen.
            def render(self, width, height, st, at):

                # The Render object we'll be drawing into.
                r = renpy.Render(width, height)

                # Figure out the time elapsed since the previous frame.
                if self.oldst is None:
                    self.oldst = st

                dtime = st - self.oldst
                self.oldst = st

                # Figure out where we want to move the ball to.
                speed = dtime * self.bspeed
                oldbx = self.bx

                if self.stuck:
                    self.by = self.playery
                else:
                    self.bx += self.bdx * speed
                    self.by += self.bdy * speed

                # Move the computer's paddle. It wants to go to self.by, but
                # may be limited by it's speed limit.
                cspeed = self.computerspeed * dtime
                if abs(self.by - self.computery) <= cspeed:
                    self.computery = self.by
                else:
                    self.computery += cspeed * (self.by - self.computery) / abs(self.by - self.computery)

                # Handle bounces.

                # Bounce off of top.
                ball_top = self.COURT_TOP - 33  + self.BALL_HEIGHT / 2
                if self.by < ball_top:
                    self.by = ball_top + (ball_top - self.by)
                    self.bdy = -self.bdy
                    renpy.sound.play("pong_beep.wav", channel=0)

                # Bounce off bottom.
                ball_bot = self.COURT_BOTTOM + 20 - self.BALL_HEIGHT / 2
                if self.by > ball_bot:
                    self.by = ball_bot - (self.by - ball_bot)
                    self.bdy = -self.bdy
                    renpy.sound.play("pong_beep.wav", channel=0)

                # This draws a paddle, and checks for bounces.
                def paddle(px, py, hotside):

                    # Render the paddle image. We give it an 800x600 area
                    # to render into, knowing that images will render smaller.
                    # (This isn't the case with all displayables. Solid, Frame,
                    # and Fixed will expand to fill the space allotted.)
                    # We also pass in st and at.
                    pi = renpy.render(self.paddle, 800, 600, st, at)

                    # renpy.render returns a Render object, which we can
                    # blit to the Render we're making.
                    r.blit(pi, (int(px), int(py - self.PADDLE_HEIGHT / 2)))

                    if py - self.PADDLE_HEIGHT / 2 <= self.by <= py + self.PADDLE_HEIGHT / 2:

                        hit = False

                        if oldbx >= hotside >= self.bx:
                            self.bx = hotside + (hotside - self.bx)
                            self.bdx = -self.bdx
                            hit = True

                        elif oldbx <= hotside <= self.bx:
                            self.bx = hotside - (self.bx - hotside)
                            self.bdx = -self.bdx
                            hit = True

                        if hit:
                            self.aux += 1
                            if(self.aux %2 == 0):
                                self.count += 1
                            #print(self.aux)
                            renpy.sound.play("pong_boop.wav", channel=1)
                            self.bspeed *= 1.10

                # Draw the two paddles.
                paddle(100, self.playery, 100 + self.PADDLE_WIDTH)
                paddle(1164, self.computery, 1164)

                # Draw the ball.
                ball = renpy.render(self.ball, 800, 600, st, at)
                r.blit(ball, (int(self.bx - self.BALL_WIDTH / 2),
                              int(self.by - self.BALL_HEIGHT / 2)))

                # Show Score
                self.showCount = Text(_(str(self.count)), size=36)
                count = renpy.render(self.showCount, 800, 600, st, at)
                cow, coh = count.get_size()
                r.blit(count, (650 - cow, 25))

                # Show Eileen's name.
                eileen = renpy.render(self.test, 800, 600, st, at)
                ew, eh = eileen.get_size()
                r.blit(eileen, (1090 - ew, 25))

                # Show the "Click to Begin" label.
                if self.stuck:
                    ctb = renpy.render(self.ctb, 800, 600, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (250 - cw / 2, 30))
                else:
                    self.ctb = Text(_("Desenvolvimento"), size=36)
                    ctb = renpy.render(self.ctb, 800, 600, st, at)
                    cw, ch = ctb.get_size()
                    r.blit(ctb, (250 - cw / 2, 30))

                # Check for a winner.
                if self.bx < 55:
                    self.winner = "eileen"
                    # Needed to ensure that event is called, noticing
                    # the winner.
                    renpy.timeout(0)

                elif self.count >= 3 or self.bx > 1200:
                    self.winner = "player"
                    renpy.timeout(0)

                # Ask that we be re-rendered ASAP, so we can show the next
                # frame.
                renpy.redraw(self, 0)

                # Return the Render object.
                return r

            # Handles events.
            def event(self, ev, x, y, st):

                import pygame

                # Mousebutton down == start the game by setting stuck to
                # false.
                if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                    self.stuck = False

                # Set the position of the player's paddle.
                y = max(y, self.COURT_TOP)
                y = min(y, self.COURT_BOTTOM)
                if not renpy.variant('touch') or pygame.mouse.get_pressed()[0]:
                    self.playery = y
                # If we have a winner, return him or her. Otherwise, ignore
                # the current event.
                if self.winner:
                    return self.winner
                else:
                    raise renpy.IgnoreEvent()


label pong:

    window hide None

    $ renpy.music.stop(channel="music",fadeout=1.0) 

    $ renpy.music.play("WaveAfterWave!v0_9.mp3", channel="music", loop=True, fadein=1.0)
   
    hide screen stressBar
    hide screen clock

    # Put up the pong background, in the usual fashion.
    scene bg pong field

    # Run the pong minigame, and determine the winner.
    python:
        ui.add(PongDisplayable())
        winner = ui.interact(suppress_overlay=True, suppress_underlay=True)

    #scene 

    window show None

    if winner == "eileen":
        show donoDoProd0 at right
        with fastDissolve
        "{cps=40}A equipe de Testes encontrou algumas {b}{i}falhas{/i}{/b} no módulo implementado!{/cps}"
        hide donoDoProd0

    else:
        show donoDoProd6 at right
        with fastDissolve
        "{cps=40}Parabéns, o {i}{b}módulo{/b}{/i} desenvolvido passou em todos os testes de regressão!{/cps}"
        hide donoDoProd6

    jump mapScene1
   
    return
