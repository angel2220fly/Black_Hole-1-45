import os  

from time import time

import binascii

import math

import os.path



#@Author Jurijus pacalovas



class compression:
    def cryptograpy_reverse(self):

                                    
                    self.name = "Created: Jurijus Pacalovas"                                    

                

                 

                    

                    name = input("What is name of file? ")
                    
                    if os.path.exists(name):
                        print('Path is exists!')
                    else:
                        print('Path is not exists!')
                        raise SystemExit
                    


                    name_new="file.Secret"

                    name_2=""

                    name_2_clear="?"
                 
                    stop=0



                 

                  

                  

                 
                  


                    INFO3=""

                    INFO4=""

                    INFO5=""
                    
               



                   

                 
                 

                    

                  

                    name_1=name

                    name_of_file=len(name_1)

                    name_1=name
                  

                    

                    name_of_file=len(name_1)

                    

                    count_numbers=0

                    counts_1=2

                 

                    s=""

                

                 

                 

                 
                 
                
                    count_N=0

                    select_words=2

                    elements_words=0

                 

                    INFO3=""

                    INFO_OR_DATA_TO_BINARY=""



                    size_of_size_cosscounts_1=0

                    

                    binary_to_data=0
                    times_count=0
                    count_N3=0
                    reverse_bin=0



                   

                    r=""
                    Er="0"
                    INFO__1=0
                    INFO__2=1
                    INFO__3=2
                    INFO_LIST= []
                    INFOS=""

                    c1=0
                    c2=0
                    c3=0
                    stop=0
                    

                    x=0

                    x1=0

                    x2=0

                    x = time()



                    

                    with open(name, "rb") as binary_file:




                       # Read the whole file at once

                        data = binary_file.read()
                        
                       
                        s=str(data)

                       

                        long1=len(data)

                        long5=len(data)
                        long5_before_1=len(data)
                        if long5_before_1>=2**32:
                            print("This is file is too big")
                            raise SystemExit
                        if long5_before_1==0:
                            raise SystemExit

                        

                        times_numbers_reapits=0

                        binary_to_data_1=0

                        

                       

                        while times_numbers_reapits<10:

                       

                            aas1=0

                            a1=0



                            counts_1=counts_1+1

                            

                            count_numbers=count_numbers+1



                            with open(name_1, "ab") as f2:

                                if count_numbers==1:
                                    # 256 range data to binary
                                    bits_long="0"+str(long1*8)+"b"



                                    b=int(binascii.hexlify(data),16)
                                    INFO=format(b,bits_long)
                                    
                                    ####################                                   
                                    INFO_OR_DATA_TO_BINARY=INFO
                                    FF=INFO
                                    INFO11=INFO
                                    long3=len(INFO_OR_DATA_TO_BINARY)

                                long2=len(INFO_OR_DATA_TO_BINARY)
                                block=0
                                X=2
                                st=0
                                st1=0
                                                               
                                long_INFO = len(INFO)
                                long_file=len(INFO)
                                block2=0
                                INFO4=INFO
                                
                                #print(INFO4)
                               
                               
                                block=0
                                
                                
                                INFO1=""
                                INFO_add=""
                                INFO8=""
                                long_file=len(INFO4)
                                E=-1
                                A1=1
                                INFO11=""
                         
                              
                                block=0
                             
                                while block<long_file:
                                    INFO=INFO4[block:block+3]
                                    INFO8=""
                                    #01,100,101,110,111,11,000 0-3 2 1,0 E
                                    
                              
                                    
                                
                                    E+=1
                                    A1+=1
                                    
                                    if INFO[:1]=="1"  and 0 < A1 <= 29:
   

                                        INFO1="0"
                                        block+=1
                                    elif INFO[:1]=="0" and 0 < A1 <= 29:
                                        INFO1="1"
                                        block+=1
                                        
                                       
                                    elif INFO[:2]=="01" and E%3==0:
                                        INFO1="00"
                                        block+=2
                                        INFO2="000"
                                        #print(INFO)
                                        

                                    
                                    
                                    elif INFO[:2]=="00" and E%3==0:
                                       
                                        
                                        INFO1="01"
                                        block+=2
                                        INFO2="0"
                                    
                                    elif INFO[:3]=="001" and E%3>=1:
                                        INFO1="000"
                                        block+=3
                                        INFO2="000"
                                        #print(INFO)
                                        

                                    
                                    
                                    elif INFO[:3]=="000" and E%3>=1:
                                       
                                        
                                        INFO1="001"
                                        block+=3
                                        INFO2="0"
                                    
                                    elif INFO[:3]=="010" and E%3>=1:
                                        INFO1="011"
                                        block+=3
                                        INFO2="000"
                                        #print(INFO)
                                        

                                    
                                    
                                    elif INFO[:3]=="011" and  E%3>=1:
                                       
                                        
                                        INFO1="010"
                                        block+=3
                                        INFO2="0"
                                           
                                    else:
                                       
                                        if E%3==0:
                                        
                                            INFO1=INFO[:1]
                                            block+=1
                                            INFO2="0"
                                        elif E%3==1:
                                        
                                            INFO1=INFO[:3]
                                            block+=3
                                            INFO2="0"                                                                                                                                                                          
                                        else:
                                                                                    
                                            INFO1=INFO[:2]
                                            block+=2#
                                            INFO2="0"                                    
                                    #print(block)
                                  
                                    INFO_add+=INFO1
                                  
                                     
                                    
                                   
                                    
                                                      

                                count_N+=1
                               # print(count_N)
                           
                                INFO_OR_DATA_TO_BINARY1=INFO_add
                                #print(INFO_add)
                                INFO_OR_DATA_TO_BINARY=INFO_OR_DATA_TO_BINARY1+INFO8
                                INFO=INFO_OR_DATA_TO_BINARY
                                
                                
                                                                        
                                                                        
                                
                                #print(INFO)
                                

                                

                                if count_N==1 or stop==1 or len(INFO)<=8:#1b-8b len(INFO)<=256 saved
                                    
                            

                                       

                                     
                                        #print(count_H)
                                
                                        count_N=0
                                                                      
                                
#print(len(INFO_OR_DATA_TO_BINARY))
                                            
               

                                        n = int(INFO_OR_DATA_TO_BINARY, 2)

                                            

                                        binary_data=len(INFO_OR_DATA_TO_BINARY)

                                        binary_data=(binary_data/8)*2

                                        binary_data=str(binary_data)

                                        binary_data="%0"+binary_data+"x"

                                         

                                        jl=binascii.unhexlify(binary_data % n)

                                        binary_to_data_2=len(jl)

                                        data=jl
                                     
                                       
                                                                         
                                       

                                       

                                        binary_to_data_1=binary_to_data_1+1

                                        binary_to_data_3=""

                                        size_x=""

                                        

                                        reverse_bin=reverse_bin+1

                                        if reverse_bin==1:

                                                times_numbers_reapits=10

                                                if times_numbers_reapits==10:
                                                
                                                    with open(name, "wb") as binary_file:
                                                        
                                                        

                                                    

                                                        f2.write(jl)

                                                    x2 = time()

                                                    x3=x2-x

                                                    return print(x3)
                                            
                                        

                                      

                                            

                                    


#############################################################################
#############################################################################
   
d=compression()



xw=d.cryptograpy_reverse()

print(xw)
