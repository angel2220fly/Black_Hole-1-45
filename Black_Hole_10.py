import os
from time import time
import binascii
import math
import os.path
import sys

# @Author Jurijus Pacalovas
# Get the name of the current script

if os.path.basename(sys.argv[0]) != "Black_Hole_10.py":
    sys.exit("This is not 'Black_Hole_10.py'.")

print("The script 'Black_Hole_10.py' is currently running.")


class compression:
    def cryptograpy_compression4(self):

        self.name = "Created Quantum Software: Jurijus pacalovas"
        print(self.name)

        N5 = 1

        if N5 == 1:

            Clear = ""

         
            
            


            name = input("What is name of file input? ")
            C_1= input("compress: 1 or Extract: 2 ? ")

            long_21 = len(name)

            name_f = name[long_21 - 4:]
            
       
            if C_1=="2":

                i = 2

            else:

                i = 1
       
            

            # print(i)
            if os.path.exists(name):

                print("Path is exists!")

            else:

                print("Path is not exists!")

                raise SystemExit

            x = 0
            C1 = 1
            x1 = 0
            x2 = 0
            x3 = 0
            X2 = 0
            C1 = 0
            C2 = 0
            C3 = 0
            C4 = 0
            F10=0
           
            ZEROS_ONE_1 = ""
            Circle_times = 0
            Circle_times2 = 1
            Circle_times3 = 0
            CB = -1
            Times1 = 0
            Tc = 0
            x = time()
            File_information6_Times2_1 = 0
            name_2 = name
            Long_Change = len(name_2)
            compress_or_not_compress = 1

            File_information6_Times3 = 0

            if i == 2:

                C = 1

            Long_Change = len(name_2)
            s = ""
            File_information5 = ""
            File_information5_2 = ""
            Clear = ""
            Translate_info_Decimal = ""
            D = 0
            long_name = len(name)
            with open(name, "rb") as binary_file:

                data = binary_file.read()
                s = str(data)

                long_11 = len(data)

                long_17 = len(data)

                if long_17 == 0:

                    raise SystemExit

                END_working = 0

                File_information6_Times2 = 0

                File_information5_24 = ""

                INFO18 = ""

                File_information5_29 = ""

                SpinS = 0

                while END_working < 10:

                    File_information6_Times3 = File_information6_Times3 + 1

                    D = 1

                    if D == 1:

                        if File_information6_Times3 == 1:

                            INFO = bin(int(binascii.hexlify(data), 16))[
                                2:
                            ]  # data to binary

                            long_1 = len(INFO)

                            long_11 = len(data)

                            count_bits = (long_11 * 8) - long_1

                            z = 0

                            if count_bits != 0:

                                while z < count_bits:

                                    INFO = "0" + INFO

                                    z = z + 1

                            Check = INFO

                            File_information5_2 = INFO

                            Extact = File_information5_2

                        long_13 = len(File_information5_2)

                        long_12 = len(File_information5_2)


                        if i == 1:

                            Ex = 1

                            if Ex == 1:

                                Extract1 = 0

                                Find = 0

                                En = 3

                                Ci = 1

                                M1 = 0

                                Row1 = 0

                                input_string = ""

                                C1 = ""

                                Row = 0

                                I8 = INFO

                                W3 = ""

                                W4 = ""

                                block = 0

                                IF1 = ""

                                long_F = len(I8)

                                # print(long_F)

                                FC = 0

                                IF2 = ""

                                Z7 = 0

                                CZ = 0

                                if Circle_times == 0:

                                    SINFO = ""

                                    TUPLE = INFO

                                if Circle_times == 0:

                                    SINFO = INFO

                                long_bits_after = 0
                                long_bits_after_b = 0
                                long_bits_before = 0
                                times_compress = 0
                                long_after_bits = 0
                                long_bits_after_b_1 = 0
                                J = 1
                                long_F1 = long_F
                                long_one_time = long_F1
                                stop_compress = 0
                                while stop_compress != 1:
                                    block = 0
                                    long_after_bits = len(INFO)
                                    Transform = INFO
                                    long_F = len(Transform)
                                    T10 = ""
                                    c_c = 0
                                    
                                    if c_c==0:
                                        block=0
                                        is_not_compress=0
                                        F9=0
                                        #print()
                                        while block<long_F:
                                            F=Transform[block:block+24]
                                            if len(F)==8:
                                                F4=F
                                                F9=1
                                            F8=int(F,2)
                                            F4=format(F8,'023b')
                                            
                                           
                                            
                                            
                                    
                                    
                                    
                                            if len(F)!=0:
                              
                                                M2 = int(F, 2) % 2  # Get the modulo of Transform when divided by 2
                                                
                                                if M2 == 0:
                                                    M3 = (int(F, 2) // 2) +1  # Modify M3 based on the logic
                                                else:
                                                    M3 = (int(F, 2) // 2) +3  # Modify M3 based on the logic
                                     
                                                M4=format(M3,'023b')
                                                #print(len(M4))
                                                #print("compress: binary from str:", M4)
                                                M7=format(M3,'023b')
                                                
        
                                                encoded_result=M4
                                                
                                                #Decode:
                                                    
                                                if len(M4)==24:
                                                    is_not_compress=1
                                                    #print(M4)
                                                    
                                                F2=0
                                                F3=0
                                                
                                                F4=format(F8,'023b')
                                                                                                        
                                                M4=format(M3,'023b')
                                                if F9==1:
                                                    F4=F
                                                T10+=F4
                                                    
                                                #print(len(M4))
                                                #print("compress: binary from str:", M4)                                                    
                                                
                                                
                                                
                                            block+=24
                                            #print(block) 
                                    
                                        
                                        
                                        
                                        
                                      
                                        #print(block)
    
                                              
                                                                   

                                    INFO = T10
                                    T8 = T10
                                    #is_not_compress=1
                                    
                                        
                                    
                                    if is_not_compress==0:
                                        INFOS=INFO
                                    elif is_not_compress==1 and times_compress==0:
                                              F10=1
                                              INFOS=INFO
                                                             
                                                                            
                                    elif is_not_compress==1 and times_compress!=0:
                                    
                                        times_compress-=1

                                        
                                        
                                        #print(times_compress)
                                                   


                                    long_one_time = len(T10)
                                    #print(long_one_time)
                                    #print(len(INFO))

                                    if (
                                            long_one_time <= 256 or times_compress==(2**24)-1 or is_not_compress==1
                                        
                                    ):
                                        stop_compress = 1
                                        Compress_file = 1
                                    long_bits_after_b_1 = 1
                                    times_compress += 1
                                    if len(INFOS)==0:
                                        raise SystemExit
                                    INFO=INFOS
                                    

                                # print(Compress_file)
                                if Compress_file == 1:
                                    Extract1 = 1
                                    if Extract1 == 1:
                                        
                                       
                                        
                                                                                                              
   
                                        
                                        times_compression_format = format(
                                            times_compress, "01b"
                                        )
                                        # print(times_compression_format)
                                        times_255 = format(
                                            len(times_compression_format),
                                            "08b",
                                        )
                                        times_255p = format(
                                            len(times_255),
                                            "016b",
                                        )

                                        # print(times_255_p_255)
                                        #  long of file  start number file before

                                        I_F_B = format(long_F1, "01b")
                                        # long of long before of file
                                        I_F_B_L = format(len(I_F_B), "08b")

                                        # long of file
                                        l_F_N = len(INFO)
                                        # long of  last number file after
                                        I_F_A = format(l_F_N, "01b")
                                        #  After long of long of file
                                        I_F_A_L = format(len(I_F_A), "08b")
                                        File_information5_17 = (
                                            "1"
                                            + times_255p
                                            + times_255
                                            + times_compression_format
                                            + I_F_B_L
                                            + I_F_B
                                            + I_F_A_L
                                            + I_F_A
                                            + INFO
                                        )
                                        if F10==1:
                                            File_information5_17="00000000"+File_information5_17
                                            #print(INFO)
                                        

                                        long_1 = len(File_information5_17)
                                        add_bits = ""
                                        count_bits = (8 - long_1 % 8) % 8

                                        if count_bits > 0 and count_bits < 8:
                                            for _ in range(count_bits):
                                                add_bits = "0" + add_bits

                                    if Extract1 == 1:

                                        File_information5_17 = (
                                            add_bits + File_information5_17
                                        )
                                        L = len(File_information5_17)

                                        # print(L)

                                        n = int(File_information5_17, 2)

                                        width_bits = len(File_information5_17)

                                        width_bits = (width_bits // 8) * 2

                                        width_bits = str(width_bits)

                                        width_bits = "%0" + width_bits + "x"

                                        width_bits3 = binascii.unhexlify(
                                            width_bits % n
                                        )

                                        width_bits2 = len(width_bits3)

                                        File_information5_2 = Clear

                                        jl = width_bits3

                                        name1 = name + ".bin"

                                        with open(name1, "wb") as f2:

                                            f2.write(jl)

                                        x2 = time()

                                        x3 = x2 - x

                                        print(
                                            f"Speed bits: {(long_11) / x3:.5f}"
                                        )

                                        print("checker seccefully")

                                        xs = float(x3)

                                        xs = str(xs)

                                        return xs

                        if i == 2:

                            if C == 1:
                                Extract1 = 0
                                File_information5 = INFO
                                #print(INFO)
                                if INFO[:8]=="00000000":
                                    
                                    INFO=INFO[8:]
                                    TUPLE1=INFO
                                    #print(TUPLE1)
                                

                                # extract
                                else:

                                    if Circle_times3 == 0:
    
                                        long_16 = len(File_information5)
    
                                        if File_information5[:1] == "0":
    
                                            while File_information5[:1] != "1":
    
                                                if File_information5[:1] == "0":
    
                                                    File_information5 = (
                                                        File_information5[1:]
                                                    )
    
                                        if File_information5[:1] == "1":
    
                                            File_information5 = File_information5[
                                                1:
                                            ]
    
                                    INFO = File_information5
                                    # print(INFO)
    
                                    if Circle_times3 == 0:
                                        # times count extract
                                        
     
    
                                        CEI = int(INFO[:16], 2)
    
                                        # print(CE)
    
                                        INFO = INFO[16:]
    
                                        CE = int(INFO[:CEI], 2)
    
                                        # print(CE)
    
                                        INFO = INFO[CEI:]
    
                                        tce = int(INFO[:CE], 2)
    
                                        # print(tce)
    
                                        INFO = INFO[CE:]
                                        #############
    
                                        # INFO before file before size of file
                                        CE1 = int(INFO[:8], 2)
    
                                        # print(CE)
    
                                        INFO = INFO[8:]
                                        bfnz = int(INFO[:CE1], 2)
    
                                        # print(bfnz)
    
                                        INFO = INFO[CE1:]
                                        #############
    
                                        # INFO before file after size of file
                                        CE2 = int(INFO[:8], 2)
    
                                        # print(CE)
    
                                        INFO = INFO[8:]
                                        efnz = int(INFO[:CE2], 2)
    
                                        # print(efnz)
    
                                        INFO = INFO[CE2:]
                                        # e.g.: 12 8-10
                                        #############
    
                                        while Extract1 != 1:
                                            # 1 bits 21
                                            # 0 19
                                            long_F = len(INFO)
                                            #print(long_F)
                                            
                                            Transform=INFO
                                            
                                            compressed=Transform
                                            F2=0
                                            F3=0
                                            block=0
                                            TUPLE=""
                                            #print(INFO)
                                            while block<long_F:
                                                    F=Transform[block:block+15]
                                                    #print(F)
                                                    F2=0
                                                    F3=0
                                                    if len(F)==8:
                                                        
                                                    
                                                        block+=15
                                                        TUPLE+=F
                                                        
                                                        
                                                    if len(F)!=8:
                                                      
                                                
                                                    
                                                        while F3!=1:
                                                            
                                                                F1=format(F2,'024b')
                                                                    
                                                                M2 = int(F1, 2) % 2  # Get the modulo of Transform when divided by 2
                                                                
                                                                if M2 == 0:
                                                                    M5 = (int(F1, 2) // 2) + 1  # Modify M3 based on the logic
                                                                else:
                                                                    M5 = (int(F1, 2) // 2) + 3  # Modify M3 based on the logic
                                                                M6=format(M5,'023b')
                                                                if F==M6:
                                                                    TUPLE+=F1
                                                                    F3=1
                                                                F2+=1
                                                        block+=15
                                                        #print(block)                                                        
                                                            
                                                                                                  
                                                            
                                            TUPLE1 = TUPLE
                                            INFO = TUPLE
                                            #print(INFO)
        
                                            long_L = len(TUPLE)
                                            Tc += 1
                                            #print(Tc)
        
                                            if tce == Tc:
                                                Extract1 = 1
    
                                    if Extract1 == 1:
                                        num4 = int(TUPLE1, 2)
                                        # print(num4)
                                        C19 = "0" + str(bfnz) + "b"
                                        TUPLE1 = format(num4, C19)
                                        File_information5_17 = TUPLE1
    
                                    if Extract1 == 1:
                                        L = len(File_information5_17)
                                        n = int(File_information5_17, 2)
                                        width_bits = "%0" + str((L // 8) * 2) + "x"
                                        width_bits3 = binascii.unhexlify(
                                            width_bits % n
                                        )
                                        width_bits2 = len(width_bits3)
                                        name2 = name[:-2]
                                        start_time = time()
                                        with open(name2, "wb") as f2:
                                            f2.write(width_bits3)
                                        elapsed_time = time() - start_time
                                        speed_bits = (long_11 * 8) // float(
                                            elapsed_time
                                        )
                                        print(f"Speed bits: {speed_bits:.5f}")
                                        print("checker seccefully")
                                        return str(elapsed_time)


d = compression()
xw1 = d.cryptograpy_compression4()
print(xw1)