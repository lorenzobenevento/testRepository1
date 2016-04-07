 #import wallHeatTransfer from wallCalculation Script
 #data about resistances can be found in wallCalcultion file (in case of changes modify that file)

from wallCalculation import *
#import *: we have imported everything
#dictionary with different values of k for the brick object
#input dictionary  

glassProp = {"name":"glass", "k":0.9}
brickProp ={"name":"brick", "k": 0.87}
cementProp ={"name":"cement", "k": 1.5}
list_material = [glassProp,brickProp,cementProp]
list_size = [0.2 , 0.35 , 0.95]
#if i want to know a property and extract it (ex. conduct of cement)

#conductivity=list_material[2]["k"]
#se volessi metterlo dentro alla funzione wallCalc al posto di k=numero in R4 metto k=conductivity



def materialSensitivity(material_List,size_list):
    """this function performs a sensitivity analysis on the heat transfer, varying the material
    used in one of the resistances to understand which could be the suitable one;
    As input (since all the other functions annidated have been imported) it is just necessary to 
    enter a new material with its properties and update the list
    """
    
 #   i=0
   
  #  totHeat={}
    #for material in material_List
    heatResult={}
    for material in material_List:
       
   
        R4["k"]=material["k"]
        for size in size_list:
            
            R4["length"]=size
            heatTransfer = wallHeatTransfer(serieSet,parallelSet,Ri,Ro,Ti,To)
            
            nameOfMaterial = material["name"]
            inputString = "material : "+nameOfMaterial+ " size: "+str(size)
            heatResult[inputString]="Heat transfer [W]: "+str(heatTransfer["Heat transfer value is equal to: "])
            
            """conductivityMaterial="conductivity [W/mK]"
            sizeOfMaterial = "length [m]"
            heatResult[conductivityMaterial]= material["k"]
            heatResult[nameOfMaterial]= heatTransfer["Heat transfer value is equal to: "]
            heatResult[sizeOfMaterial]= size
            
            totHeat[i]=heatResult
            i= i + 1"""
        
    return heatResult
    
MatSensit = materialSensitivity(list_material,list_size)   
print MatSensit
    
#out put should be like this: result_sensitivity=  {"glass":253,"brick": 350,... } 
# the ouput can also be a list of dictionaries [{"name":"glass","HeatTransfer" : 253},{"name":"brick","HeatTransfer" : 352}]   