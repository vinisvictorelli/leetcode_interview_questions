# Link da questão = https://leetcode.com/problems/length-of-last-word/submissions/?envType=study-plan-v2&envId=top-interview-150
# O desafio aqui é extrair a quantidade de caracteres da ultima palavra de uma string que é o input da função
def lengthOfLastWord(s):
    lastS = 0 #Aqui, criamos uma variavel que guarda a quantidade de letras da ultima palavra
    for i in range(len(s)-1,-1,-1): #For loop para varrer o string que vem como input
        if s[i] != " ": #Verifica se o caractere é diferente de um espaço vazio e assim adiciona 1 ao valor LastS
            lastS += 1
#Verifica para terminar o loop, verifica se o valor lastS é maior que 0. Isso faz com que caso tenhamos um espaço vazio
# antes da ultima palavra o loop não termina e verifica se o valor atual é um espaço vazio para terminar o loop. 
        elif lastS > 0 and s[i] == " ": 
            break
    print(lastS)

lengthOfLastWord("luffy is still joyboy")
        