from Code import Encripter
from Code import Decoder

def AllProces(input):
    firstInstance = Encripter(input)
    print("char prob list: " ,firstInstance.CharProbalityCounter())
    #(firstInstance.CharProbalityCounter())
    (firstInstance.TreeMaker3())

    print("tree 2")
    tree = ""
    tree = (firstInstance.TreeMaker3())
    if len(tree) == 0:
        print("Creating a tree failed at: ", input)
    else:

        CharCode = (firstInstance.CharCodeMaker())
        if (CharCode) == -1:
            print("Creating code for char failed at: ", input)
        else:
            print(firstInstance.CodeCreater())

    firstDEcoder = Decoder(firstInstance.Code, firstInstance.charCode, len(firstInstance.text) )
    temporary = firstDEcoder.listMaker()
    print("Sup: " , firstDEcoder.Decoder(temporary[0], temporary[1]))

    secondInstance = Decoder(firstInstance.Code, firstInstance.charCode, len(firstInstance.text))
    print("decoded text by passing the char Code : " ,secondInstance.DecoderByKey())


    print()
    print("third Instance: ")
    thirdInstance = Decoder(firstInstance.Code, firstInstance.tree, len(firstInstance.text))
    #print("decoded text by extracting the char Code : " ,thirdInstance.DecoderByTree())

decodingList = ["CSACSKAMACSKACSACSKAMACSKA", "VALAMI", "AAAAAAAAAAA" ,"BABABABABABBA" ]
for i in decodingList:
    AllProces(i)
