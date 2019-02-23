#conditions for optimizations 

###########################################################################

for _, passenger in data.iterrows():
        sex = passenger["Sex"]
        age = passenger["Age"]
        sib = passenger["SibSp"]
        cabin = passenger["Cabin"]
        if  sex == "female":
            predictions.append(1)
        elif sex == "male":
            if age < 10 and sib <= 2:
                predictions.append(1)
            elif  20 <= age <= 30 and cabin == "A6":
                predictions.append(1)
            else:
                predictions.append(0)
        else:
            predictions.append(0)




############################################################33


for _, passenger in data.iterrows():
        sex = passenger["Sex"]
        age = passenger["Age"]
        sib = passenger["SibSp"]
        cabin = passenger["Cabin"]
        if  sex == "female":
            predictions.append(1)
        elif sex == "male":
            if age < 10 and sib <= 2:
                predictions.append(1)
            elif  20 <= age <= 30 and cabin == "A6":
                predictions.append(1)
            elif  30 <= age <= 40 and cabin == "D56":
                predictions.append(1)
            else:
                predictions.append(0)
        else:
            predictions.append(0)



###################################################################################


 for _, passenger in data.iterrows():
        sex = passenger["Sex"]
        age = passenger["Age"]
        sib = passenger["SibSp"]
        cabin = passenger["Cabin"]
        if  sex == "female":
            predictions.append(1)
        elif sex == "male":
            if age < 10 and sib <= 2:
                predictions.append(1)
            elif  20 <= age <= 30 and cabin == "A6":
                predictions.append(1)
            elif  30 <= age <= 40 and (cabin in ["D56","D35"]):
                predictions.append(1)
            else:
                predictions.append(0)
        else:
            predictions.append(0)


###################################################################################




for _, passenger in data.iterrows():
        sex = passenger["Sex"]
        age = passenger["Age"]
        sib = passenger["SibSp"]
        cabin = passenger["Cabin"]
        if  sex == "female":
            predictions.append(1)
        elif sex == "male":
            if age < 10 and sib <= 2:
                predictions.append(1)
            elif  (20 <= age <= 30) and (cabin in ["A6","C148"]):
                predictions.append(1)
            elif  (30 <= age <= 40) and (cabin in ["D56","D35"]):
                predictions.append(1)
            else:
                predictions.append(0)
        else:
            predictions.append(0)



################################################################################




