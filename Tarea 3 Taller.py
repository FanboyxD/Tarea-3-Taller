hexa = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
    16: "G"
}
class Restas(object):
    def __init__(self):
        pass
    def restas(self,num1,num2,base):
        if (isinstance(num1,list)and(num2,list)and(base,int)):
            return self.resta_aux(num1,num2,base)
        else:return "Error"
    def resta_aux(self,num1,num2,base):
        if num1==[] and num2==[] and base>=0:
            return []
        elif num1[-1]>num2[-1]:
            return self.resta_aux(num1[:-1],num2[:-1],base)+[hexa[num1[-1]-num2[-1]]]
        elif num1[-1]==num2[-1]:
            return self.resta_aux(num1[:-1],num2[:-1],base)+[hexa[0]]
        elif num1[-1]<num2[-1]:
            return (self.resta_aux(num1[:-2]+[num1[-2]-1],num2[:-1],base))+[hexa[num1[-1]+base-num2[-1]]]

