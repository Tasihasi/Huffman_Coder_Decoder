import re
from socket import SocketKind
from tempfile import TemporaryDirectory
from tkinter.tix import Tree




class Decoder:

    def __init__(self, input, key, textSize):
        self.input = input          # the code
        self.key = key              # is the tree
        self.size = textSize        # reviztit if needed
        


    def listMaker(self):                #creating the key array and the encripted text string
        char = []
        charCode = []
        temporaryNumbersList = []
        for i in range(len(self.key)):
            
            
            if self.key[i].isalpha():
                char.append(self.key[i])
                if i != 0:
                    charCode.append(temporaryNumbersList)
                    temporaryNumbersList = []
            else:
                temporaryNumbersList.append(self.key[i])
                

            if i + 1 == len(self.key):
                charCode.append(temporaryNumbersList)
        return char, charCode
   
    def Decoder (self, char, charCode):         #using the char, charCode decripting
        self.char = char
        self.charCode = charCode
        output = ""
        maxCharCodeLen = 0          #maximum bit size for a char

        for i in range(len(self.charCode)):
            if maxCharCodeLen < len(self.charCode[i]):
                maxCharCodeLen = len(self.charCode[i])
        #---------------- creating max char code -------------

        temporaryChar = []
        for i in range(len(self.input)):
            temporaryChar.append( self.input[i])
            for j in range(len(self.charCode)):
                if temporaryChar == self.charCode[j]:
                    output = output + char[j]
                    temporaryChar = []
        return output

    def DecoderByTree (self):      # getting the char codes from the tree and the code
        def CharAnswer(input):  # returning the input element
            if len(str(input)) == 1:   # if passed only one element give back that
                return self.key[int(input)]
            else:
                #return CharAnswer(input[0:len(input)-1])[int(str(input)[-1])]
                
                var = CharAnswer(input[0:len(input)-1])
                return var[int(str(input)[-1])]
                
                

        def ifChar(input):
            if type(CharAnswer(input)) == str or type(CharAnswer(input)[0]) == str:
                return True
            else:
                return False
        # ------------------
        # Testing 
        # ------------------

        #Char answer: ---- DONE ---- 
        
        #print("Testing char answer: ",CharAnswer('11'))

        # IfChar: ---- DONE ----
        #print('Testing If char: ', ifChar('01'))
        
        outPut = ''
        var = ''
        for i in self.input:
            var = var + i
            if ifChar(var):
                variant = CharAnswer(var)
                if type(variant) == str:

                    outPut = outPut + variant
                    var = ""
                elif type(variant[0]) == str:
                    outPut = outPut + variant[0]
                    var = ""
        return outPut
        

    def DecoderByKey(self):
        def CharFinder(input):    # finding the coresponding char
            for i in self.key:
                var = i[1:len(i)]             # stripping the first char from key

                if input == var:  
                    return i[0]
            return -1

        #for i in self.key:
            #print("Char finder Test: " , CharFinder(str(i[1:len(i)])))
        # The char dinder is tested working well

        
        value = ""
        var = ""
        for i in self.input:
            var = var + i
            if type(CharFinder(var)) == str:
                value = value + CharFinder(var)
                var = ""

        return value
    #using decoding by key is working        

