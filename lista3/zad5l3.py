import re

print("Utwórz hasło, pamiętając, że musi zawierać:")
print("1) Od 6 do 16 znaków")
print("2) Przynajmniej jedną małą i jedną dużą literę")
print("2) Przynajmniej jedną cyfrę")
print("4) co najmniej jeden znak z grupy: $,#,@")
haslo = input()

def main(): 
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#])[A-Za-z\d@$#]{6,16}$"
    pat = re.compile(reg)                  
    mat = re.search(pat, haslo) 
    if mat:
        print("Hasło utworzone :)")
    else: 
        print("Nieprawidlowe hasło :(")

if __name__ == '__main__': 
    main() 