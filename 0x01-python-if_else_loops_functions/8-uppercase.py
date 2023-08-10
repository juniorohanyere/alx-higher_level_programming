 #!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) == ord(' '):
            print("{:s}".format(chr(ord(i))), end="")
        elif ord(i) >= ord('a') and ord(i) <= ord('z'):
            print("{:s}".format(chr(ord(i) - 32)), end="")
        elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
            print("{:s}".format(chr(ord(i))), end="")
        else:
            print("{:s}".format(chr(ord(i))), end="")
    print()