#   ----------- Encripter -----------------------------
class Encripter:
    def __init__(self, text):
        self.text = text
        self.Code = ""

    def CharProbalityCounter (self):
        self.setText = set(self.text)
        outPut = []        
        counter = 0


        for i in ((self.setText)):
            for j in self.text:
                if j == i:
                    counter += 1
            outPut.append(i + str(counter))
            counter = 0
        # ----- counting elemets are done -----

        for i in range(len(outPut)):   
            for j in range(0, len(outPut) - i - 1):     
                if int(outPut[j][1]) > int(outPut[j + 1][1]):       
                    temp = outPut[j]
                    outPut[j] = outPut[j+1]
                    outPut[j+1] = temp

        # ------- sorting in decreasing order -----

        self.charProb = outPut
        return outPut
    '''
    def TreeMaker(self):
        # counting tree length
        maxCounter = 0
        for i in self.charProb:
            maxCounter = maxCounter + int(i[1])

        outPut = []
        temporary = []
        counter =   0 #int(self.charProb[0][-1])
        treeIndexCounter = 0

        for i in range(len(self.charProb)):
            

            if  i == 0:
                temporary.append(self.charProb[i][0])
                temporary.append(self.charProb[i + 1][0])
                counter =+ int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
            
                outPut.append(temporary)
                outPut.append(counter)
                temporary = []
                
                #treeIndexCounter += 1
            # ------ fisrt move is to start the tree ------

            elif i > 1 and int(outPut[-1]) <= int(self.charProb[i][1]) and counter < maxCounter:
                temporary.append(self.charProb[i][0])
                counter = counter +  int(self.charProb[i][1])
                outPut.append(temporary)
                outPut.append(counter)
                treeIndexCounter += 1
                temporary = outPut
                outPut = temporary
                temporary = []


            elif i + 1 < len(self.charProb) and i > 1 and counter < maxCounter:
                temporary.append(self.charProb[i][0])
                temporary.append(self.charProb[i + 1][0])
                counter = counter +  int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
            
                outPut.append(temporary)
                outPut.append(counter)
                temporary = []

            if counter == maxCounter:
                break
        

       
        
        self.tree = outPut
        return outPut

    def TreeMaker(self):
        # counting tree length
        maxCounter = 0
        for i in self.charProb:
            maxCounter = maxCounter + int(i[1])

        outPut = []
        temporary = []
        counter =   0 #int(self.charProb[0][-1])
        treeIndexCounter = 0

        for i in range(len(self.charProb)):
            

            if  i == 0:
                temporary.append(self.charProb[i][0])
                temporary.append(self.charProb[i + 1][0])
                counter =+ int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
            
                outPut.append(temporary)
                outPut.append(counter)
                temporary = []
                
                #treeIndexCounter += 1
            # ------ fisrt move is to start the tree ------

            elif i > 1 and int(outPut[-1]) <= int(self.charProb[i][1]) and counter < maxCounter:
                temporary.append(self.charProb[i][0])
                counter = counter +  int(self.charProb[i][1])
                outPut.append(temporary)
                outPut.append(counter)
                treeIndexCounter += 1
                temporary = outPut
                outPut = temporary
                temporary = []


            elif i + 1 < len(self.charProb) and i > 1 and counter < maxCounter:
                temporary.append(self.charProb[i][0])
                temporary.append(self.charProb[i + 1][0])
                counter = counter +  int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
            
                outPut.append(temporary)
                outPut.append(counter)
                temporary = []

            if counter == maxCounter:
                break
        

       
        
        self.tree = outPut
        return outPut


    
        

    def TreeMaker2(self):
        # counting tree length
        maxCounter = 0
        for i in self.charProb:
            maxCounter = maxCounter + int(i[1])

        outPut = []
        temporary = []
        counter =   0 #int(self.charProb[0][-1])
        treeIndexCounter = 0

        for i in range(len(self.charProb)):
                

            if  i == 0:
                temporary.append(self.charProb[i][0])
                temporary.append(self.charProb[i + 1][0])
                counter =+ int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
                
                outPut.append(temporary)
                outPut.append(counter)
                temporary = []
                    
                #treeIndexCounter += 1
                # ------ fisrt move is to start the tree ------

            elif i > 1 and int(outPut[-1]) <= int(self.charProb[i][1]) and counter < maxCounter:
                outPut = [outPut]
                temporary.append(self.charProb[i][0])
                counter = counter +  int(self.charProb[i][1])
                outPut.append(temporary)
                outPut.append(counter)
                treeIndexCounter += 1
                temporary = outPut
                outPut = temporary
                temporary = []


            elif i + 1 < len(self.charProb) and i > 1 and counter < maxCounter:
                outPut = [outPut]
                temporary.append(self.charProb[i][0])
                temporary.append(self.charProb[i + 1][0])
                counter = counter +  int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
                
                outPut.append(temporary)
                outPut.append(counter)
                temporary = []

            if counter == maxCounter:
                break
            

        
            
        self.tree = outPut
        print(outPut)
        return outPut
    
    ''' 

    def TreeMaker3(self):
        # counting tree length
        maxCounter = 0
        for i in self.charProb:
            maxCounter = maxCounter + int(i[1])

        outPut = []
        temporary = []
        counter =   0 #int(self.charProb[0][-1])
        treeIndexCounter = 0
        if len(self.charProb) == 1:
            outPut = [self.charProb[0] , maxCounter]
        elif len(self.charProb) == 2:
            outPut = [self.charProb[0], self.charProb[1] , maxCounter]
        else:

            for i in range(len(self.charProb)):
                    

                if  i == 0:
                    temporary.append(self.charProb[i][0])
                    temporary.append(self.charProb[i + 1][0])
                    counter =+ int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
                    
                    outPut.append(temporary)
                    outPut.append(counter)
                    temporary = []
                        
                    #treeIndexCounter += 1
                    # ------ fisrt move is to start the tree ------

                elif i > 1 and int(outPut[-1]) <= int(self.charProb[i][1]) and counter < maxCounter:
                    outPut = [outPut]
                    temporary.append(self.charProb[i][0])
                    counter = counter +  int(self.charProb[i][1])
                    outPut.append(temporary)
                    outPut.append(counter)
                    treeIndexCounter += 1
                    temporary = outPut
                    outPut = temporary
                    temporary = []


                elif i + 1 < len(self.charProb) and i > 1 and counter < maxCounter:
                    outPut = [outPut]
                    temporary.append(self.charProb[i][0])
                    temporary.append(self.charProb[i + 1][0])
                    counter = counter +  int(self.charProb[i][1]) + int(self.charProb[i + 1][1])
                    
                    outPut.append(temporary)
                    outPut.append(counter)
                    temporary = []

                if counter == maxCounter:
                    break
            

        
            
        self.tree = outPut
        print('Tree created successfully!')
        print(outPut)
        return outPut


    

    

    def CharCodeMaker(self):   # ----- Creates binary code for every char

        def CharSeeker(seekerList, Cchar):   # gives back value based on char and list
            side = 0
            outPut = ""
            #print(seekerList)
            if type(seekerList) != list:   # if we are lookin at a char
                if seekerList == Cchar:
                    return 0 
                else:
                    return -1
            else:
                if type(seekerList[0]) != list: # retunring value 
                    if seekerList[0] == Cchar:
                        if len(seekerList) > 1:
                            return 0
                        else:
                            return 
                    elif len(seekerList) > 1 and seekerList[1] == Cchar:
                        return 1
                    else:
                        return -1
            
                var = CharSeeker(seekerList[0], Cchar)
                if var == -1:
                    var = CharSeeker(seekerList[1], Cchar)
                    if var == -1:
                        return -1
                    else :
                        return "1" + str(var) 
                else:
                    return "0" + str(var)

        def CharSeeker2(seekerList, Cchar):   # gives back value based on char and list
            side = 0
            outPut = ""
            #print(seekerList)
            if type(seekerList) != list:   # if we are lookin at a char
                if seekerList == Cchar:
                    return 0 
                else:
                    return -1
            else:
                if type(seekerList[0]) != list: # we are looking at a list
                    if seekerList[0] == Cchar:
                        if len(seekerList) > 1: # checking if the list contains other elements
                            return 0
                        else:
                            return 
                    elif len(seekerList) > 1 and seekerList[1] == Cchar:
                        return 1
                    else:
                        return -1
            
                var = CharSeeker2(seekerList[0], Cchar) # if the list is bigger recurzive 
                if var == -1:
                    var = CharSeeker2(seekerList[1], Cchar)
                    if var == -1:
                        return -1
                    else :
                        return '1' +  str(var) 
                else:
                    return '0' +  str(var)
            
            #print("output: ", outPut)
        def CalleblaCharCode(seekerList, Cchar):  # Creating code for all Chars
            var = CharSeeker2(seekerList, Cchar)  # returning -1 if char not found
            if var == -1:
                print("Error: Char not found")
                self.charCode = ""
                return -1  
            outPut = ""
            for i in var:
                if i == "1":
                    outPut = outPut + "1"
                elif i == "0":
                     outPut = outPut + "0"
            return outPut

        maxCharProb = 0
        for i in self.charProb:
            if maxCharProb < int(i[1]):
                maxCharProb = int(i[1])
        
        
        char = []
        charCode = []
        for i in ((self.setText)):
            if (CalleblaCharCode(self.tree, i[0])) == -1:
                print("Error: Cannot create code for: ", i[0])
                return -1
            #char.append(i[0])
            charCode.append(str(i[0]) + str(CalleblaCharCode(self.tree, i[0])))
        self.charCode = charCode
        



        temporary = ""
        for i in charCode:
            temporary = temporary + i

        self.compactCharCode = temporary
        return charCode


    def CodeCreater (self):
        if len(self.charCode) == 0:
            print('Error at Code creating')
            self.Code = ""
            return
        def LastChar(text):
            output = ""
            for i in range(len(text)):
                if i != 0:
                    output = output + text[i]
            return output


        Code = ""
        for i in self.text:
            for j in range(len(self.charCode)):
                if self.charCode[j][0] == i:
                    Code = Code + str(LastChar(self.charCode[j]))
        self.Code = Code
        return Code
        

        
       
