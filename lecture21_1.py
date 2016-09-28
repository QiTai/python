from pylab import *
import random, math

def writeSpringData(fname):
    springData = open(fname, 'w')
    springData.write('#distances:forces\n')
    for distances in range(-10,100):
        forces = distances * 3 + random.randint(-3,1)
        springData.write(str(distances)+':'+str(forces)+'\n')
        

def getSpringData(fname):
    springData = open(fname, 'r')
    distances = []
    forces = []
    for line in springData:
        if line[0] == '#': continue
        line = line[:-1]
        elems = line.rsplit(':')
        distances.append(float(elems[0]))
        forces.append(float(elems[1]))
    return array(distances), array(forces)

writeSpringData('springData.txt')
distances, forces = getSpringData('springData.txt')
scatter(distances,forces)
xlabel('Distance (Meters)')
ylabel('|Forces| (Newtons)')
title('Force vs. Distance for Spring')

##figure()

k,b = polyfit(distances, forces, 1)
yVals = k*distances + b
plot(distances, yVals, c = 'r', linewidth = 2)
title('Force vs. Distance, k = ' + str(k))

show()


##a, b, c = polyfit(times, speeds, 2)
##yVals = a*(times**2) + b*times + c
##plot(times, yVals, c = 'y' , linewidth = 4)



##def rSquare(measured, estimated):
##    diffs = (estimated - measured) ** 2
##    mMeans = measured.sum() / float(len(measured))
##    var = (mMean - measured) ** 2
##    return 1 - diffs.sum() / var.sum()
##
