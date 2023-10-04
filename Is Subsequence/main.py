#Link da questão - https://leetcode.com/problems/is-subsequence/?envType=study-plan-v2&envId=top-interview-150

def isSubsequence(s, t):
        ans = 0 #Aqui temos a variavel que dirá se retornamos true ou false
        for i in range(0,len(t)):#Aqui iteramos sobre a string t
#Verificamos se ans é igual ao tamanho da string s e se o valor no index ans é igual ao valor da string t no index i
            if ans == len(s) and s[ans] == t[i]:
                ans += 1
                #Caso verdadeiro, adicionamos um a variavel ans e mudamos para o proximo index
        return ans == len(s)
#Depois de sair do loop for retornamos True se ans for igual ao tamanho da string s, assim confirmando que a subsequencia s existe em t

isSubsequence("abc","ahbgdc")
