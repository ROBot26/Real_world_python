from turtle import Shape, Screen, Turtle, Vec2D as Vec

#User input

G = 8
NUM_LOOPS = 4100
Ro_X=0
Ro_y= -85
Vo_x=485
Vo_Y=0

class GravSys():
    """Runs a gravity simulation on n-bodies."""
    def __init__(self):
        self.bodies = []
        self.t = 0
        self.dt= 0.001
    def sim_loop(self):
        """loop bodies in a list through time steps."""
        for _ in range(NUM_LOOPS):
            self.t += self.dt
            for body in self.bodies:
                body.step()

class Body(Turtle):
    """Celestial object that orbits and projects gravity field."""
    def __init__(self, mass, start_loc, vel, gravsys, shape):
        super().__init__(shape=shape)
        self.gravsys= gravsys
        self.penup()
        self.mass = mass
        self.setpos(start_loc)
        self.vel=vel
        gravsys.bodies.append(self)
        #self.resizemode("user")
        #self.pendown()

    def acc(self):
        """Calculate combined forces on body and return vector components"""
        a= Vec(0,0)
        for body in self.gravsys.bodies:
            if body !=self:
                r=body.pos() - self.pos()
                a += (G * body.mass / abs(r)**3) *r
            return a
    def step(self):
        """"Calculate position, orientation, and velociity of a body."""
        dt=self.gravsys.dt
        a = self.acc()
        self.vel=self.vel+dt*a
        self.setpos(self.pos() + dt* self.vel)
        if self.gravsys.bodies.index(self) == 2: # index 2 = CSM
            rotate_factor =0.0006
            self.setheading((self.heading()-rotate_factor*self.xcor()))
            if self.xcor() < -20:
                self.shape('arrow')
                self.shapesize(0.5)
                self.setheading(105)
def main():
    screen = Screen()
    screen.setup(width=1, height=1) # for full screen
    screen.bgcolor('black')
    screen.title("Apollo 8 Free Return Simulation")

    gravsys= GravSys()
