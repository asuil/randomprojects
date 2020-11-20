class C:
    #constructor
    def __init__(self,real=0,imaginary=0):
        self.__r=real
        self.__i=imaginary

    #translate to complex
    global com
    def com(self=0,x=0):
        if type(self)==str:
            ind=self.find('+')
            r=self[0:ind]
            i=self[ind+1:len(self)-1]
            if r.find('.')==-1: r=int(r)
            else: r=float(r)
            if i.find('.')==-1: i=int(i)
            else: i=float(i)
            return C(r,i)
        elif isinstance(self,C): return self
        elif type(self)==list: return C(self[0],self[1])
        else: return C(self,x)
        
    #real part
    def Re(self):
        return self.__r

    #imaginary part
    def Im(self):
        return self.__i

    #modulus
    def __abs__(self):
        return ((self.Re()**2)+(self.Im()**2))**(1.0/2)

    #angle
    def angle(self):
        import math
        if abs(self)==0: return 0
        if self.Re()>0 and self.Im()>0:
            a=math.asin(self.Im()/abs(self))
        if self.Re()<0 and self.Im()>0:
            a=math.asin(-self.Re()/abs(self))+(math.pi/2)
        if self.Re()<0 and self.Im()<0:
            a=math.asin(-self.Im()/abs(self))+math.pi
        if self.Re()>0 and self.Im()<0:
            a=math.asin(self.Re()/abs(self))+(3*math.pi/2)
        return a/math.pi*180

    #addition
    def __add__(self,c2):
        return C(self.Re()+c2.Re(),self.Im()+c2.Im())

    #comparison
    def __cmp__(self,c2):
        if self.Re()==c2.Re() and self.Im()==c2.Im(): return 0
        elif abs(self)>abs(c2): return 1
        elif abs(self)<abs(c2): return -1
        elif self.angle()>c2.angle(): return 1
        elif self.angle()<c2.angle(): return -1 

    #multiplication
    def __mul__(self,c2):
        r=self.Re()*c2.Re()-self.Im()*c2.Im()
        i=self.Re()*c2.Im()+self.Im()*c2.Re()
        return C(r,i)

    #conjugate
    def __invert__(self):
        return C(self.Re(),-self.Im())

    #division
    def __div__(self,c2):
        n=self*(~c2)
        d=c2.Re()**2-c2.Im()**2
        return C(r/d,i/d)

    #additive inverse
    def __neg__(self):
        return C(-self.Re(),-self.Im())

    #additive neutral?
    def __pos__(self):
        return self

    #to string
    def __str__(self):
        return str(self.Re())+'+'+str(self.Im())+'i'

    #substraction
    def __sub__(self,c2):
        return self+(-c2)
