#Link da Questão - https://leetcode.com/problems/longest-common-prefix/submissions/?envType=study-plan-v2&envId=top-interview-150

def longestCommonPrefix(strs):
    ans = "" #Iniciamos a variavel que ira conter os prefixos comuns
    strs = sorted(strs)#O primeiro passo é ordenar a lista de strings de forma alfabética, isso facilita o processo de verificar o prefixo
#Aqui temos um loop for, que vai iterar sobre as letras das strings da lista
    for i in range(min(len(strs[0]),len(strs[-1]))):
        if strs[0][i] != strs[-1][i]:#Aqui comparamos as letras da primeira palavra com a ultima
            #Caso forem diferentes, retornamos a variavel ans vazia
            return ans
        ans += strs[0][i]#Caso sejam iguais adicionamos a letra a nossa variavel
    return ans


print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["flower","flow","flight"]))