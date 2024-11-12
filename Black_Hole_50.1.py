import os

from time import time

import binascii

import math

import os.path

import sys



# @Author Jurijus Pacalovas

# Get the name of the current script



if os.path.basename(sys.argv[0]) != 'Black_Hole_50.1.py':

    sys.exit("This is not 'Black_Hole_50.1.py'.")



print("The script 'Black_Hole_50.1.py' is currently running.")





class compression:



    def cryptograpy_compression4(self):



        def process_file1(Extract1=0, File_information5_17="Ex", name="", x=0):

            if Extract1 == 1:

                with open(name + ".b", "wb") as f2:

                    f2.write(

                        binascii.unhexlify(

                            ("%0" + str((len(File_information5_17) // 8) * 2) + "x")

                            % int(File_information5_17, 2)

                        )

                    )

                    return str(time() - x)



        def process_file(Extract1=0, File_information5_17="Ex", name="", x=0):

            if Extract1 == 1:

                width_bits = (

                    "%0" + str((len(File_information5_17) // 8) * 2) + "x"

                ) % int(File_information5_17, 2)

                with open(name[:-2], "wb") as f2:

                    f2.write(binascii.unhexlify(width_bits))

                    return str(time() - x)









        def Count_adds(En, Row1, Row):



            Row += 1

           



            if Row == (8192 * 4) - 1:

                Row = 0



            if En == (8192 * 4) - 1:

                En = 255

            En+=1



            return En, Row1, Row



        import re



        def find_smallest_longl_F_values(input_string):



            # Extract all 'En', 'En2', 'Row', and 'Longl_F' values



            pattern = r'En=(\d+), Longl_F=(\d+)'



            matches = re.findall(pattern, input_string)



            # Convert the extracted strings to tuples of integers



            longl_F_values = [(int(en), int(longl_f)) for en, longl_f in matches]



            if longl_F_values:



                # Find the smallest 'Longl_F' value and its corresponding variables



                smallest_longl_F_values = min(longl_F_values, key=lambda x: x[1])



                return smallest_longl_F_values



            else:



                return None



        self.name = "Written: Jurijus pacalovas"



        N5 = 1



        if N5 == 1:



            Clear = ""



            name = input("What is name of file input? ")



            long_21 = len(name)



            name_f = name[long_21 - 2 :]



            if name_f == ".b":



                i = 2



            else:



                i = 1



            # print(i)

            if os.path.exists(name):



                print('Path is exists!')



            else:



                print('Path is not exists!')



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

            ZEROS_ONE_1 = ""

            Circle_times = 0

            Circle_times2 = 1

            Circle_times3 = 0

            CB = -1

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



                File_information5_23 = ""



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



                            if File_information6_Times3 == 1:



                                File_information5_2 = INFO



                            n = int(File_information5_2, 2)



                            width_bits = len(File_information5_2)



                            width_bits = (width_bits / 8) * 2



                            width_bits = str(width_bits)



                            width_bits = "%0" + width_bits + "x"



                            width_bits3 = binascii.unhexlify(width_bits % n)



                            width_bits2 = len(width_bits3)



                            data = width_bits3



                            long_15 = len(data)



                            INFO = bin(int(binascii.hexlify(data), 16))[2:]



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



                            A = int(Extact, 2)

                        long_13 = len(File_information5_2)



                        long_12 = len(File_information5_2)



                        if i == 1:



                            if long_17 > (2**28) - 1 and i == 1:



                                print("print file is too big!")



                                raise SystemExit



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



                                if I8[long_F-8]!="00000000":

                                    I8+="00000000"

                                else:

                                	I8+="11111111"



                                while block < long_F+8:



                                    IF = I8[block : block + 8]



                                    if FC == 0:



                                        IF1 = I8[block + 8 : block + 16]



                                    W4 += IF



                                    block += 8



                                    if IF1 == IF:



                                        # print(IF1)



                                        # print(IF2)



                                        FC += 1



                                        # print(FC)



                                        if FC == 1:



                                            W = block - 8



                                    if IF1 != IF:



                                        if FC < 3:



                                            FC = 0



                                        if Z7 == 0:



                                            if FC >= 3:



                                                Z7 = 1



                                                CZ = 1



                                                W1 = block - 16



                                                Sw1 = format(W//8, '1b')



                                                Sw3 = format(len(Sw1), '05b')



                                                # print(FC)



                                                Sw2 = format(FC, '1b')



                                                Sw4 = format(len(Sw2), '05b')



                                                W3 += "0" + IF1 + Sw3 + Sw1 + Sw4 + Sw2



                                                W4 = W4[:W] + W4[W1:]



                                                FC = 0



                                if CZ == 0:



                                    W5 = W3 + "1"



                                elif CZ == 1:



                                    W5 = W3



                                W4 = W5 + W4



                                INFO = W4

                                long_F = len(INFO)

                                INFO=INFO[:long_F-8]



                                # print(len(INFO))



                                while Find != 1:



                                    # print(Find)



                                    TUPLE = ""



                                    N3 = 0



                                    long_F = len(INFO)



                                    block = 0



                                    FC = 0



                                    IF1 = ""



                                    while block < long_F:



                                        INFO_A = INFO[block : block + En]



                                        longl = len(INFO_A)



                                        Counts = int(INFO_A, 2)



                                        C = format(Counts, '1b')



                                        C3 = En - len(C)



                                        # print(C1)



                                        if (C3 >= 6 and En <= (2 ** (C3 - 4) - 1)) or INFO_A[:3] in {"11", "10"}:

    

                                            # print(C3)



                                            Counts = int(INFO_A, 2)



                                            C = format(Counts, '1b')



                                            C4 = En - len(C)



                                            bit_width = math.ceil(math.log2(En + 1))



                                            C1 = format(C4, f'0{bit_width}b')



                                            C2 = format(longl, '06b')



                                            if C3 != 1:



                                                Z5 = "11" + C1 + C



                                                # print(Z5)



                                            if C3 == 1:



                                                Z5 = "10" + INFO_A[2:]



                                                # print(Z5)



                                                # print(INFO_A)



                                            # print(C1)



                                            # print(INFO_A)



                                        else:



                                            Z5 = INFO_A



                                            # not six Zeros_onesros else 7 Zeros_onesros or more left or 2-5 Zeros_onesros



                                        # change back



                                        # same siZeros_ones



                                        TUPLE += Z5



                                        # print(Find)



                                        block += En



                                    if Find == 2 or Row == (8192 * 4) - 2:



                                        Find = 1



                                        Extract1 = 1



                                    elif Row == (8192 * 4) - 3 and Find == 3:



                                        smallest_longl_F_values = (

                                            find_smallest_longl_F_values(input_string)

                                        )



                                        if smallest_longl_F_values:



                                            en, longl_F = smallest_longl_F_values



                                            En = int(en)



                                            Find = 2



                                    elif (

                                        len(TUPLE) + 8 + 13 + 8 + len(C1) < long_11 * 8

                                        and len(C1) != 0

                                    ):



                                        input_string += (

                                            "En="

                                            + str(En)

                                            + ", "

                                            + "Longl_F="

                                            + str(len(TUPLE))

                                            + " / "

                                        )



                                        if len(input_string) > 100:



                                            smallest_longl_F_values = (

                                                find_smallest_longl_F_values(

                                                    input_string

                                                )

                                            )



                                            if smallest_longl_F_values:



                                                en, longl_F = smallest_longl_F_values



                                                input_string = (

                                                    "En="

                                                    + str(en)

                                                    + ", "

                                                    + "Longl_F="

                                                    + str(longl_F)

                                                    + " / "

                                                )



                                                # print(input_string)



                                        Find = 3



                                        En, Row1, Row = Count_adds(En, Row1, Row)



                                        # print(En)



                                        # print(len(TUPLE))



                                    else:

                                            En, Row1, Row = Count_adds(En, Row1, Row)



                                if Ci == 1:



                                    N3 = 1



                                    W = "0" + str(len(C1)) + "b"



                                    CL1 = format(longl, W)



                                    CL2 = format(En, '15b')



                                    # print(N3)



                                    if N3 == 1:



                                        # print(Long_PM1)



                                        N3 = 1



                                        Circle_times += 1



                                        # print(Circle_times)



                                        # print(len(TUPLE))



                                        # print(long_11)



                                        INFO = CL2 + CL1 + TUPLE



                                        if Circle_times == 1:



                                            Circle_times2 = Circle_times



                                            long_11 = long_11 * 8



                                        Extract1 = 0



                                        if len(TUPLE) <= long_11 or Circle_times == 255:



                                            long_11 = len(TUPLE)



                                            INFOS = INFO



                                            Circle_times2 = Circle_times



                                        if (

                                            len(TUPLE) > long_11

                                            or Circle_times > Circle_times2 + 1

                                            or Circle_times == 255

                                        ):



                                            N3 = 2



                                            Extract1 = 1



                                        if N3 == 2:



                                            SCircle_times = format(Circle_times2, '08b')



                                            if Circle_times == 1:



                                                File_information5_17 = (

                                                    "1" + SCircle_times + INFO

                                                )



                                            if Circle_times != 1:



                                                File_information5_17 = (

                                                    "1" + SCircle_times + INFOS

                                                )



                                            N4 = 2



                                            if N4 == 2:



                                                long_1 = len(File_information5_17)



                                                add_bits = ""



                                                count_bits = 8 - long_1 % 8



                                                z = 0



                                                if count_bits != 0:



                                                    while z < count_bits:



                                                        add_bits = "0" + add_bits



                                                        z = z + 1



                                                File_information5_17 = (

          
