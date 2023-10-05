def canConstruct(ransomNote, magazine):
        for i in set(ransomNote):#Iterando sobre o objeto no formato set, dessa forma não terá caracteres repetidos para verificar
            if magazine.count(i) < ransomNote.count(i):#Constata se a quantidade de caracteres i em magazine é menor que em ransomNote
                #Caso a condição seja verdadeira em qualquer momento podemos dizer que é impossivel de se construir ransomNote com os caracteres em magazine
                return False
        return True#Caso o for loop seja completado podemos retornar True já que confirmamos a construção de ransomNote usando magazine