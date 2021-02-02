#STEP 207 - Polymorphism Assignment

#creating parent class
class Drawing:
    number = 0
    name = 'Product'
    revision = 'A'
    quantity = 0

    def information(self):
        infoD = '\nNumber: {}\nName: {}\nRevision: {}\nQuantity: {}\
                '.format(self.number,self.name,self.revision,self.quantity)
        return infoD

    def purpose(self): #a method to determine what is to be done with the drawing
        pathOptions = ['Make', 'New', 'Obsolete']
        print(pathOptions)
        purpose1 = input('Choose one of the preceding options: ')
        optionM = '"Send drawing to production Manager."'
        optionN = '"Send drawing to responsible engineer for sign-off."'
        optionO = '"Send drawing to all department leads."'
        if purpose1 == 'Make':
            print(optionM)
        elif purpose1 == 'New':
            print(optionN)
        else:
            print(optionO)
        

#creating a child class
class Part(Drawing):
    typ = 'Prototype'
    material = 'Steel'
    number = 10
    name = 'Widet'

    #utilizing polymorphism
    def purpose(self): #the option 'Revise' was 'Make' and it's corresponding string changed
        pathOptions = ['Revise', 'New', 'Obsolete']
        print(pathOptions)
        purpose1 = input('Choose one of the preceding options: ')
        optionM = '"Send drawing to Project Engineer for revise."\n'
        optionN = '"Send drawing to responsible engineer for sign-off."\n'
        optionO = '"Send drawing to all department leads."\n'
        if purpose1 == 'Revise':
            print(optionM)
        elif purpose1 == 'New':
            print(optionN)
        else:
            print(optionO)

    #methods for this child class
    def information(self):
        infoP = '\nNumber: {}\nName: {}\nRevision: {}\nQuantity: {}\nType: {}\nMaterial: {}\
                '.format(self.number,self.name,self.revision,self.quantity,self.typ,self.material)
        return infoP

    def analysis(self):
        revLetter = input('Enter the revision letter for this drawing: ')
        if revLetter != 'A':
            print('"No analysis required."')
        else:
            print('"Perform FEA analysis on component."')


#creating a child class
class Assy(Drawing):
    explodedView = 'No'
    partQty = 2
    number = 1
    name = 'Widget Assembly'

    #methods for this child class
    def information(self):
        infoA = '\nNumber: {}\nName: {}\nRevision: {}\nQuantity: {}\nExploded View: {}\nPart Quantity: {}\
                '.format(self.number,self.name,self.revision,self.quantity,self.explodedView,self.partQty)
        return infoA

    def dsnReview(self):
        string = '"Perform a design review prior to release."'
        return string

    #utilizing polymorphism
    def purpose(self): #the option 'Replace' was 'Obsolete' and it's corresponding string changed
        pathOptions = ['Make', 'New', 'Replace']
        print(pathOptions)
        purpose1 = input('Choose one of the preceding options: ')
        optionM = '"Send drawing to production Manager."\n'
        optionN = '"Send drawing to responsible engineer for sign-off."\n'
        optionR = '"Send drawing to testing."\n'
        if purpose1 == 'Make':
            print(optionM)
        elif purpose1 == 'New':
            print(optionN)
        else:
            print(optionR)
    

if __name__ == '__main__':
    drawing = Drawing()  #instantiating the class Drawing and giving it the name drawing
    print(drawing.information()) #then calling on its method
    drawing.purpose() 
    print()
 
    part = Part()  #instantiating the child class Part and giving it the name part
    print(part.information())
    part.analysis() #then calling on its methods
    part.purpose()
    print()

    assy = Assy()  #instantiating the child class Assy and giving it the name assy
    print(assy.information())
    print(assy.dsnReview()) #then calling on its methods
    assy.purpose()
  
