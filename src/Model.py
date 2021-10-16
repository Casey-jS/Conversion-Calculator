#Decimal Conversions
#
#
#decimal to binary
def dec_to_bin(decimal):
    return bin(decimal)[2:]

#decimal to hex
def dec_to_hex(dec):
    return hex(dec)[2:]

#decimal to octal
def  dec_to_oct(dec):
    return oct(dec)[2:]

#Binary Conversions
#
#
#binary to decimal
def bin_to_dec(binary):
    dec = 0
    count = 0
    while(binary != 0):
        n = binary % 10
        dec = dec + n * pow(2, count)
        binary = binary // 10
        count += 1
    return dec

#binary to hexadecimal
def bin_to_hex(bin):
    dec = int(bin, 10)
    return hex(dec)

#binary to octal
def bin_to_oct(bin):
    dec = int(bin, 10)
    return oct(dec)

#Hex Conversions
#
#
#hexadecimal to decimal
def hex_to_dec(hex):
    dec = 0

    for i, j in enumerate(hex):
        hexList = "0123456789ABCDEF"
        val = hexList.index(j)
        power = (len(hex) - (i + 1))
        dec = dec + (val*16**power)
    return dec

def hex_to_oct(hex):
    dec = int(hex, 10)




