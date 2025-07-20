#PPS "A049"
def is_vowel(c):
    return c in 'aeiou'

def check_password(password):
    vol_check = False
    three_check = True
    two_check = True
    
    vowel_count = 0
    consonant_count = 0

    for i in range(len(password)):
        ch = password[i]

        if is_vowel(ch):
            vol_check = True
            vowel_count += 1
            consonant_count = 0
        else:
            consonant_count += 1
            vowel_count = 0
        
        if vowel_count == 3 or consonant_count == 3:
            three_check = False

        if i >= 1 and password[i] == password[i - 1]:
            if password[i] not in ('e', 'o'):
                two_check = False

    return vol_check and three_check and two_check

def main():
    while True:
        password = input().strip()
        if password == "end":
            break
        if check_password(password):
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")

main()