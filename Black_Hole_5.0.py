from time import time
cvf=0
Portal=2
import os
import binascii
import math

Deep=400
Spin2=3112

lenf=0
name=""
szx=""
wer=""
namez = input("c: compress or e: extract? ")

f = open("PI_10M.txt", "r")
PI=f.read()


#@Author Jurijus pacalovas
class compression:
       
	def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas Date: 29/09/2021 18:06"
                
                if namez=="c" or namez=="e":
                    if namez=="c":
                        i=1
                    if namez=="e":
                        i=2
                    
                    #import mpmath as m
                    #m.mp.dps = 100000
                    #PI=4 * m.atan(1)

                    spin=0
                    c=0
                    A=0
                    Spin=0
                    sda4=""
                    sda5=""
                    sda6=""
                    e4a=""
                    e4b=""
                    ei8=""
                        
                    name = input("What is name of file? ")
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)

                    if i==2:
                        if nameas[nac-4:nac]!=".bin" and nameas[nac-3:nac]!=".b2":
                             print("Program close because this is file is not .bin")
                             raise SystemExit
                    Go=0
                             
                    if  i==2: 
                                long2=len(nameas)
                                nameas1=nameas[long2-3:]
                                if nameas1==".b2":
                                     Go=1
                                else:
                                    nameas=name[:nac-4]
                                    nac=len(nameas)
                        
                        
                    
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    nac=len(nameas)
                    
                    Circle_times3=0
                    cvf=2
                    cvf1=0
                    s=""
                    
                    e2=0
                    e3=1
                    e4=""
                    ei4=0
                    ei5=7
                    
                    e4=""
                    
                    c=2
                    sw=2
                    elw=0
                 
                    sda3=""
                    sda2=""

                    sda5=""
                    sda6=""
                    sda7=""
                    sda8=""
                    sda9=""
                    sda11=""
                    sda12=""
                    
                    sda14=""
                    sdaB=""
                    D=0

                    block=1
                    block2=0
                    block3=0
                    
                    count=0
                    
                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        
                       
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
         
                                                           
                        if Go==1:
                                    nameas=nameas[:long2-3]
                                    #print(nameas)
                                    
                                    
                                    with open(nameas, "ab") as f7:
                                        f7.write(data)
                                        print("Finish all done!")
                                    raise SystemExit              
                                
                        if lenf1<=1024:
                            if i==1:
                                long2=len(nameas)
                                nameas=nameas[:long2-4]
                                nameas=nameas+".b2"
                            
                            
                            with open(nameas, "ab") as f7:
                                f7.write(data)
                                print("Finish all done!")
                            raise SystemExit 
                       
                        
                        END_working=0
                        Circle_times2=0
                        ii=0
                        sda20=""
                        
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1

                            with open(nameas, "ab") as f2:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if Circle_times3==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**32)-1:
                                        raise SystemExit
                                        
                                    if lenf7<=82:
                                        raise SystemExit 
                                #########################################################################################################################################################
                                
                                block2=0
                                if i==2:

                                    lenf5=len(sda2)

                                    block2=0
                                    ei4=0
                                    ei5=1

                                    
                                    sda3=sda2
                                    
                                    block3=0
                                    Colaider3=""
                                   
                                    lenf5=len(sda3)
                                    
                                    
                                    #Extract
                                    
                                    
                                    s=""

                                    sda3=sda2
                                    lenf6=len(sda3)
                                    
                                    sda4=""
                                    sda5=""
                                    sda6=""
                                    sda7=""
                                    sda8=""
                                    sda9=""
                                    sda17=""
                                    Bytes_row4=""
                                    sda19=""
                                    
                                    ei=0

                                    if Circle_times2==0:
                                           
                                           g=1

                                    if g==1:

                                        if sda2[lenf5-8:lenf5]=="10000000":

                                            sda2=sda2[1:lenf5-8]

                                        elif sda2[lenf5-7:lenf5]=="1000000":

                                            sda2=sda2[1:lenf5-7]

                                        elif sda2[lenf5-6:lenf5]=="100000":

                                            sda2=sda2[1:lenf5-6]

                                        elif sda2[lenf5-5:lenf5]=="10000":

                                            sda2=sda2[1:lenf5-5]


                                        elif sda2[lenf5-4:lenf5]=="1000":

                                            sda2=sda2[1:lenf5-4]

                                        elif sda2[lenf5-3:lenf5]=="100":

                                            sda2=sda2[1:lenf5-3]

                                        elif sda2[lenf5-2:lenf5]=="10":

                                            sda2=sda2[1:lenf5-2]

                                        elif sda2[lenf5-1:lenf5]=="1":

                                            sda2=sda2[1:lenf5-1]

                                    g=0

                                    sda3=sda2

                                    lenf6=len(sda3)
                        
                                    count_times4=0

                                    FF=len(sda3)
                                    
                                    sda17=""
                                    sda19=""
                                    
                                    sda3=sda2
                                    Spin=0
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""
                                    sda17=""

                                    ei=0
 
                                    lenf6F=lenf6

                                    ei=0

                                    Spin=0

                                    while ei<lenf6F:

                                           sda9=sda3[ei:ei+1]
                                           sda12=sda3[ei:ei+3]
                                           sda18=sda3[ei:ei+34]
                                           lenf2=len(sda18)


                                           if Spin==Spin2:
                                               sda10=sda3[ei:ei+32]
                                               sda17=sda17+sda10
                                               lenf3=len(sda10)
                                               ei=ei+lenf3
                                               

                                           
                                           
                                        
                                           if sda12[0:1]=="0" and Spin<Spin2:
                                                         sda10=sda3[ei:ei+33]
                                                         sda10=sda10[1:]
                                                         sda17=sda17+sda10
                                                         ei=ei+33
                                                         Spin=Spin+1

                                           if sda12[0:3]=="100" and Spin<Spin2:

                                                         sda10=sda3[ei:ei+18]

                                                         sda10=sda10[3:]

                                                         lenf1=len(sda10)

                                                         N1 = int(sda10, 2)

                                                         lenf2=len(sda10)
                                                         
                                                           

                                                           

                                                         #32 bit 33 bit 31 bit

                                                         #print(sda10)
                                                         PI_take=str(PI)

                                                        

                                                        
                                                         N3 = PI_take[N1:N1+3]
                                                         N3=int(N3)
                                                         
                                                         N4=bin(N3)[2:]
                                                         
                                                         N7=len(N4)
                                                         
                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=32-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=32:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         
                                                        
                                                         sda17=sda17+szx2+N4
                                                         ei=ei+18


                                           if sda12[0:3]=="101" and Spin<Spin2:

                                                          

                                                         sda10=sda3[ei:ei+23]

                                                         sda10=sda10[3:]

                                                         

                                                         lenf1=len(sda10)

                                                         N1 = int(sda10, 2)

                                                         lenf2=len(sda10)
                                                         
                                                           

                                                           

                                                         #32 bit 33 bit 31 bit

                                                         #print(sda10)
                                                         PI_take=str(PI)

                                                        

                                                        
                                                         N3 = PI_take[N1:N1+5]
                                                         N3=int(N3)
                                                         
                                                         N4=bin(N3)[2:]
                                                         
                                                         N7=len(N4)
                                                         
                                                         lenf=len(N4)
                                                                 
                                                         szx2=""
                                                         xc=32-lenf
                                                         z=0
                                                         if xc!=0:
                                                               if xc!=32:
                                                                      while z<xc:
                                                                             szx2="0"+szx2
                                                                             z=z+1
                                                         
                                                        
                                                         sda17=sda17+szx2+N4
                                                         ei=ei+23
                                                         

                                           
                                        
                                                         
                                           if sda12[0:2]=="11" and Spin<Spin2:

                                                         sda10=sda3[ei:ei+31]
                                                         sda11=sda3[ei:ei+30]

                                                         sda10=sda10[2:]
                                                         sda11=sda11[2:]
                                                         if sda10[0:1]=="0":
                                                             sda10=sda10[1:]

                                                             sda10=sda10[4:6]+sda10[0:8]+sda10[4:6]+sda10[8:]
                                                             sda17=sda17+sda10
                                                             ei=ei+31
                                                             
                                                             

                                                         elif sda11[0:1]=="1":
                                                             sda11=sda11[1:]

                                                             sda11=sda11[4:6]+sda11[4:6][::-1]+sda11[0:8]+sda11[4:6][::-1]+sda11[8:]
                                                             sda17=sda17+sda11
                                                             ei=ei+30
                                                        
                                                         
                                                         
                                       

                                                         

                                           
                                           
                                    sda2=sda17
                                    Circle_times2=Circle_times2+1
                                    
                                    
                                    if   Circle_times2==Deep:
                                         #print(sda17)
                                       
                                         n = int(sda17, 2)
                                         qqwslenf=len(sda17)
                                         qqwslenf=(qqwslenf/8)*2
                                         qqwslenf=str(qqwslenf)
                                         qqwslenf="%0"+qqwslenf+"x"
                                         jl=binascii.unhexlify(qqwslenf % n)
                                         sssssw=len(jl)

                                         szxzzza=""
                                         szxzs=""
                                            
                                         f2.write(jl)
                                         x2 = time()
                                         x3=x2-x
                                         return print(x3)
                                        
                                if i==1:

                                    sda17=""
                                    sda19=""
                                    
                                    sda3=sda2
                                    Spin=0
                                    lenf6=len(sda3)
                                    ei4=0
                                    ei5=20
                                    block3=0
                                    Colaider3=""
                                    block2=0
                                    block3=0

                                    szx=""

                                    sda6=""

                                    #Compression

                                    sda9=""

                                    sda10=""
                                    sda11=""
                                    sda12=""
                                    sda13=""

                                    ei=0
 
                                    lenf6F=lenf6

                                    ei=0
                                    Spin=0

                                    while ei<lenf6F:

                                           sda10=sda3[ei:ei+32]#32 bit 33 bit 31 bit

                                           
                                           lenf1=len(sda10)

                                           N1 = int(sda10, 2)

                                           lenf2=len(sda10)

                                           N4=N1

                                           
                                           N1=str(N1)
                                           PI_take=str(PI)

                                           N3 = PI_take.find(N1)
                                           N6=str(N3)
                                           N5=len(N6)
                                           
                                           N7=len(N1)
                                           
                                                   
                                           if Spin<Spin2:

                                               if lenf2!=32:
                                                  sda17=sda17+"0"+sda10
                                           
                                        
                                              
                                               elif lenf2==32  and N7==3 and N3>=0:
                                                             N4=bin(N3)[2:]
                                                             

                                                             lenf=len(N4)
                                                                     
                                                             szx2=""
                                                             xc=15-lenf
                                                             z=0
                                                             if xc!=0:
                                                                   if xc!=15:
                                                                          while z<xc:
                                                                                 szx2="0"+szx2
                                                                                 z=z+1
                                                             
                                                             sda17=sda17+"100"+szx2+N4
                                                   
                                                             
                                               elif lenf2==32  and N7==5 and N3>=0:

                                                             N4=bin(N3)[2:]
                                                             

                                                             lenf=len(N4)
                                                                     
                                                             szx2=""
                                                             xc=20-lenf
                                                             z=0
                                                             if xc!=0:
                                                                   if xc!=20:
                                                                          while z<xc:
                                                                                 szx2="0"+szx2
                                                                                 z=z+1
                                                             sda17=sda17+"101"+szx2+N4


                                               

                                               elif sda10[0:2]==sda10[6:8] and sda10[0:2]==sda10[10:12]:
                                                            
                                                            
                                                            sda10=sda10[2:10]+sda10[12:]
                                                            
                                                    

                                                            sda17=sda17+"110"+sda10


                                               elif sda10[0:2]==sda10[6:8][::-1] and sda10[0:2]==sda10[10:12] and sda10[1:3]==sda10[10:12]:
                                                            
                                                            
                                                            sda10=sda10[3:10]+sda10[12:]
                                                            
                                                    

                                                            sda17=sda17+"111"+sda10
                                               else:
                                                        
                                                           
                                                        sda17=sda17+"0"+sda10
                                                        Spin=Spin+1


                                           elif Spin==Spin2:
                                               sda17=sda17+sda10
                                               


                                           ei=ei+32
                                                  
                                    sda6=sda4
                                    sda4=""
                                      
                                    #####################################################################################################################################################
                                                  
                                    block2=0
                                    
                                    Spinh=0              
                                    block2=0
                              
                                    e4=""
                                    e4a=""
                                    e4b=""
                                    block2=0
                                    sda5=""
                                     
                                    sda2=sda17
                                   

                                    if i==1:
                                        wer=""
                                        wer=sda6
                                        sda4=""
                                        szx=""
                                        
                                        Circle_times2=Circle_times2+1

                                        lenf9=len(sda17)
                                        #print(Circle_times2)
                                        
                                        
                                        if  Circle_times2==Deep:
                                            #print(lenf6-1)

                                            
                                            sda17="1"+sda17+"1"
                                            
                                            lenf=len(sda17)
                                            
                                            szx=""
                                            xc=8-lenf%8
                                            z=0
                                            if xc!=0:
                                                if xc!=8:
                                                    while z<xc:
                                                        szx="0"+szx
                                                        z=z+1

                                            lenf=len(sda17)
                                            B3=""

                                                                                      

                                            sda17=sda17+szx
                                            

                                            n = int(sda17, 2)
                                            qqwslenf=len(sda17)
                                            qqwslenf=(qqwslenf//8)*2
                                            qqwslenf=str(qqwslenf)
                                            qqwslenf="%0"+qqwslenf+"x"
                                            jl=binascii.unhexlify(qqwslenf % n)
                                            sssssw=len(jl)

                                            szxzzza=""
                                            szxzs=""
                                            sda2=sda6
                                              
                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)

                                            Speed=0

                                            if x3!=0:

                                                   Speed=(lenf7//xs)#B/s
                                                   print(Speed)
                                                   print("B/s")

                                            if x3==0:
                                                   print("FAST")

                                             
                                            return print(x3)

d=compression()

xw=d.cryptograpy_compression4()
print(xw)
