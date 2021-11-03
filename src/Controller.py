import Model
import View

class Controller:
    def __init__(self, parent):
        self.parent = parent
        self.model = Model(self)
        self.view = View(self)

    def get_num_output(input, in_c, out_c):

        if in_c == "bin":
            if out_c == "hex":
                return Model.bin_2_hex(input)
            elif out_c == "dec":
                return Model.bin_2_dec(input)
            elif out_c == "oct":
                return Model.bin_2_oct(input)

        if in_c == "hex":
            if out_c == "bin":
                return Model.hex_2_bin(input)
            elif out_c == "dec":
                return Model.hex_2_dec(input)
            elif out_c == "oct":
                return Model.hex_2_oct(input)

        if in_c == "dec":
            if out_c == "bin":
                return Model.dec_2_bin(input)
            elif out_c == "hex":
                return Model.dec_2_hex(input)
            elif out_c == "oct":
                return Model.dec_2_oct(input)
        
        if in_c == "oct":
            if out_c == "bin":
                return Model.oct_2_bin(input)
            elif out_c == "hex":
                return Model.oct_2_hex(input)
            elif out_c == "dec":
                return Model.oct_2_dec(input)


    
    def convert():
        pass
