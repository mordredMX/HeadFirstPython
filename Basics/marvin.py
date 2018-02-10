def marvin1():
    paranoid_android="Marvin"
    letters=list(paranoid_android)
    for char in letters:
        print('\t',char)

def marvin2():
    paranoid_android="Marvin, the Paranoid Android"
    letters=list(paranoid_android)
    for char in letters[:6]:
        print('\t',char)
    print()
    for char in letters[-7:]:
        print('\t'*2,char)
    print()
    for char in letters[12:20]:
        print('\t'*3,char)


print("marvin1\n")
marvin1()
print("marvin2\n")
marvin2()