'''
    
firstInstance = Encripter("BELAALMAULISKAPITYAANNA")
print("char prob list: " ,firstInstance.CharProbalityCounter())
#(firstInstance.CharProbalityCounter())
(firstInstance.TreeMaker3())

print("tree 2")
(firstInstance.TreeMaker2())
print(firstInstance.CharCodeMaker())
print(firstInstance.CodeCreater())

firstDEcoder = Decoder(firstInstance.Code, firstInstance.charCode, len(firstInstance.text) )
temporary = firstDEcoder.listMaker()
print("Sup: " , firstDEcoder.Decoder(temporary[0], temporary[1]))

secondInstance = Decoder(firstInstance.Code, firstInstance.charCode, len(firstInstance.text))
print("decoded text by passing the char Code : " ,secondInstance.DecoderByKey())


print()
print("third Instance: ")
#thirdInstance = Decoder(firstInstance.Code, firstInstance.tree, len(firstInstance.text))
#print("decoded text by extracting the char Code : " ,thirdInstance.DecoderByTree())

'''

#    --------------- TO DO -------------------------

# The deoder gives back special variable '<'  ---- DONE ----


#The coder gives back more digits ---- DONE ---- 
# the char code creater has some problems 
#the deepest list contain one more 0 digit 

# passing the char code to the decoder working 
# finding solution how to get the chars code from the tree and the code 


#     --------   Further testing     ---------
# Goal is to separeta by the text by spaces and code by words 
# The encrypted message than passed by 
