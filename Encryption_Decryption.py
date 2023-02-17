# Encryption And Decryption
def SquareMult(x, y, z):
    if (x == 0):
        return 0
    if (y == 0):
        return 1

    if (y % 2 == 0):
        l = SquareMult(x, y / 2, z)
        l = (l * l) % z

    else:
        l = x % z
        l = (l * SquareMult(x, y - 1, z) % z) % z
        return ((l + z) % z)


def MultInv(a, b):
    x = 1
    y = 0
    b1 = b
    if b == 1:
        return y

    while (a > 1):
        u = a / b
        v = b
        b = a % b
        a = v
        v = y
        y = x - u * y
        x = v

        if (x < 0):
            x = x + b1
            return x


def divide_msg():
    my_msg = "Hello professor do you want a cookie?"
    return [my_msg[i:i + 3] for i in range(0, len(my_msg), 3)]


chunk_msg = divide_msg()
print("Chunk Message is", chunk_msg)


def ASCIItoHEX(chunk_msg):
    list = []
    for i in chunk_msg:
        c = "".join([hex(ord(ch)) for ch in i])
        list.append(c.replace("0x", ""))
    return list


hex_list = ASCIItoHEX(chunk_msg)
print("Hexadecima value is", hex_list)


def HexatoInt(hex_list):
    List = [int(x, 16) for x in hex_list]
    return List


integer_list = HexatoInt(hex_list)
print("Integer value is", integer_list)

x = [pow(i, 1225393063, 2471549629) for i in integer_list]
print("Encrypted text is", x)
e = 1071682943
Phi = 3287313120
d = MultInv(e, Phi)

print("d: " + str(d))


def decrypt():
    x = [1011009140, 1843304476, 2477120276]
    y = [pow(i, 2652525887, 3287427827) for i in x]
    return y


y = decrypt()
print("Decrypted integer values are", y)

z = list()
var1 = [hex(i) for i in y]
for i in var1:
    z.append(i.replace("0x", ""))
print("Corresponding hexa_decimal values of decrypted integer", z)

var2 = [bytearray.fromhex(i).decode() for i in z]
print("Decrypted message in 3-byte chunks", var2)

decrypted_message = "".join(var2)
print("Decrypted message received from partner is:", decrypted_message)