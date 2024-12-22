import os
import struct
import random
import paq
print("Created by Jurijus Pacalavas.")
print("Black_Hole_53")

# Symbol and space mapping (5-bit representation)
symbol_map = {
    " ": 0b00001,  # Space
    ".": 0b00010,
    ",": 0b00011,
    "?": 0b00100,
    "!": 0b00101,
    "-": 0b00110,
    "'": 0b00111,
    '"': 0b01000,
    ":": 0b01001,
    ";": 0b01010,
    "(": 0b01011,
    ")": 0b01100,
    "[": 0b01101,
    "]": 0b01110,
    "{": 0b01111,
    "}": 0b10000,
    "/": 0b10001,
    "\\": 0b10010,
    "@": 0b10011,
    "#": 0b10100,
    "$": 0b10101,
    "%": 0b10110,
    "^": 0b10111,
    "&": 0b11000,
    "*": 0b11001,
    "+": 0b11010,
    "=": 0b11011,
    "<": 0b11100,
    ">": 0b11101,
    "|": 0b11110,
    "~": 0b11111
}

# Reverse map for decoding
reverse_symbol_map = {v: k for k, v in symbol_map.items()}

# Function to count zeros in 5-bit values
def count_zeros_in_bin_values():
    zero_counts = {}
    for symbol, value in symbol_map.items():
        zero_count = bin(value).count('0')
        zero_counts[symbol] = zero_count
    return zero_counts

# Display the zero counts for each symbol
zero_counts = count_zeros_in_bin_values()
print("Zero counts in 5-bit binary values:")
for symbol, count in zero_counts.items():
    i = 0

# Compression Function (modified for 20-bit buffer)
def compress_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    if not input_filename.endswith('.txt'):
            import os
            from time import time
            import binascii
            import math
            import os.path
            import sys
            
            # @Author Jurijus Pacalovas
            # Get the name of the current script
            
            if os.path.basename(sys.argv[0]) != 'Black_Hole_53.py':
                sys.exit("This is not 'Black_Hole_53.py'.")
            
            print("The script 'Black_Hole_53.py' is currently running.")
            
            
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
                                                                    TUPLE=INFO
            
            
            
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
            
                                                                        # print(len(TUPLE))
            
                                                                        if N3 == 1:
            
                                                                            E = Z[
                                                                                block : block
                                                                                + 1
                                                                            ]
            
                                                                            if E == "0":
            
                                                                                cut_b = 1
            
                                                                                CB += 1
            
                                                                                block += 1
            
                                                                                E2 = Z[
                                                                                    block : block
                                                                                    + 8
                                                                                ]
            
                                                                                block += 8
            
                                                                                E3 = int(
                                                                                    Z[
                                                                                        block : block
                                                                                        + 5
                                                                                    ],
                                                                                    2,
                                                                                )
            
                                                                                block += 5
            
                                                                                S5 = Z[
                                                                                    block : block
                                                                                    + E3
                                                                                ]
            
                                                                                if (
                                                                                    len(S5)
                                                                                    == 0
                                                                                ):
            
                                                                                    File_information5_17 = (
                                                                                        "00000000"
                                                                                        + Check
                                                                                    )
            
                                                                                    Ex = Check
            
                                                                                    elapsed_time = process_file1(
                                                                                        Extract1=1,
                                                                                        File_information5_17=File_information5_17,
                                                                                        name=name,
                                                                                        x=x,
                                                                                    )
            
                                                                                    return elapsed_time
            
                                                                                E1 = int(
                                                                                    Z[
                                                                                        block : block
                                                                                        + E3
                                                                                    ],
                                                                                    2,
                                                                                )
            
                                                                                block += E3
            
                                                                                TUPLE4 = int(
                                                                                    Z[
                                                                                        block : block
                                                                                        + 5
                                                                                    ],
                                                                                    2,
                                                                                )
            
                                                                                block += 5
            
                                                                                E5 = int(
                                                                                    Z[
                                                                                        block : block
                                                                                        + TUPLE4
                                                                                    ],
                                                                                    2,
                                                                                )
            
                                                                                block += (
                                                                                    TUPLE4
                                                                                )
            
                                                                                b = 0
            
                                                                                E3 = ""
            
                                                                                while (
                                                                                    b
                                                                                    < E5 - 1
                                                                                ):
            
                                                                                    E3 += E2
            
                                                                                    b += 1
            
                                                                                    # print(E2)
            
                                                                                TUPLE1 = TUPLE1[
                                                                                    block:
                                                                                ]
                                                                                E1 *= 8
            
                                                                                TUPLE1 = (
                                                                                    TUPLE1[
                                                                                        :E1
                                                                                    ]
                                                                                    + E3
                                                                                    + TUPLE1[
                                                                                        E1:
                                                                                    ]
                                                                                )
            
                                                                                block += (
                                                                                    long_F
                                                                                )
            
                                                                            elif E == "1":
            
                                                                                block += 1
            
                                                                                Z7 = 1
            
                                                                                if (
                                                                                    cut_b
                                                                                    == 0
                                                                                ):
            
                                                                                    TUPLE1 = TUPLE1[
                                                                                        block:
                                                                                    ]
            
                                                                                    block += long_F
            
                                                                                    cut_b = (
                                                                                        1
                                                                                    )
            
                                                                                    # print(CB)
            
                                                                                    # print(block)
            
                                                                            else:
            
                                                                                block += 1
            
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
            
                                                                        if (
                                                                            Circle_times
                                                                            == Circle_times4
                                                                        ):
            
                                                                            Extract1 = 1
            
                                                                            if (
                                                                                Check
                                                                                == TUPLE
                                                                            ):
                                                                                File_information5_17 = (
                                                                                    Check2
                                                                                )
                                                                                if (
                                                                                    Check2[
                                                                                        :8
                                                                                    ]
                                                                                    == "00000000"
                                                                                ):
                                                                                    File_information5_17 = Check2[
                                                                                        8:
                                                                                    ]
            
                                                                            if (
                                                                                Check
                                                                                != TUPLE
                                                                            ):
            
                                                                                Ex = (
                                                                                    "00000000"
                                                                                    + Check
                                                                                )
            
                                                                                File_information5_17 = (
                                                                                    Ex
                                                                                )
            
                                                                                elapsed_time = process_file1(
                                                                                    Extract1=1,
                                                                                    File_information5_17=File_information5_17,
                                                                                    name=name,
                                                                                    x=x,
                                                                                )
            
                                                                                return elapsed_time
            
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
            return

    def load_dictionary(dictionary_file):
        word_to_index = {}
        try:
            with open(dictionary_file, "r", encoding=encoding) as f:
                for index, line in enumerate(f):
                    word = line.strip().lower()
                    word_to_index[word] = index
            return word_to_index
        except Exception as e:
            print("Error")
            return None

    word_to_index = load_dictionary(dictionary_file)
    if word_to_index is None:
        return

    try:
        with open(input_filename, "r", encoding=encoding) as infile:
            data = infile.read()

        compressed_data = bytearray()
        words = data.split(" ")

        for word in words:
            normalized_word = word.lower()
            if normalized_word in word_to_index:
                index = word_to_index[normalized_word]
                compressed_data.append(0x00)  # Dictionary flag
                compressed_data.extend(struct.pack(">I", index))  # Adjust this to use a 20-bit encoding if necessary
            else:
                compressed_data.append(0x01)  # Non-dictionary word
                compressed_data.extend(word.encode(encoding))

            # Encode space or symbols after the word
            if word.endswith(tuple(symbol_map.keys())):
                symbol = word[-1]
                symbol_code = symbol_map[symbol]
                compressed_data.append(0x02)  # Symbol flag
                compressed_data.append(symbol_code)
            else:
                compressed_data.append(0x02)  # Space flag
                compressed_data.append(symbol_map[" "])

        # PAQ compression
        final_compressed_data = paq.compress(bytes(compressed_data))

        with open(output_filename, "wb") as outfile:
            outfile.write(final_compressed_data)
            print(f"Compressed file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during compression: {e}")

