import Model


class Controller:
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        self.model = Model(self)

    in_c = ""
    out_c = ""
    
    def convert_num(in_c, input,  out_c):

        if in_c == "Binary":
            if out_c == "Hex": return Model.bin_to_hex(input)
            elif out_c == "Decimal": return Model.bin_to_dec(input)
            elif out_c == "Octal": return Model.bin_to_oct(input)

        if in_c == "Hex":
            if out_c == "Binary": return Model.hex_to_bin(input)
            elif out_c == "Decimal": return Model.hex_to_dec(input)
            elif out_c == "Octal": return Model.hex_to_oct(input)

        if in_c == "Decimal":
            if out_c == "Binary": return Model.dec_to_bin(input)
            elif out_c == "Hex": return Model.dec_to_hex(input)
            elif out_c == "Octal": return Model.dec_to_oct(input)
        
        if in_c == "Octal":
            if out_c == "Binary": return Model.oct_to_bin(input)
            elif out_c == "Hex": return Model.oct_to_hex(input)
            elif out_c == "Decimal": return Model.oct_to_dec(input)

    #Talks to Model to select File
    def selectFile():
        return Model.getFile()

    #Talks to Model to select units
    def selectUnits():
        return Model.selectUnits()

    #Talks to Model to graph
    def graphit():
        return Model.graph()

    def convert():
        pass