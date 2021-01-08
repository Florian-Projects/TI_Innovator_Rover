#TODO Füge alle commands ab I/O hinzu.
#TODO Duplikate durch method overloading ersetzen

#Drive
def forward(distance):
    """Move the rover forwards. distance in 0.1m"""

def forward_time(time):
    """Move the rover forwards for a specific amount of time. time in seconds"""

def backward(distance):
    """Move the rover backwards. distance in 0.1m"""
def backward():
    """"""

def backward_time(time):
    """Move the rover backwards for a specific amount of time. time in seconds"""


def left(angle):
    """Turn the rover left. angle in degree"""

def left(angle, unit):
    """Turn the rover left. unit is a String specifieing the unit:
     "degrees"
     "radians"
     "grads"
     """
def right(angle, unit):
    """Turn the rover right. unit is a String specifieing the unit:
     "degrees"
     "radians"
     "grads"
     """

def right(angle):
    """Turn the rover right. angle in degree"""

def right(angle, unit):
    """Turn the rover right. unit is a String specifieing the unit:
     "degrees"
     "radians"
     "grads"
     """

def stop():
    """Stops all movement"""

def resume():
    """resumes the movement queue"""

def stay(time):
    """Stops the rover at its current position. time in seconds"""

def to_xy(x,y):
    """Move the rover to the specified cartesian-coordinates.
    to learn more about coordinates please reference coordinates in the guide book"""

def to_polar(r, theta):
    """Move the Rover to the specified polar-coordinates. r in 01.m. theta in degree"""

def to_angle(angle):
    """rotates the rover to the specified angle.
    the angle is between the x-axis and the rover in counterclockwise direction.
    90° = turn left
    angle in degree"""
