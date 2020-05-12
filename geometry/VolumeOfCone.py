import math

def VolumeOfCone(Pi,Height,Radius):
    Volume = (1/3)*(Height*(Radius**2)*(Pi))
    return Volume


Pi = float(input("What are you using for PI "))
Height = float(input("What are you using for the Height "))
Radius = float(input("What are you using for the Radius "))


print(VolumeOfCone(Pi,Height,Radius))
