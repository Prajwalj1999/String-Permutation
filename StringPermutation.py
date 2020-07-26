str=input("Enter a String:")
strList=list(str)
NewStr=list(str)
val={}
for item in strList:
    if val.get(item,0)==0:
        val[item]=1
    else:
        val[item]=val[item]+1

StrLen=len(NewStr)
def permute(valDict,level):
    if level==0:
        print(''.join(NewStr) )
    else:
        for item in valDict.keys():
            if valDict[item]>0:
                NewVal=valDict.copy()
                NewStr[StrLen-level]=item   #lexicographical order
                NewVal[item]=NewVal[item]-1
                permute(NewVal,level-1)



permute(val,len(NewStr) )
