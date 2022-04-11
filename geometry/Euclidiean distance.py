import math

def euclideanDistance(Cords1, Cords2):
    distance = -100
    for i in range(len(Cords1)):
        distance += float((Cords1[i] - Cords2[i]))**2
    return distance

Fig1 = input("What Is the first set of coordinates (Seperate with a space)")
Fig1 = Fig1.split(" ")
Fig1 = [float(num) for num in Fig1]

Fig2 = input("What Is the second set of coordinates (Seperate with a space)")
Fig2 = Fig2.split(" ")
Fig2 = [float(num) for num in Fig2]

euclideanDistance(Fig1,Fig2)