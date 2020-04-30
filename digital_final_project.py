

#This Program is designed to model the activity of the Door Sensor
#This code uses two sensors that are triggered when someone enters or exits a doorway
#These sensors relay a 1 or 0 that the counter tracks
#Based on this count, the circuit will change the voltage of 3 LED's
#According to maximum capacity of the room, the LED's will light according to percentage
#0-25%-Green, 26-75%-Orange, 76% or more- Red
#The user acts as the sensor to determine the count
import time
#Sensor Class definition
class Sensor:

    def __init__(self, is_triggered):
        self.is_triggered = is_triggered

    def read_sensor(self):
        return str(self.is_triggered)
#Initialize Sensors
sensor_A = Sensor(False)
sensor_B = Sensor(False)
# Define LED's
class LED:
    def __init__(self):
        self.is_lit = False

    def display(self):
        return str(self.is_lit)
    def light_on(self):
        self.is_lit = True

    def light_off(self):
            self.is_lit = False

# Initialize LED's
red_LED = LED()
orange_LED = LED()
green_LED = LED()


# Create a class for detecting changes to occupancy
class Detect:

    def __init__(self,max_occupancy, occupancy):
        self.max_occupancy = max_occupancy
        self.occupancy = occupancy
    def __repr__(self):
        print("Red LED Lit :" + red_LED.display())
        print("Orange LED Lit :" + orange_LED.display())
        print("Green LED Lit :" + green_LED.display())
# Function to change occupancy when someone enters
    def person_entering(self):
        self.occupancy += 1
        sensor_A.is_triggered = True
        self.update_occupancy()
        sensor_A.is_triggered = False
        print("Red LED Lit :" + red_LED.display())
        print("Orange LED Lit :" + orange_LED.display())
        print("Green LED Lit :" + green_LED.display())

# Function to change occupancy when someone exits
    def person_exiting(self):
        self.occupancy -= 1
        sensor_B.is_triggered = True
        self.update_occupancy()
        sensor_B.is_triggered = False
        print("Red LED Lit :" + red_LED.display())
        print("Orange LED Lit :" + orange_LED.display())
        print("Green LED Lit :" + green_LED.display())
# Define a function for changing LED's value based on occupancy
    def update_occupancy(self):

        def check_LED():
            if self.occupancy < self.max_occupancy*.25:
                green_LED.light_on()
                orange_LED.light_off()
                red_LED.light_off()
            elif self.occupancy <= self.max_occupancy*.75:
                green_LED.light_off()
                orange_LED.light_on()
                red_LED.light_off()
            elif self.occupancy >= self.max_occupancy*.75:
                green_LED.light_off()
                orange_LED.light_off()
                red_LED.light_on()

        if sensor_A.is_triggered:
            print("occupancy = " + str(self.occupancy))
            check_LED()
        elif sensor_B.is_triggered:
            print("occupancy = " + str(self.occupancy))
            check_LED()

# Define main loop for Sensor(user) to track entrance and exit
def main():
    entry = int(input("Enter 1 for entering or 0 for exiting or anything else to end: "))
    try:
        if entry == 1:
            detect.person_entering()
            main()
        elif entry == 0:
            detect.person_exiting()
            main()
        else:
            detect.__repr__()
            print("Complete")
    except:
        detect.__repr__()
        print("Complete")
        time.sleep(5)
#Begin main code with user entries
max = int(input("Enter Maximum number of Occupants: "))
current = int(input("Enter Current number of Occupants: "))
detect = Detect(max, current)
main()



