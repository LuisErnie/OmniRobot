from GroveUltrasonicRanger import GroveUltrasonicRanger 

sonarL = GroveUltrasonicRanger(24)
sonarR = GroveUltrasonicRanger(26)

def sensorsRead():
    distL = sonarL.get_distance()
    distR = sonarR.get_distance()

    return distL, distR