import random
import matplotlib as mp 

#declare initial varaibles for Yoda characteristics and universe
startingPopulation = 10 #arbitatry start number

infantMortality = 5 #we see very few Yodas in the SW universe, so I assume a high mortality rate since the Yodas who do survive are quite old

#Yodas seem to be omniverous species, so I modeled population growth with two sources
frogsAvailable = 40 #per Yoda

mushroomsAvailable = 20 #per Yoda

frogsHarvested = 0

mushroomsHarvested = 0

millenium = 1000

numYears = 0

currentPopulation = 0

'''Yodas don't age the same way as humans, so I approximated
a female Yoda's fertile period based of an analysis by Jon Chase in
this article from Popular Mechanics: https://www.popularmechanics.com/culture/tv/a30079354/baby-yoda/#:~:text=What%20does%20this%20mean%20for,495%20years%2C%E2%80%9D%20Chase%20says. '''
fertilityx = 90 #according to Jon Chase, youngest age that Yoda might reach maturity
fertilityy = 495 #according to Jon Chase, oldest age that Yoda might reach maturity

deathStarChance = .5 #chance of Yoda genocide

yodaDict = [] #will store each member of Yoda population as Yoda object

class Yoda:
    def __init__(self, age):
        self.gender = random.randint(0, 1)
        self.age = age 

def harvest(frogsHarvested, mushroomsHarvested, mushroomsAvailable, frogsAvailable):

    #in The Mandalorian, Grogu seems to be able to harvest frogs on his own at age 50
    ableYodas = 0 #number of Yodas able to harvest

    for yoda in yodaDict:
        if yoda.age > 50:
            ableYodas += 1
    
    #each able Yoda can harvest between 1 and foodAvailable. To simplify the simulation, all able Yodas will harvest the same amount of food in the cyclegit
    frogsHarvested += ableYodas * frogsAvailable
    mushroomsHarvested += ableYodas * mushroomsAvailable

    #Yodas can survive on either frogs or mushrooms. If there are neither enough frogs nor mushrooms, then Yodas will die.

    if frogsAvailable < len(yodaDict) and mushroomsAvailable < len(yodaDict):
            if mushroomsAvailable <= frogsAvailable:
                del yodaDict[0:int(len(yodaDict)-mushroomsAvailable)]
            else:
                del yodaDict[0:int(len(yodaDict)-frogsAvailable)]

    else:
        if frogsAvailable < len(yodaDict):
            mushroomsAvailable -= len(yodaDict)
            frogsAvailable = 0
        elif mushroomsAvailable < len(yodaDict):
            frogsAvailable -= len(yodaDict)
            mushroomsAvailable = 0
        else:
            mushroomsAvailable -= len(yodaDict)
            frogsAvailable -= len(yodaDict)


#simulate reproduction
def reproduce(fertilityx, fertilityy):
    for yoda in yodaDict:
        if yoda.gender == 1: #female
            if yoda.age > fertilityx:
                if yoda.age < fertilityy:
                    if random.randint(0,5)==1:
                        yodaDict.append(Yoda(0))

    if random.randint(0,5)==1:
     if random.randint(0,100)>infantMortality:
           yodaDict.append(Yoda(0))


#populates yodaDict with mature Yodas to start simulation
def beginSim():
    for x in range(startingPopulation):
        yodaDict.append(Yoda(random.randint(90,495)))

#simulates one year
def runYear(frogsHarvested, mushroomsHarvested, mushroomsAvailable, frogsAvailable, fertilityx, fertilityy, infantMortality, deathStarChance):
    harvest(frogsHarvested, mushroomsHarvested, mushroomsAvailable, frogsAvailable)
    reproduce(fertilityx, fertilityy)
    for yoda in yodaDict:
        if yoda.age > 950:
            yodaDict.remove(yoda)
        else:
            yoda.age +=1
    
    print(len(yodaDict))

    #chance the Death Star destroys the planet, wiping out the species
    if random.uniform(0,100) == deathStarChance:
        del yodaDict[0:len(yodaDict)]

    return len(yodaDict)


beginSim()
#runs simulation for 1000 years
for year in range(millenium):
    currentPopulation = runYear(frogsHarvested, mushroomsHarvested, mushroomsAvailable, frogsAvailable, fertilityx, fertilityy, infantMortality, deathStarChance)

print("In one millenium, the Yoda population grew to " + str(currentPopulation))
    




    





