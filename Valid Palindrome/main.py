#Link da questão - https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

def isPalindrome(s):
    i, j = 0, len(s) - 1 #Index do primeiro e ultimo caractere
    while i < j:
        a, b = s[i].lower(), s[j].lower() #Pega caracteres e coloca em lowercase
        if a.isalnum() and b.isalnum(): #Primeiro verifica se o caractere atual é alfanumerico
            if a != b: #Caso o caratere inicial e o final sejam diferentes, retornamos False porque não é um palindromo
                return False
            else:
                i, j = i + 1, j - 1 #Aumenta o index inicial por um e o final por menos um
                continue
        i, j = i + (not a.isalnum()), j - (not b.isalnum())
    return True

isPalindrome("raceacar")