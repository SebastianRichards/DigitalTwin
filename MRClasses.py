#this file is where all classes are stored, you can see the classes in a more summarised version in the UML class diagram file

class MicroReactor:
    def __init__(self, electrode1, electrode2, electrodeDimensions, listOfTubes):
        self.electrode1 = electrode1
        self.electrode2 = electrode2
        self.electrodeDimensions = electrodeDimensions
        self.listOfTubes = listOfTubes



class ElectrodeDimensions:
    #constructor
    def __init__(self, electrodeArea, electrodeDistance):
        self.electrodeArea = electrodeArea #in mM^2
        self.electrodeDistance = electrodeDistance #in mM


class ElectrodeType:
    #constructors
    def __init__(self, element, standardElectrodePotential):
        self.element = element
        self. standardElectrodePotential = standardElectrodePotential


#instantiating different Electrodetype classes to be used in the Electrode

Gold = ElectrodeType("Gold", 1.83)
Nickel = ElectrodeType("Nickel", -0.257)
Platinum = ElectrodeType("Platinum", 1.2)
Lithium = ElectrodeType("Lithium", -3.04)
Calcium = ElectrodeType("Calcium", -2.87)
Sodium = ElectrodeType("Sodium", -2.71)
Zinc = ElectrodeType("Zinc", -0.762)
Iron2 = ElectrodeType("Iron2", -0.441)
Hydrogen = ElectrodeType("Hydrogen", 0)
Magnesium = ElectrodeType("Magnesium", -2.36)
Iron3 = ElectrodeType("Iron3", 0.77)
Fluorine = ElectrodeType("Fluorine", 2.87)

#list of ElectrodeType classes
electrodeTypeList = [Gold, Platinum, Nickel, Lithium, Calcium, Sodium, Zinc, Iron2, Hydrogen, Magnesium, Iron3, Fluorine]




class ReactionConditions:
    def __init__(self, temperature, flowRate, pressure):
        self.temperature = temperature #Kelvin
        self.flowRate = flowRate #m3/s
        self.pressure = pressure
    #setters
    def setTemperature(self, temperature):
        self.temperature = temperature
    def setFlowRate(self, flowRate):
        self.flowRate = flowRate
    def setPressure(self, pressure):
        self.pressure = pressure


class Chemical:
    def __init__(self, chemicalName, chemicalFormula, atomicNumber, molecularNumber, isRadical, charge):
        self.chemicalName = chemicalName
        self.chemicalFormula = chemicalFormula
        self.atomicNumber = atomicNumber
        self.molecularNumber = molecularNumber
        self.isRadical = isRadical
        self.charge = charge
    def increaseCharge(self):
        self.charge += 1
        print("increasing charge...")

#instantiating library of Chemicals:
Benzene = Chemical("Benzene", "c6h6", 42, 88, False, 0)
BenzylIodide = Chemical("BenzylIodide", "c7h7i", 102, 218, False, 0)
Thioanisole = Chemical("Thioanisole", "c7h8s", 66, 124, False, 0)



reagentList = [Benzene, BenzylIodide, Thioanisole]

class Reaction:
    def __init__(self, chemical1, chemical2, reactionConditions, microReactor):
        self.chemical1 = chemical1
        self.chemical2 = chemical2
        self.reactionConditions = reactionConditions
        self.microReactor = microReactor

class Tube:
    #length in M, diameter in mM
    def __init__(self, length, diameter, numberOfLoops, material):
        self.id = id
        self.length = length
        self.diameter = diameter
        self.numberOfLoops = numberOfLoops
        self.material = material
