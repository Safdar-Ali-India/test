import sys
def name(fist, last):
    print(f" First Name is {fist}")
    print(f" Last Name is {last}")
    return (f"Hello Dear {fist} {last}, How's You!")

print(name(sys.argv[1], sys.argv[2]))
