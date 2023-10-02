#link da questão = https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150
'''
A questão é uma função que recebe uma string com um número em algarismo romano, e a mesma deve retornar o número
que ele representa.
Para isso, é importante lembrar a regra para fazer a conversão de um algarismo romano, onde caso exista um número menor
a esquerda de um número maior, então executamos uma subtração. Caso o número menor esteja a direita de um número maior
executamos uma adição.
'''
def romanToInt(s):
        #aqui mapeamos cada algarismo para um número
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0 #criamos uma variável para guardar o valor que será retornado na função

        for i in range(len(s)):#aqui iteramos sobre a string que é o input da função
#Verificamos se o algarismo é o ultimo da string e se o valor é menor que o valor seguinte
            if i < len(s) - 1  and m[s[i]] < m[s[i+1]]: 
                ans -= m[s[i]] #Caso a condição seja verdade fazemos a subtração
            else:
                ans += m[s[i]]# Qualquer outro caso apenas fazer a adição

        return ans #Por fim, retornamos o valor