# Extraction Function (modified for 20-bit buffer)
def extract_file(input_filename, output_filename, dictionary_file="Dictionary.txt", encoding="utf-8"):
    if not output_filename.endswith('.txt'):
        print("Error: Extracted file must have a .txt extension.")
        return

    def load_dictionary(dictionary_file):
        index_to_word = {}
        try:
            with open(dictionary_file, "r", encoding=encoding) as f:
                for index, line in enumerate(f):
                    word = line.strip()
                    index_to_word[index] = word
            return index_to_word
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            return None

    index_to_word = load_dictionary(dictionary_file)
    if index_to_word is None:
        return

    try:
        with open(input_filename, "rb") as infile:
            compressed_data = infile.read()

        decompressed_data = paq.decompress(compressed_data)

        decoded_data = bytearray()
        i = 0
        while i < len(decompressed_data):
            flag = decompressed_data[i]
            i += 1
            if flag == 0x00:  # Dictionary word
                if i + 3 <= len(decompressed_data):  # Ensure enough bytes for 3-byte 20-bit index
                    index = struct.unpack(">I", decompressed_data[i:i+3])[0]  # Decode a 20-bit index
                    word = index_to_word.get(index, "<unknown>")
                    decoded_data.extend(word.encode(encoding))
                    i += 3
                else:
                    print("Error: Insufficient data for dictionary word index.")
                    break
            elif flag == 0x01:  # Non-dictionary word
                word = bytearray()
                while i < len(decompressed_data) and decompressed_data[i] != 0x02:
                    word.append(decompressed_data[i])
                    i += 1
                decoded_data.extend(word)
            elif flag == 0x02:  # Symbol or space
                symbol_code = decompressed_data[i]
                i += 1
                symbol = reverse_symbol_map.get(symbol_code, " ")
                decoded_data.extend(symbol.encode(encoding))

        with open(output_filename, "w", encoding=encoding) as outfile:
            outfile.write(decoded_data.decode(encoding))
            print(f"Extracted file saved to '{output_filename}'.")
    except Exception as e:
        print(f"Error during extraction: {e}")

# Main Menu
def main():
    print("Choose an option:")
    print("1. Compress a file")
    print("2. Extract a file")
    print("3. Exit")

    while True:
        choice = input("Enter your choice (1/2/3): ").strip()
        if choice == '1':
            input_file = input("Enter the name of the file to compress (e.g., input.txt): ").strip()
            output_file = input("Enter the name of the compressed file (e.g., output.b): ").strip()
            compress_file(input_file, output_file)
        elif choice == '2':
            input_file = input("Enter the name of the file to extract (e.g., output.b): ").strip()
            output_file = input("Enter the name of the extracted file (e.g., output.txt): ").strip()
            extract_file(input_file, output_file)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()