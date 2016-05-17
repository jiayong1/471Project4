import sys
import math
import random
import matplotlib.pyplot as plt

def main():
    numberofk = int(sys.argv[1])
    filename = sys.argv[2]
    #numberofk = int(input("numer of clusters"))
    #lfilename = input("the file path of 2d points")
    inputfile = open(filename, "r")
    allpoints = []
    for line in inputfile:
        allpoints.append(line.strip().split(' '))
    dis = calDistance(allpoints[4], allpoints[6])
    clusterid = random.sample(range(0,len(allpoints)), numberofk)
    #clusterid= [3, 6, 7]
    #print(clusterid)
    allclusters = {}
 
    for i in clusterid:

        allclusters[i] = []
    clusters = {}
    #print(clusterid)
    for j in clusterid:
        clusters[j] = allpoints[j]
    allpoints = [i for j, i in enumerate(allpoints) if j not in clusterid] 
    for everypoint in allpoints:
        closestCluster = clusterid[0]
        smalldistance = calDistance(everypoint, clusters[clusterid[0]])
        for k in clusters:
            distance = calDistance(everypoint, clusters[k])
            if distance < smalldistance:
                smalldistance = distance
                closestCluster = k
        allclusters[closestCluster].append(everypoint)            
    #print(allclusters)
    newclustersPosition = {}
    for eachid in clusterid:
        if len(allclusters[eachid]) > 0:
            newclustersPosition[eachid] = findnewposition(allclusters[eachid])
        else:
            newclustersPosition[eachid] = clusters[eachid]
    #print(newclustersPosition)
    color1 = ['bo','go','yo','co','mo','ro','ko','wo']
    color2 = ['bx','gx','yx','cx','mx','rx','kx','wx']
    z = 0
    #print(newclustersPosition)
    for eachid in clusterid:
       
        for eachpoint in allclusters[eachid]:
            plt.plot(eachpoint[0],eachpoint[1], color1[z] )
        plt.plot(newclustersPosition[eachid][0],newclustersPosition[eachid][1], color2[z] )
        z += 1
    plt.show()
    
    
    
def calDistance(pointA, pointB):
    distance = math.sqrt((float(pointA[0]) - float(pointB[0]))**2+(float(pointA[1])-float(pointB[1]))**2)
    return distance

def findnewposition(listofpoints):
    newX = 0
    newY = 0 
    for eachpoint in listofpoints:
        newX += float(eachpoint[0])
        newY += float(eachpoint[1])
    return [newX/len(listofpoints), newY/len(listofpoints)]
    
    
    
main()
