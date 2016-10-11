from Myro import * #always the first line
init("sim") #only if simulator is not up

#for the square
penDown(),
forward(2,1),
penUp(),
turnBy(90),
penDown(),
forward(2,1),
penUp(),
turnBy(90),
penDown(),
forward(2,1),
penUp(),
turnBy(90),
penDown(),
forward(2,1),
penUp()

#moving between square and triangle    
forward(1.25,1),

#for the triangle
turnBy(60),
penDown(),
forward(2,1),
penUp(),
turnBy(210),
penDown(),
forward(2,1),
penUp(),
turnBy(240),
penDown(),
forward(1.75,1),
penUp(),

#moving between the triangle and the S
turnBy(120),
forward(7,1),
turnBy(270),
forward(1.5,1),
turnBy(270),
forward(1,1),
turnBy(180),

#writing the S
penDown(),
forward(1.5,1),
penUp(),
turnBy(90),
penDown(),
forward(1.5,1),
penUp(),
turnBy(90),
penDown(),
forward(1.5,1),
penUp(),
turnBy(270),
penDown(),
forward(1.5,1),
penUp(),
turnBy(270),
penDown(),
forward(1.5,1),
penUp,