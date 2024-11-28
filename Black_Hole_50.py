import os
from time import time
import binascii
import math
import os.path
import sys

# @Author Jurijus Pacalovas
# Get the name of the current script

if os.path.basename(sys.argv[0]) != 'Black_Hole_50.py':
    sys.exit("This is not 'Black_Hole_50.py'.")

print("The script 'Black_Hole_50.py' is currently running.")


class compression:

    def cryptograpy_compression4(self):

        def process_file1(Extract1=0, File_information5_17="Ex", name="", x=0):
            if Extract1 == 1:
                with open(name + ".b", "wb") as f2:
                    f2.write(
                        binascii.unhexlify(
                            (
                                "%0"
                                + str((len(File_information5_17) // 8) * 2)
                                + "x"
                            )
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
            En += 1

            return En, Row1, Row

        import re

        def find_smallest_longl_F_values(input_string):

            # Extract all 'En', 'En2', 'Row', and 'Longl_F' values

            pattern = r'En=(\d+), Longl_F=(\d+)'

            matches = re.findall(pattern, input_string)

            # Convert the extracted strings to tuples of integers

            longl_F_values = [
                (int(en), int(longl_f)) for en, longl_f in matches
            ]

            if longl_F_values:

                # Find the smallest 'Longl_F' value and its corresponding variables

                smallest_longl_F_values = min(
                    longl_F_values, key=lambda x: x[1]
                )

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
                if i == 2:
                    import paq
                    data = paq.decompress(data)
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
                                if I8[long_F - 8] != "00000000":
                                    I8 += "00000000"
                                else:
                                    I8 += "11111111"

                                while block < long_F + 8:

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

                                        if FC < 5:

                                            FC = 0

                                        if Z7 == 0:

                                            if FC >= 5:

                                                Z7 = 1

                                                CZ = 1

                                                W1 = block - 16

                                                Sw1 = format(W // 8, '01b')

                                                Sw3 = format(len(Sw1), '05b')

                                                # print(FC)

                                                Sw2 = format(FC, '01b')

                                                Sw4 = format(len(Sw2), '05b')

                                                W3 += (
                                                    "0"
                                                    + IF1
                                                    + Sw3
                                                    + Sw1
                                                    + Sw4
                                                    + Sw2
                                                )

                                                W4 = W4[:W] + W4[W1:]

                                                FC = 0

                                if CZ == 0:

                                    W5 = W3 + "1"

                                elif CZ == 1:

                                    W5 = W3

                                W4 = W5 + W4

                                INFO = W4
                                long_F = len(INFO)
                                INFO = INFO[: long_F - 8]
                                Transform=INFO
                                Shora_decode=1
                                if Shora_decode==1:
                                #Shora Encode
                                    Transform="1"+Transform
                                    T8 = INFO
                                    Shora_decode=1
                                    if Shora_decode==1:
                                        # Input product
                                            try:
                                                product = int(Transform,2)
                                                #print(product)
                                                
                                                if product <= 0:
                                                    raise ValueError("Product must be a positive integer greater than 0.")
                                                
                                                # Step 1: Factorize the product into byte values (0-255)
                                                factors = []
                                                for i in range(2, 256):
                                                    while product % i == 0:
                                                        factors.append(i)
                                                        product //= i
                                                    if product == 1:
                                                        break  # Exit early if fully factored
                                            
                                                # If product is still greater than 1 and less than 256, it should be a valid byte
                                                if 1 < product < 256:
                                                    factors.append(product)
                                            
                                                # Step 2: Print the results
                                                #print(f"Input Product: {product}")
                                                #print(f"Factors (decoded byte values): {factors}")
                                            
                                                # Step 3: Confirm the product
                                                calculated_product = 1
                                                for byte in factors:
                                                    calculated_product *= byte
                                                #print(f"Product of Byte Values: {calculated_product}")
                                            
                                                # Step 4: Decode the byte values into a message (if possible)
                                                decoded_message = ''
                                                for n in factors:
                                                    if 32 <= n <= 126:  # Check if the byte corresponds to a printable ASCII character
                                                        decoded_message += chr(n)
                                                #print(f"Decoded Message (from byte values): {decoded_message}")
                                            
                                                # Step 5: Convert to Base 256 (Hexadecimal)
                                                base256_message = ' '.join(format(num, 'x') for num in factors)
                                                #print(f"Decoded Message in Base 256: {base256_message}")
                                            
                                                # Step 6: Convert to Binary (8 bits each)
                                                binary_message = ''.join(format(num, '08b') for num in factors)
                                                #print(f"Decoded Message in Binary (8 bits each): {binary_message}")
                                            
                                            except ValueError as e:
                                                print(f"Error: {e}")
                                      
                                    
                                    #print(binary_message)
                                    T10=binary_message
                                    INFO=T10
                                    
    
                                                                                                 
                               

                                # print(len(INFO))

                                Ci=1
                                if Ci == 1:

                                    # print(Find)

                                    TUPLE = ""

                                    N3 = 0

                                    long_F = len(INFO)

                                    block = 0

                                    FC = 0

                                    IF1 = ""
                                    TUPLE=INFO


                                Find=1


                                Ci=1
                                if Ci == 1:

                                    N3 = 1

                                    

                                    # print(N3)

                                    if N3 == 1:

                                        # print(Long_PM1)

                                        N3 = 1

                                        Circle_times += 1

                                        # print(Circle_times)

                                        #print(len(TUPLE))

                                        #print(long_11)

                                        INFO = TUPLE

                                        if Circle_times == 1:

                                            Circle_times2 = Circle_times

                                            long_11 = long_11 * 8

                                        Extract1 = 0

                                        if (
                                            len(TUPLE) <= long_11
                                            or Circle_times == 255
                                        ):

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

                                            SCircle_times = format(
                                                Circle_times2, '08b'
                                            )

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

                                                long_1 = len(
                                                    File_information5_17
                                                )

                                                add_bits = ""

                                                count_bits = 8 - long_1 % 8

                                                z = 0

                                                if count_bits != 0:

                                                    while z < count_bits:

                                                        add_bits = (
                                                            "0" + add_bits
                                                        )

                                                        z = z + 1

                                                File_information5_17 = (
                                                    add_bits
                                                    + File_information5_17
                                                )

                                                N4 = 3

                                                if N4 == 3:

                                                    File_information5 = (
                                                        File_information5_17
                                                    )

                                                    Check2 = (
                                                        File_information5_17
                                                    )

                                                    N5 == 1

                                                    if N5 == 1:

                                                        Ex = "00000000" + Check

                                                        File_information5_17 = (
                                                            Ex
                                                        )

                                                        elapsed_time = process_file1(
                                                            Extract1=1,
                                                            File_information5_17=File_information5_17,
                                                            name=name,
                                                            x=x,
                                                        )

                                                    Circle_times3 = 0

                                                    Extract1 = 0

                                                    Circle_times = 0

                                                    if Circle_times3 == 0:

                                                        long_16 = len(
                                                            File_information5
                                                        )

                                                        if (
                                                            File_information5[
                                                                :1
                                                            ]
                                                            == "0"
                                                        ):

                                                            while (
                                                                File_information5[
                                                                    :1
                                                                ]
                                                                != "1"
                                                            ):

                                                                if (
                                                                    File_information5[
                                                                        :1
                                                                    ]
                                                                    == "0"
                                                                ):

                                                                    File_information5 = File_information5[
                                                                        1:
                                                                    ]

                                                        if (
                                                            File_information5[
                                                                :1
                                                            ]
                                                            == "1"
                                                        ):

                                                            File_information5 = File_information5[
                                                                1:
                                                            ]

                                                    INFO = File_information5

                                                    if Circle_times3 == 0:

                                                        Circle_times4 = int(
                                                            INFO[:8], 2
                                                        )

                                                        # print(Circle_times4)

                                                        INFO = INFO[8:]

                                                    while Extract1 != 1:

                                                        


                                                        Extract1 = 0

                                                        TUPLE = ""

                                                        N3 = 0

                                                        long_F = len(INFO)

                                                        block = 0

                                                        Save = 0
                                                        #Shora Decode
                                                        Transform=INFO
                                                        print(INFO)
                                                        shora=1
                                                        if shora==1:
                            
                                                                    
                                                                    # Input product
                                                                        try:
                                                                            product = int(Transform,2)
                                                                            #print(product)
                                                                            
                                                                            if product <= 0:
                                                                                raise ValueError("Product must be a positive integer greater than 0.")
                                                                            
                                                                            # Step 1: Factorize the product into byte values (0-255)
                                                                            factors = []
                                                                            for i in range(2, 256):
                                                                                while product % i == 0:
                                                                                    factors.append(i)
                                                                                    product //= i
                                                                                if product == 1:
                                                                                    break  # Exit early if fully factored
                                                                        
                                                                            # If product is still greater than 1 and less than 256, it should be a valid byte
                                                                            if 1 < product < 256:
                                                                                factors.append(product)
                                                                        
                                                                            # Step 2: Print the results
                                                                            #print(f"Input Product: {product}")
                                                                            #print(f"Factors (decoded byte values): {factors}")
                                                                        
                                                                            # Step 3: Confirm the product
                                                                            calculated_product = 1
                                                                            for byte in factors:
                                                                                calculated_product *= byte
                                                                            #print(f"Product of Byte Values: {calculated_product}")
                                                                        
                                                                            # Step 4: Decode the byte values into a message (if possible)
                                                                            decoded_message = ''
                                                                            for n in factors:
                                                                                if 32 <= n <= 126:  # Check if the byte corresponds to a printable ASCII character
                                                                                    decoded_message += chr(n)
                                                                            #print(f"Decoded Message (from byte values): {decoded_message}")
                                                                        
                                                                            # Step 5: Convert to Base 256 (Hexadecimal)
                                                                            base256_message = ' '.join(format(num, 'x') for num in factors)
                                                                            #print(f"Decoded Message in Base 256: {base256_message}")
                                                                        
                                                                            # Step 6: Convert to Binary (8 bits each)
                                                                            binary_message = ''.join(format(num, '08b') for num in factors)
                                                                            #print(f"Decoded Message in Binary (8 bits each): {binary_message}")
                                                                        
                                                                        except ValueError as e:
                                                                            print(f"Error: {e}")
                                      
                                    
                                    #print(binary_message)

                                                        
                                                        T10=binary_message
                                                        TUPLE=T10
                                                        TUPLE1 = TUPLE
                                                        #print(T10)
                                                        TUPLE1=TUPLE
                                                        INFO=TUPLE
                                                        TUPLE=INFO
                                                        Find=1


                                                        Ci=1
                                                        if Ci == 1:
                        
                                                            N3 = 1
                        
                                                            
                        
                                                            # print(N3)
                        
                                                            if N3 == 1:
                        
                                                                # print(Long_PM1)
                        
                                                                N3 = 1
                        
                                                                Circle_times += 1
                        
                                                                # print(Circle_times)
                        
                                                                #print(len(TUPLE))
                        
                                                                #print(long_11)
                        
                                                                INFO = TUPLE
                        
                                                                if Circle_times == 1:
                        
                                                                    Circle_times2 = Circle_times
                        
                                                                    long_11 = long_11 * 8
                        
                                                                Extract1 = 0
                        
                                                                if (
                                                                    len(TUPLE) <= long_11
                                                                    or Circle_times == 255
                                                                ):
                        
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
                        
                                                                    SCircle_times = format(
                                                                        Circle_times2, '08b'
                                                                    )
                        
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
                        
                                                                        long_1 = len(
                                                                            File_information5_17
                                                                        )
                        
                                                                        add_bits = ""
                        
                                                                        count_bits = 8 - long_1 % 8
                        
                                                                        z = 0
                        
                                                                        if count_bits != 0:
                        
                                                                            while z < count_bits:
                        
                                                                                add_bits = (
                                                                                    "0" + add_bits
                                                                                )
                        
                                                                                z = z + 1
                        
                                                                        File_information5_17 = (
                                                                            add_bits
                                                                            + File_information5_17
                                                                        )
                        
                                                                        N4 = 3
                        
                                                                        if N4 == 3:
                        
                                                                            File_information5 = (
                                                                                File_information5_17
                                                                            )
                        
                                                                            Check2 = (
                                                                                File_information5_17
                                                                            )
                        
                                                                            N5 == 1
                        
                                                                            if N5 == 1:
                        
                                                                                Ex = "00000000" + Check
                        
                                                                                File_information5_17 = (
                                                                                    Ex
                                                                                )
                        
                                                                                elapsed_time = process_file1(
                                                                                    Extract1=1,
                                                                                    File_information5_17=File_information5_17,
                                                                                    name=name,
                                                                                    x=x,
                                                                                )


                                
                                if Extract1 == 1:
                                    n = int(File_information5_17, 2)
                                    width_bits = "%0{}x".format(
                                        (len(File_information5_17) // 8) * 2
                                    )
                                    jl = binascii.unhexlify(width_bits % n)
                                    import paq
                                    jl = paq.compress(jl)
                                    with open(f"{name}.b", "wb") as f2:
                                        f2.write(jl)
                                    x3 = time() - x
                                    print(f"Speed bits: {long_11 / x3:.5f}")
                                    print("checker seccefully")
                                    return str(float(x3))

                        if i == 2:

                            if C == 1:

                                Extract1 = 0

                                if File_information6_Times2 == 0:

                                    File_information5 = INFO

                                    Extract = 0

                                    Ex = INFO

                                    if Ex[:8] == "00000000":

                                        L = len(Ex[8:])

                                        File_information5_17 = Ex[8:]

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

                                        long = len(name)

                                        name2 = name[: long - 2]

                                        with open(name2, "wb") as f2:

                                            f2.write(width_bits3)

                                        x2 = time()

                                        x3 = x2 - x

                                        xs = float(x3)

                                        xs = str(xs)

                                        return xs

                                    if Circle_times3 == 0:

                                        long_16 = len(File_information5)

                                        if File_information5[:1] == "0":

                                            while File_information5[:1] != "1":

                                                if File_information5[:1] == "0":

                                                    File_information5 = (
                                                        File_information5[1:]
                                                    )

                                        if File_information5[:1] == "1":

                                            File_information5 = (
                                                File_information5[1:]
                                            )

                                    INFO = File_information5

                                    if Circle_times3 == 0:

                                        Circle_times4 = int(INFO[:8], 2)

                                        # print(Circle_times4)

                                        INFO = INFO[8:]

                                    while Extract1 != 1:
                                    	
                                        
                                        T8=INFO
                                        Transform=T8
                                        shora=1
                                        if shora==1:

                                        
                                            try:
                                                # Step 1: Ask the user to enter a binary string without spaces
                                                binary_input = Transform
                                                
                                                # Step 2: Validate the binary input and decode into byte values (0-255)
                                                if len(binary_input) % 8 != 0:
                                                    raise ValueError("Binary input must be a multiple of 8 bits.")
                                                
                                                byte_values = [int(binary_input[i:i+8], 2) for i in range(0, len(binary_input), 8)]
                                            
                                                # Step 3: Convert the byte values into base 256 (hexadecimal)
                                                base256_message = ''.join(format(num, '02x') for num in byte_values)
                                            
                                                # Step 4: Calculate the product of the byte values
                                                product = 1
                                                for byte in byte_values:
                                                    product *= byte
                                            
                                                # Step 5: Calculate the binary representation of the product
                                                product_binary = format(product, 'b')  # Binary representation without spaces
                                            
                                                # Step 6: Convert byte values back to binary representation (8 bits each, no spaces)
                                                binary_message = ''.join(format(num, '08b') for num in byte_values)
                                            
                                                # Step 7: Display the results
                                                #print(f"Input Binary: {binary_input}")
                                                #print(f"Byte Values (decoded from binary): {byte_values}")
                                                #print(f"Product of Byte Values: {product}")
                                                #print(f"Binary Representation of Product: {product_binary}")
                                                #print(f"Decoded Message in Base 256 (hexadecimal): {base256_message}")
                                                #print(f"Binary Representation (8 bits each, no spaces): {binary_message}")
                                                #print("The decoded message based on the byte values is displayed above.")
                                            
                                            except ValueError as e:
                                                print(f"Error: {e}")
                                   
                                        
                                        


                                        T10=product_binary
                                    #print(T10)
                                        TUPLE=T10
                                        TUPLE1 = TUPLE[1:]                                        
                                        INFO=TUPLE
                                        TUPLE=INFO
                                        long_L = len(TUPLE)

                                        # print(long_L)

                                        N3 = 1

                                        # print(N3)

                                        if N3 == 1:

                                            N3 = 1

                                            block = 0

                                            long_F = len(TUPLE)

                                            Z = TUPLE

                                            Z6 = ""

                                            Z7 = 0

                                            TUPLE1 = Z

                                            cut_b = 0

                                            long_F = len(TUPLE)

                                            while block < long_F:

                                                E = Z[block : block + 1]

                                                if E == "0" and Z7 == 0:

                                                    cut_b = 1

                                                    block += 1

                                                    E2 = Z[block : block + 8]

                                                    block += 8

                                                    E3 = int(
                                                        Z[block : block + 5], 2
                                                    )

                                                    block += 5

                                                    S5 = Z[block : block + E3]

                                                    if len(S5) == 0:

                                                        Extract1 = 0

                                                        File_information5_17 = (
                                                            Ex
                                                        )

                                                        elapsed_time = process_file(
                                                            Extract1=1,
                                                            File_information5_17=File_information5_17,
                                                            name=name,
                                                            x=x,
                                                        )

                                                        return elapsed_time

                                                    E1 = int(
                                                        Z[block : block + E3], 2
                                                    )

                                                    block += E3

                                                    TUPLE4 = int(
                                                        Z[block : block + 5], 2
                                                    )

                                                    block += 5

                                                    E5 = int(
                                                        Z[
                                                            block : block
                                                            + TUPLE4
                                                        ],
                                                        2,
                                                    )

                                                    block += TUPLE4

                                                    b = 0

                                                    E3 = ""

                                                    while b < E5 - 1:

                                                        E3 += E2

                                                        b += 1

                                                        # print(E2)

                                                    TUPLE1 = TUPLE1[block:]
                                                    E1 *= 8

                                                    TUPLE1 = (
                                                        TUPLE1[:E1]
                                                        + E3
                                                        + TUPLE1[E1:]
                                                    )

                                                    block += long_F

                                                elif E == "1" or Z7 == 1:

                                                    block += 1

                                                    Z7 = 1

                                                    if cut_b == 0:

                                                        TUPLE1 = TUPLE1[block:]

                                                        cut_b = 1

                                                        block += long_F

                                                        # print(block)

                                                # print(block)

                                            # print(Long_PM1)

                                            TUPLE = TUPLE1

                                            # print(len(TUPLE))

                                            N3 = 1

                                            Circle_times += 1

                                            # print(Circle_times)

                                            INFO = TUPLE

                                            Extract1 = 0

                                            N3 = 0

                                            # print(len(TUPLE))

                                            # print(Circle_times4)

                                            if Circle_times == Circle_times4:

                                                Extract1 = 1

                                                N3 = 2

                                            if N3 == 2:

                                                File_information5_17 = TUPLE

                                                long_1 = len(
                                                    File_information5_17
                                                )

                                                add_bits = ""

                                                count_bits = 8 - long_1 % 8

                                                z = 0

                                                if count_bits != 0:

                                                    while z < count_bits:

                                                        add_bits = (
                                                            "0" + add_bits
                                                        )

                                                        z = z + 1

                                                File_information5_17 = (
                                                    File_information5_17
                                                )

                                                if Extract1 == 1:
                                                    L = len(
                                                        File_information5_17
                                                    )
                                                    n = int(
                                                        File_information5_17, 2
                                                    )
                                                    width_bits = (
                                                        "%0"
                                                        + str((L // 8) * 2)
                                                        + "x"
                                                    )
                                                    width_bits3 = (
                                                        binascii.unhexlify(
                                                            width_bits % n
                                                        )
                                                    )
                                                    width_bits2 = len(
                                                        width_bits3
                                                    )
                                                    name2 = name[:-2]
                                                    start_time = time()
                                                    with open(
                                                        name2, "wb"
                                                    ) as f2:
                                                        f2.write(width_bits3)
                                                    elapsed_time = (
                                                        time() - start_time
                                                    )
                                                    speed_bits = (
                                                        long_11 * 8
                                                    ) / float(elapsed_time)
                                                    print(
                                                        f"Speed bits: {speed_bits:.5f}"
                                                    )
                                                    print("checker seccefully")
                                                    return str(elapsed_time)


d = compression()
xw1 = d.cryptograpy_compression4()
print(xw1)
