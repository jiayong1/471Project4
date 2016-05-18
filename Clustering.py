import sys
import math
import random
import matplotlib.pyplot as plt

def main():
    #get the data in file and save in the list
    numberofk = int(sys.argv[1])
    filename = sys.argv[2]
    inputfile = open(filename, "r")
    allpoints = []
    for line in inputfile:
        allpoints.append(line.strip().split(' '))
    #random get the k clusters
    clusterid = random.sample(range(0,len(allpoints)), numberofk)
    newclustersPosition = {}
   
    thebiggest = [1,2]
    allclusters = {}
    clusters = {}
    for i in clusterid:
        allclusters[i] = []
    
   
    
    
    for j in clusterid:
        clusters[j] = allpoints[j]
    allpoints = [i for j, i in enumerate(allpoints) if j not in clusterid] 
    
    #setup an maximum iterations, if the iterations more than the number. Break.
    count = 0
    maxiterations = 30
    #loop until all the nodes in a cluster doesnot change.
    while thebiggest[-1] != thebiggest[-2]:
        count+=1
        if count >= maxiterations:
              break    
        for everypoint in allpoints:
            closestCluster = clusterid[0]
            smalldistance = calDistance(everypoint, clusters[clusterid[0]])
            for k in clusters:
                distance = calDistance(everypoint, clusters[k])
                if distance < smalldistance:
                    smalldistance = distance
                    closestCluster = k
            allclusters[closestCluster].append(everypoint)            
        
        for eachid in clusterid:
            if len(allclusters[eachid]) > 0:
                newPos = findnewposition(allclusters[eachid])
                newclustersPosition[eachid] = newPos
                clusters[eachid] = newPos
            else:
                newclustersPosition[eachid] = clusters[eachid]
        
        thebiggest.append(allclusters.copy())
        for i in clusterid:
            allclusters[i] = []
    
    
    
    
    allclusters = thebiggest[-1]
    
    
    

    
    color1 = ['bo','go','yo','co','mo','ro','ko','wo']
    color2 = ['bx','gx','yx','cx','mx','rx','kx','wx']
    z = 0
    #draw the graph with different color.
    for eachid in clusterid:
       
        for eachpoint in allclusters[eachid]:
            plt.plot(eachpoint[0],eachpoint[1], color1[z] )
        plt.plot(newclustersPosition[eachid][0],newclustersPosition[eachid][1], color2[z] )
        z += 1
    plt.show()
    
    
#the function to calculate the distance between two points.
def calDistance(pointA, pointB):
    distance = math.sqrt((float(pointA[0]) - float(pointB[0]))**2+(float(pointA[1])-float(pointB[1]))**2)
    return distance
#the function to find the center of a cluster.
def findnewposition(listofpoints):
    newX = 0
    newY = 0 
    for eachpoint in listofpoints:
        newX += float(eachpoint[0])
        newY += float(eachpoint[1])
    return [newX/len(listofpoints), newY/len(listofpoints)]
    
    
    
main()
