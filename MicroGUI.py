#this file is for the design and functionality of the GUI for the microReactor

#imports
from tkinter import *
from MRClasses import *
import sys

#initialising tkinter loop for GUI
root = Tk()
root.title("MicroReactor GUI")

counter = -1
tubeNumber = "Tube"



#Frame
currentConditions = Frame(root)
changeParameter = Frame(root)
inputFieldFrame = Frame(root)
runButtonFrame = Frame(root)
electrodeDimensionsFrame = Frame(root)
tubingFrame = Frame(root)
inputFieldFrame2 = Frame(root)
tubeObjectsFrame = Frame(root)
timeStampFrame = Frame(root)
confirmedStampsFrame = Frame(root)



#input import
e1 = Entry(inputFieldFrame, width=15)
e2 = Entry(inputFieldFrame, width=15)
e3 = Entry(inputFieldFrame, width=15)

reagent1 = Benzene
reagent2 = Benzene

#instatiation of default reaction conditions
defaultReactionConditions = ReactionConditions(30, 2.5, 10)


#instantiation of electrode distance and area
defaultElectrodeDimensions = ElectrodeDimensions(5, 70)


#Label showing conditions
labelReactionConditions = Label(currentConditions, text="Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))

#label showing reagent
labelReagent1 = Label(currentConditions, text="Reagent 1: " + reagent1.chemicalName)
labelReagent2 = Label(currentConditions, text="Reagent 2: " + reagent2.chemicalName)

#instantiation of default Electrodes
electrodeA = Platinum
electrodeB = Platinum

#label showing Electrodes in Use
electrodeLabel1 = Label(currentConditions, text="Electrode 1: " + electrodeA.element)
electrodeLabel2 = Label(currentConditions, text="Electrode 2: " + electrodeB.element)

#Label showing electrode area
electrodeDimensionsLabel = Label(currentConditions, text="Electrode Area(mM^2): " + str(defaultElectrodeDimensions.electrodeArea) + "\nElectrode Distance(mM): " + str(defaultElectrodeDimensions.electrodeDistance))


#Labels which go next to the input boxes when creating a new tube object
addTubeLengthLabel = Label(inputFieldFrame2, text="Add Tube Length(M)")
addDiameterLabel = Label(inputFieldFrame2, text="Add Tube Diameter(mM)")
numberOfLoopsLabel =Label(inputFieldFrame2, text="Add No. of Loops")
addMaterialLabel = Label(inputFieldFrame2, text="Add Material")

#gets rid of .0 from float numbers
def formatNumber(num):
  if num % 1 == 0:
    return int(num)
  else:
    return num


#functions
def editButtonF():
    runButtonFrame.grid_forget()
    #button changes
    editButton.grid_forget()
    backButton.grid(row=1, column=0)
    editElectrodeButton1.grid(row=0, column=0)
    editElectrodeButton2.grid(row=1, column=0)
    editReactionConditionsButton.grid(row=2, column=0)
    editReagentButton1.grid(row=3, column=0)
    editReagentButton2.grid(row=4, column=0)
    editElectrodeDimensionsButton.grid(row=5, column=0)
    setVariableButton.grid(row=6, column=0)
    changeParameter.grid(row=1, column=2)

def backButtonF():
    runButtonFrame.grid(row=0, column=0)
    #button changes
    backButton.grid_forget()
    editButton.grid(row=1, column=0)
    editElectrodeButton1.grid_forget()
    editElectrodeButton2.grid_forget()
    changeParameter.grid_forget()
    electrodeFrame.grid_forget()
    electrodeFrame2.grid_forget()
    submitChangesElectrode1Button.grid_forget()
    submitChangesElectrode2Button.grid_forget()
    inputFieldFrame.grid_forget()
    electrodeDimensionsFrame.grid_forget()
    reagentFrame.grid_forget()
    reagentFrame2.grid_forget()
    submitChangesReagent1Button.grid_forget()
    submitChangesReagent2Button.grid_forget()



def editElectrodeButtonF1():
    electrodeFrame.grid(row=1, column=3)
    submitChangesElectrode1Button.grid(row=2, column=3)


def editElectrodeButtonF2():
    electrodeFrame2.grid(row=3, column=3)
    submitChangesElectrode2Button.grid(row=4, column=3)

def editReagentF1():
    reagentFrame.grid(row=1, column=4)
    submitChangesReagent1Button.grid(row=2, column=4)

def editReagentF2():
    reagentFrame2.grid(row=3, column=4)
    submitChangesReagent2Button.grid(row=4, column=4)

def submitChangesReagent1F():
    reagent1 = str_to_class(reagentListBox.get(ANCHOR))
    changeText(labelReagent1, "Reagent 1: " + str(reagent1.chemicalName))

def submitChangesReagent2F():
    reagent2 = str_to_class(reagentListBox2.get(ANCHOR))
    changeText(labelReagent2, "Reagent 2: " + str(reagent2.chemicalName))

def editReactionConditionsF(temperature, flowRate):
    temperature = defaultReactionConditions.temperature
    flowRate = defaultReactionConditions.flowRate


entryArea = Entry(electrodeDimensionsFrame, width=15)
entryDistance = Entry(electrodeDimensionsFrame, width=15)
def openElectrodeDimensionsF():
    entryArea.grid(column=0, row=0)
    submitChangesElectrodeAreaButton.grid(row=1, column=0)
    entryDistance.grid(row=0, column=1)
    submitChangesElectrodeDistanceButton.grid(row=1, column=1)
    electrodeDimensionsFrame.grid(row=6, column=1)

def submitChangesElectrodeAreaF():
    defaultElectrodeDimensions.electrodeArea = formatNumber(float(entryArea.get()))
    changeText(electrodeDimensionsLabel, "Electrode Area(mM^2): " + str(defaultElectrodeDimensions.electrodeArea) + "\nElectrode Distance(mM): " + str(defaultElectrodeDimensions.electrodeDistance))

def submitChangesElectrodeDistanceF():
    defaultElectrodeDimensions.electrodeDistance = formatNumber(float(entryDistance.get()))
    changeText(electrodeDimensionsLabel, "Electrode Area(mM^2): " + str(defaultElectrodeDimensions.electrodeArea) + "\nElectrode Distance(mM): " + str(defaultElectrodeDimensions.electrodeDistance))


def showInputField():
    e1.grid(column=0, row=0)
    submitChangesButtonTemp.grid(column=0, row=1)
    e2.grid(column=0, row=2)
    submitChangesButtonFlowRate.grid(column=0, row=3)
    e3.grid(column=0, row=4)
    submitChangesButtonPressure.grid(column=0, row=5)
    inputFieldFrame.grid(row=5, column=0)


def submitChangesTempF():
    defaultReactionConditions.temperature = formatNumber(float(e1.get()))
    changeText(labelReactionConditions, "Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))


def submitChangesFlowRateF():
    defaultReactionConditions.flowRate = formatNumber(float(e2.get()))
    changeText(labelReactionConditions, "Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))

def submitChangesPressureF():
    defaultReactionConditions.pressure = formatNumber(float(e3.get()))
    changeText(labelReactionConditions, "Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))

def submitChangesElectrode1F():
    electrodeA = str_to_class(electrodeListBox.get(ANCHOR))
    changeText(electrodeLabel1, "Electrode 1: " + str(electrodeA.element))

def submitChangesElectrode2F():
    electrodeB = str_to_class(electrodeListBox2.get(ANCHOR))
    changeText(electrodeLabel2, "Electrode 2: " + str(electrodeB.element))


#converts string to class object (needed for the listbox selection in submitChangesElectrode1F and "" ""2f functions)
def str_to_class(str):
    return getattr(sys.modules[__name__], str)

#a setter to change/update the text attribute in the electrodeLabel1 and 2 Labels(objects)
def changeText(self, newText):
    self.configure(text=newText)

#setting the counter when pressing the run button
def runF():
    runButton.grid_forget()
    stopButton.grid(column=0, row=0)
    global counterLabel
    counterLabel = Label(root, text="Time Elapsed(s): " + str(counter))
    counterLabel.grid(row=6, column=1)
    def count():
        global counter
        counter += 1
        counterLabel.config(text="Time Elapsed(s): " + str(counter))
        for key in tempDict:
            if key == counter:
                defaultReactionConditions.temperature = tempDict[key]
                changeText(labelReactionConditions, "Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))
        for key in flowRateDict:
            if key == counter:
                defaultReactionConditions.flowRate = flowRateDict[key]
                changeText(labelReactionConditions, "Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))
        for key in pressureDict:
            if key == counter:
                defaultReactionConditions.pressure = pressureDict[key]
                changeText(labelReactionConditions, "Temperature(K): " + str(defaultReactionConditions.temperature) + "\nFlow rate(m3/s): " + str(defaultReactionConditions.flowRate) + "\nPressure(Pa): " + str(defaultReactionConditions.pressure))
        counterLabel.after(1000, count)
        return counter
    count()





#dictionaires for timestamps
tempDict = {}
pressureDict = {}
flowRateDict = {}
pressureDict = {}
labelSting = "label"
labelCount = 0
labelDict1 = {}
labelList = []

def variableTempF():
    tempStamp = formatNumber(float(timeStampEntryTemp.get()))
    timeStamp = int(timeStampEntryTempTime.get())
    tempDict[timeStamp] = tempStamp
    global labelCount
    labelCount += 1
    labelDict1[labelCount] = labelSting + str(labelCount)
    labelDict[labelCount] = Label(confirmedStampsFrame, text="Time Stamp " + str(labelCount) + ": " + "At time: " + str(timeStamp) + "(s) Temperature = " + str(tempStamp) + "K")
    labelDict[labelCount].grid(row=labelCount, column=0)
    labelList.append(labelDict[labelCount])


def variablePressureF():
    pressureStamp = formatNumber(float(timeStampEntryPressure.get()))
    timeStamp = int(timeStampEntryTempTime.get())
    pressureDict[timeStamp] = pressureStamp
    global labelCount
    labelCount += 1
    labelDict1[labelCount] = labelSting + str(labelCount)
    labelDict[labelCount] = Label(confirmedStampsFrame, text="Time Stamp " + str(labelCount) + ": " + "At time: " + str(timeStamp) + "(s) Pressure = " + str(pressureStamp) + "Pa")
    labelDict[labelCount].grid(row=labelCount, column=0)
    labelList.append(labelDict[labelCount])


def variableFlowRateF():
    flowRateStamp = formatNumber(float(timeStampEntryFlow.get()))
    timeStamp = int(timeStampEntryTempTime.get())
    flowRateDict[timeStamp] = flowRateStamp
    global labelCount
    labelCount += 1
    labelDict1[labelCount] = labelSting + str(labelCount)
    labelDict[labelCount] = Label(confirmedStampsFrame, text="Time Stamp " + str(labelCount) + ": " + "At time: " + str(timeStamp) + "(s) FlowRate = " + str(flowRateStamp) + "m3/s")
    labelDict[labelCount].grid(row=labelCount, column=0)
    labelList.append(labelDict[labelCount])





def stopFunction():
    counterLabel.grid_forget()
    counterLabel.destroy()
    global counter
    counter = -1
    stopButton.grid_forget()
    runButton.grid(column=0, row=0)

def setVariableFunction():
    editElectrodeButton1.grid_forget()
    editElectrodeButton2.grid_forget()
    changeParameter.grid_forget()
    electrodeFrame.grid_forget()
    electrodeFrame2.grid_forget()
    submitChangesElectrode1Button.grid_forget()
    submitChangesElectrode2Button.grid_forget()
    inputFieldFrame.grid_forget()
    electrodeDimensionsFrame.grid_forget()
    backButton.grid_forget()
    #forgetting home screen stuff
    currentConditions.grid_forget()
    tubeObjectsFrame.grid_forget()
    reagentFrame.grid_forget()
    reagentFrame2.grid_forget()
    submitChangesReagent1Button.grid_forget()
    submitChangesReagent2Button.grid_forget()
    backButton2.grid(row=1, column=0)
    timeStampButton.grid(row=2, column=0)
    confirmedStampsFrame.grid(row=3, column=2)
timeStampLabelTemp = Label(timeStampFrame, text="Enter Temperature(K)")
timeStampLabelTempTime = Label(timeStampFrame, text="Enter Time(s)")
timeStampLabelFlow = Label(timeStampFrame, text="Enter FlowRate(m3/s)")
timeStampLabelFlowTime = Label(timeStampFrame, text="Enter Time(s)")
timeStampLabelPressure = Label(timeStampFrame, text="Enter Pressure(Pa)")
timeStampLabelPressureTime = Label(timeStampFrame, text="Enter Time(s)")
timeStampEntryTemp = Entry(timeStampFrame, text="enter temperature change", width=15)
timeStampEntryFlow = Entry(timeStampFrame, width=15)
timeStampEntryPressure = Entry(timeStampFrame, width=15)
timeStampEntryTempTime = Entry(timeStampFrame, text="enter time", width=15)
timeStampEntryFlowTime = Entry(timeStampFrame, width=15)
timeStampEntryPressureTime = Entry(timeStampFrame, width=15)





def timeStampF():
    timeStampLabelTemp.grid(row=0, column=0)
    timeStampEntryTemp.grid(row=0, column=1)
    timeStampLabelTempTime.grid(row=0, column=2)
    timeStampEntryTempTime.grid(row=0, column=3)
    timeStampButtonTemperature.grid(row=0, column=4)
    timeStampLabelFlow.grid(row=1, column=0)
    timeStampEntryFlow.grid(row=1, column=1)
    timeStampLabelFlowTime.grid(row=1, column=2)
    timeStampEntryFlowTime.grid(row=1, column=3)
    timeStampButtonFlowRate.grid(row=1, column=4)
    timeStampLabelPressure.grid(row=2, column=0)
    timeStampEntryPressure.grid(row=2, column=1)
    timeStampLabelPressureTime.grid(row=2, column=2)
    timeStampEntryPressureTime.grid(row=2, column=3)
    timeStampButtonPressure.grid(row=2, column=4)
    timeStampFrame.grid(row=1, column=2)
    timeStampButton.grid_forget()













def backButton2F():
    runButtonFrame.grid(row=0, column=0)
    backButton2.grid_forget()
    editButton.grid(row=1, column=0)
    currentConditions.grid(row=1, column=1)
    tubeObjectsFrame.grid(row=2, column=1)
    timeStampButton.grid_forget()
    timeStampFrame.grid_forget()
    confirmedStampsFrame.grid_forget()



#instantiaing new entry widget (input field) that will be used in the addTube function
tubeLengthEntry = Entry(inputFieldFrame2, width=15)
tubeDiameterEntry = Entry(inputFieldFrame2, width=15)
numberOfLoopsEntry = Entry(inputFieldFrame2, width=15)
tubeMaterialEntry = Entry(inputFieldFrame2, width=15)

def editTubingF():
    editElectrodeButton1.grid_forget()
    editElectrodeButton2.grid_forget()
    changeParameter.grid_forget()
    electrodeFrame.grid_forget()
    electrodeFrame2.grid_forget()
    submitChangesElectrode1Button.grid_forget()
    submitChangesElectrode2Button.grid_forget()
    inputFieldFrame.grid_forget()
    electrodeDimensionsFrame.grid_forget()
    backButton.grid_forget()
    reagentFrame.grid_forget()
    reagentFrame2.grid_forget()
    submitChangesReagent1Button.grid_forget()
    submitChangesReagent2Button.grid_forget()
    #forgetting home screen stuff
    currentConditions.grid_forget()
    backButton3.grid(row=0, column=0)
    addTubeButton.grid(row=0, column=2)
    tubeObjectsFrame.grid(row=2, column=1)

def backButton3F():
    runButtonFrame.grid(row=0, column=0)
    backButton3.grid_forget()
    editButton.grid(row=1, column=0)
    currentConditions.grid(row=1, column=1)
    inputFieldFrame2.grid_forget()
    addTubeButton.grid_forget()




def addTubeF():
    addTubeButton.grid_forget()
    tubeLengthEntry.grid(row=0, column=0)
    addTubeButton.grid_forget()
    addTubeLengthLabel.grid(row=0, column=1)
    tubeDiameterEntry.grid(row=1, column=0)
    addDiameterLabel.grid(row=1, column=1)
    numberOfLoopsEntry.grid(row=2, column=0)
    numberOfLoopsLabel.grid(row=2, column=1)
    tubeMaterialEntry.grid(row=3, column=0)
    addMaterialLabel.grid(row=3, column=1)
    submitTubeButton.grid(row=4, column=0)
    inputFieldFrame2.grid(row=1, column=1)

#all of these variavles below are to be used in the submitTubeF found below
numberOfTubesList = []
tubeObjectList = []
labelObjectList = []
tubeCounter = 0
tubeDict = {}
labelDict = {}
strNo = 0


def submitTubeF():
    """the code here is designed to instantiate a new object of class Tube everytime the user presses the submit tube button
    which calls this submitTubeF function, the idea is to create a list of newly created different objects with the names tube0, tube1 etc..
    hence the defaultString of "tube" which will be altered by adding an incrementing number and then storing that new string as a key-
    - in a dictionary 'tubeDict' this is then called to create our object, after this (since we need objects of the class Label to show information to our user)
    we repeat the same process but with label objects, creating a dictionary 'labelDict' which have label0,label1,label2"""
    defaultString = "tube"
    defaultStringLabel = "label"
    global tubeCounter
    global numberOfTubesList
    global tubeDict
    global tubeObjectList
    global labelObjectList
    global labelDict
    if tubeCounter in numberOfTubesList:
        tubeCounter += 1
        numberOfTubesList.append(tubeCounter)
        tubeDict[tubeCounter] = defaultString + str(tubeCounter)
        tubeDict[tubeCounter] = Tube(formatNumber(float(tubeLengthEntry.get())), formatNumber(float(tubeDiameterEntry.get())), int(numberOfLoopsEntry.get()), tubeMaterialEntry.get())
        tubeObjectList.append(tubeDict[tubeCounter])
        labelDict[tubeCounter] = defaultStringLabel + str(tubeCounter)
        labelDict[tubeCounter] = Label(tubeObjectsFrame, text="tube length(M): " + str(tubeObjectList[tubeCounter].length) + " diameter(mM): " + str(tubeObjectList[tubeCounter].diameter) + " number of loops: " + str(tubeObjectList[tubeCounter].numberOfLoops) + " material: " + str(tubeObjectList[tubeCounter].material))
        labelDict[tubeCounter].grid(row=tubeCounter, column=0)
        labelObjectList.append(labelDict[tubeCounter])
    else:
        numberOfTubesList.append(tubeCounter)
        tubeDict[tubeCounter] = defaultString + str(tubeCounter)
        tubeDict[tubeCounter] = Tube(formatNumber(float(tubeLengthEntry.get())), formatNumber(float(tubeDiameterEntry.get())), int(numberOfLoopsEntry.get()), tubeMaterialEntry.get())
        tubeObjectList.append(tubeDict[tubeCounter])
        labelDict[tubeCounter] = defaultStringLabel + str(tubeCounter)
        labelDict[tubeCounter] = Label(tubeObjectsFrame, text="tube length(M): " + str(tubeObjectList[tubeCounter].length) + " diameter(mM): " + str(tubeObjectList[tubeCounter].diameter) + " number of loops: " + str(tubeObjectList[tubeCounter].numberOfLoops) + " material: " + str(tubeObjectList[tubeCounter].material))
        labelObjectList.append(labelDict[tubeCounter])
        labelDict[tubeCounter].grid(row=tubeCounter, column=0)
        tubeCounter += 1
    addTubeLengthLabel.grid_forget()
    tubeDiameterEntry.grid_forget()
    addDiameterLabel.grid_forget()
    numberOfLoopsEntry.grid_forget()
    numberOfLoopsLabel.grid_forget()
    tubeMaterialEntry.grid_forget()
    addMaterialLabel.grid_forget()
    submitTubeButton.grid_forget()
    inputFieldFrame2.grid_forget()
    addTubeButton.grid(row=1, column=0)
    tubeObjectsFrame.grid(row=2, column=1)




#listboxes - create frame and scrollbar 1
electrodeFrame = LabelFrame(root)
scrollbar = Scrollbar(electrodeFrame, orient=VERTICAL)
electrodeListBox = Listbox(electrodeFrame, width=50, yscrollcommand=scrollbar.set)
scrollbar.config(command=electrodeListBox.yview)
for element in electrodeTypeList:
    electrodeListBox.insert(0, element.element)
#packing listbox for electrode button
scrollbar.pack(side=RIGHT, fill=Y)
electrodeListBox.pack(side=LEFT, fill=BOTH)



#listboxes - create frame and scrollbar 2
electrodeFrame2 = LabelFrame(root)
scrollbar2 = Scrollbar(electrodeFrame2, orient=VERTICAL)
electrodeListBox2 = Listbox(electrodeFrame2, width=50, yscrollcommand=scrollbar2.set)
scrollbar2.config(command=electrodeListBox2.yview)
for element in electrodeTypeList:
    electrodeListBox2.insert(0, element.element)
scrollbar2.pack(side=RIGHT, fill=Y)
electrodeListBox2.pack(side=LEFT, fill=BOTH)




#edit Reagent frame and scrollbar

reagentFrame = LabelFrame(root)
scrollbar3 = Scrollbar(reagentFrame, orient=VERTICAL)
reagentListBox = Listbox(reagentFrame, width=50, yscrollcommand=scrollbar3.set)
scrollbar3.config(command=reagentListBox.yview)
for element in reagentList:
    reagentListBox.insert(0, element.chemicalName)
#packing listbox for electrode button
scrollbar3.pack(side=RIGHT, fill=Y)
reagentListBox.pack(side=LEFT, fill=BOTH)

#reagent frame and scrollbar number 2
reagentFrame2 = LabelFrame(root)
scrollbar4 = Scrollbar(reagentFrame2, orient=VERTICAL)
reagentListBox2 = Listbox(reagentFrame2, width=50, yscrollcommand=scrollbar4.set)
scrollbar4.config(command=reagentListBox2.yview)
for element in reagentList:
    reagentListBox2.insert(0, element.chemicalName)
#packing listbox for electrode button
scrollbar4.pack(side=RIGHT, fill=Y)
reagentListBox2.pack(side=LEFT, fill=BOTH)



#buttons
runButton = Button(runButtonFrame, text="RUN", command=runF)
editButton = Button(root, text="EDIT", command=editButtonF)
backButton = Button(root, text="BACK", command=backButtonF)
editElectrodeButton1 = Button(changeParameter, text="Edit Electrode 1", command=editElectrodeButtonF1)
editElectrodeButton2 = Button(changeParameter, text="Edit Electrode 2", command=editElectrodeButtonF2)
editReactionConditionsButton = Button(changeParameter, text="Edit Reaction Conditions", command=showInputField)
submitChangesButtonTemp = Button(inputFieldFrame, text="Submit Temperature", command=submitChangesTempF)
submitChangesButtonFlowRate = Button(inputFieldFrame, text="Submit Flow Rate", command=submitChangesFlowRateF)
submitChangesButtonPressure = Button(inputFieldFrame, text="Submit Pressure", command=submitChangesPressureF)
submitChangesElectrode1Button = Button(root, text="Submit Electrode 1", command=submitChangesElectrode1F)
submitChangesElectrode2Button = Button(root, text="Submit Electrode 2", command=submitChangesElectrode2F)
submitChangesReagent1Button = Button(root, text="Submit Reagent 1", command=submitChangesReagent1F)
submitChangesReagent2Button = Button(root, text="Submit Reagent 2", command=submitChangesReagent2F)
editReagentButton1 = Button(changeParameter, text="Edit Reagent 1", command=editReagentF1)
editReagentButton2 = Button(changeParameter, text="Edit Reagent 2", command=editReagentF2)
stopButton = Button(root, text="STOP", command=stopFunction)
setVariableTemperatureButton = Button(inputFieldFrame, text="Set Variable Temperature")
setVariableFlowRateButton = Button(inputFieldFrame, text="Set Variable Flow Rate")
setVariablePressureButton = Button(inputFieldFrame, text="Set Variable Pressure")
editElectrodeDimensionsButton = Button(changeParameter, text="Edit Electrode Dimensions", command=openElectrodeDimensionsF)
submitChangesElectrodeAreaButton = Button(electrodeDimensionsFrame, text="Submit Electrode Area", command=submitChangesElectrodeAreaF)
submitChangesElectrodeDistanceButton = Button(electrodeDimensionsFrame, text="Submit Electrode Distance", command=submitChangesElectrodeDistanceF)
backButton2 = Button(root, text="BACK", command=backButton2F)
backButton3 = Button(root, text="BACK", command=backButton3F)
editTubingButton = Button(changeParameter, text="View/Add Tube", command=editTubingF)
addTubeButton = Button(root, text="Add New Tube", command=addTubeF)
submitTubeButton = Button(inputFieldFrame2, text="Submit", command=submitTubeF)
setVariableButton = Button(changeParameter, text="Set/View Variable Condition", command = setVariableFunction)
timeStampButton = Button(root, text="Add new timestamp", command=timeStampF)
timeStampButtonTemperature = Button(timeStampFrame, text="submit temperature stamp", command=variableTempF)
timeStampButtonFlowRate = Button(timeStampFrame, text="submit flow rate stamp", command=variableFlowRateF)
timeStampButtonPressure = Button(timeStampFrame, text="submit pressure stamp", command=variablePressureF)








#home screen packs
runButton.grid(row=0, column=0)
runButtonFrame.grid(row=0, column=0)
editButton.grid(row=1, column=0)
#label1.grid(row=0, column =1)
labelReagent1.grid(row=0, column=0)
labelReagent2.grid(row=1, column=0)
electrodeLabel1.grid(row=2, column=0)
electrodeLabel2.grid(row=3, column=0)
labelReactionConditions.grid(row=4, column=0)
electrodeDimensionsLabel.grid(row=6, column=0)
editTubingButton.grid(row=7, column=0)
currentConditions.grid(row=1, column=1)








#loop
button_exit = Button(root, text="exit", command=root.quit)
button_exit.grid(row=3, column=1)
root.mainloop()
