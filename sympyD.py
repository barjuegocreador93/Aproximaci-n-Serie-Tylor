from sympy import *
from sympy.parsing.sympy_parser import parse_expr





class SympyDer():
    def __init__(self,y,x,n,xmin=0,xmax=0,a=0):

        file=input("nombre del archivo: ")
        AproxSerieInit=int(input("Quiere realizar AproxSerie(1/0): "))
        if AproxSerieInit:
            xmin=float(input("xmiin: "))
            xmax = float(input("xmiin: "))
            a = float(input("a: "))
        y = parse_expr(input("y: "))
        n = int(input("n: "))
        self.fns = [y]
        for i in range(n):
            self.fns.append(diff(self.fns[i], x))
        content="from AproxError import AproxSerie,plt,fact\nfrom numpy import *\n"
        j=0
        if AproxSerieInit:
            self.arrf="["
        for i in self.fns:
            content+="def f"+str(j)+"(x):\n\treturn "+str(i)+"\n\n"
            if AproxSerieInit:
                self.arrf+="f"+str(j)
                if j<len(self.fns)-1:
                    self.arrf+=","
            j+=1

        if AproxSerieInit:
            self.arrf += "]"
            content+="p=AproxSerie("+str(xmin)+","+str(xmax)+","+self.arrf+","+str(a)+")"

        a=open(file,"w")
        a.write(content)
        a.close()

x=Symbol("x")
y=sin(x)
x=SympyDer(y,x,3)