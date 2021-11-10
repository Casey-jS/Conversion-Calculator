import Model


class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model(self)
        

    def convert_num(in_c, input,  out_c):

        if in_c == "Binary":
            if out_c == "Hexadecimal":
                return Model.bin_2_hex(input)
            elif out_c == "Decimal":
                return Model.bin_2_dec(input)
            elif out_c == "Octal":
                return Model.bin_2_oct(input)

        if in_c == "Hexadecimal":
            if out_c == "Binary":
                return Model.hex_2_bin(input)
            elif out_c == "Decimal":
                return Model.hex_2_dec(input)
            elif out_c == "Octal":
                return Model.hex_2_oct(input)

        if in_c == "Decimal":
            if out_c == "Binary":
                return Model.dec_2_bin(input)
            elif out_c == "Hexadecimal":
                return Model.dec_2_hex(input)
            elif out_c == "Octal":
                return Model.dec_2_oct(input)
        
        if in_c == "Octal":
            if out_c == "Binary":
                return Model.oct_2_bin(input)
            elif out_c == "Hexadecimal":
                return Model.oct_2_hex(input)
            elif out_c == "Decimal":
                return Model.oct_2_dec(input)

    def selectFile():
        return Model.getFile()

    def selectUnits():
        return Model.selectUnits()

    def graphit():
        return Model.graph()

    def convert():
        pass