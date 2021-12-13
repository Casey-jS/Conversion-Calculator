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
            elif out_c == "Binary": return Model.same_unit(input)

        if in_c == "Hex":
            if out_c == "Binary": return Model.hex_to_bin(input)
            elif out_c == "Decimal": return Model.hex_to_dec(input)
            elif out_c == "Octal": return Model.hex_to_oct(input)
            elif out_c == "Hex": return Model.same_unit(input)

        if in_c == "Decimal":
            if out_c == "Binary": return Model.dec_to_bin(input)
            elif out_c == "Hex": return Model.dec_to_hex(input)
            elif out_c == "Octal": return Model.dec_to_oct(input)
            elif out_c == "Decimal": return Model.same_unit(input)
        
        if in_c == "Octal":
            if out_c == "Binary": return Model.oct_to_bin(input)
            elif out_c == "Hex": return Model.oct_to_hex(input)
            elif out_c == "Decimal": return Model.oct_to_dec(input)
            elif out_c == "Octal": return Model.same_unit(input)

    in_l = ""
    out_l = ""

    def convert_length(in_l, input,  out_l):
        input = float(input)

        if in_l == "Inch":
            if out_l == "Feet": return Model.in_to_feet(input)
            elif out_l == "Yards": return Model.in_to_yard(input)
            elif out_l == "Miles": return Model.in_to_mi(input)
            elif out_l == "Centimeter": return Model.in_to_cm(input)
            elif out_l == "Meter": return Model.in_to_me(input)
            elif out_l == "Kilometer": return Model.in_to_km(input)
            elif out_l == "Inch": return Model.same_length_unit(input)

        if in_l == "Feet":
            if out_l == "Inches": return Model.feet_to_in(input)
            elif out_l == "Yards": return Model.feet_to_yards(input)
            elif out_l == "Miles": return Model.feet_to_mi(input)
            elif out_l == "Centimeter": return Model.feet_to_cm(input)
            elif out_l == "Meter": return Model.feet_to_m(input)
            elif out_l == "Kilometer": return Model.feet_to_km(input)
            elif out_l == "Feet": return Model.same_length_unit(input)
  
        if in_l == "Yards":
            if out_l == "Inches": return Model.yards_to_inches(input)
            elif out_l == "Feet": return Model.yards_to_feet(input)
            elif out_l == "Miles": return Model.yards_to_mi(input)
            elif out_l == "Centimeter": return Model.yards_to_cm(input)
            elif out_l == "Meter": return Model.yards_to_m(input)
            elif out_l == "Kilometer": return Model.yards_to_km(input)
            elif out_l == "Yards": return Model.same_length_unit(input)

        if in_l == "Miles":
            if out_l == "Inches": return Model.mi_to_inches(input)
            elif out_l == "Feet": return Model.mi_to_feet(input)
            elif out_l == "Yards": return Model.mi_to_yards(input)
            elif out_l == "Centimeter": return Model.mi_to_cm(input)
            elif out_l == "Meter": return Model.mi_to_m(input)
            elif out_l == "Kilometer": return Model.mi_to_km(input)
            elif out_l == "Miles": return Model.same_length_unit(input)

        if in_l == "Centimeter":
            if out_l == "Inches": return Model.cm_to_in(input)
            elif out_l == "Feet": return Model.cm_to_feet(input)
            elif out_l == "Yards": return Model.cm_to_yd(input)
            elif out_l == "Miles": return Model.cm_to_mi(input)
            elif out_l == "Meter": return Model.cm_to_m(input)
            elif out_l == "Kilometer": return Model.cm_to_km(input)
            elif out_l == "Centimeter": return Model.same_length_unit(input)

        if in_l == "Meter":
            if out_l == "Inches": return Model.m_to_in(input)
            elif out_l == "Feet": return Model.m_to_feet(input)
            elif out_l == "Yards": return Model.m_to_yards(input)
            elif out_l == "Miles": return Model.m_to_miles(input)
            elif out_l == "Centimeter": return Model.m_to_cm(input)
            elif out_l == "Kilometer": return Model.m_to_km(input)
            elif out_l == "Meter": return Model.same_length_unit(input)

        if in_l == "Kilometer":
            if out_l == "Inches": return Model.km_to_in(input)
            elif out_l == "Feet": return Model.km_to_feet(input)
            elif out_l == "Yards": return Model.km_to_yards(input)
            elif out_l == "Miles": return Model.km_to_mi(input)
            elif out_l == "Centimeter": return Model.km_to_cm(input)
            elif out_l == "Meter": return Model.km_to_m(input)
            elif out_l == "Kilometer": return Model.same_unit(input)




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