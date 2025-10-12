def main():
    name = ['Amir','Ati','Reyhan']
    for i in range(len(name)):
        print(i+1)
        print(name[i])
        print(write_letter(name[i],"price"))
def write_letter(receive,sender):
    return f"""
=======================================================

DEAR {receive},
Hello
{sender}
======================================================
"""

main()