#Faça o código Python p/ gerar as tabelas;
#A) (AvB) <-> (¬A ^ ¬B)

vetorPossibilidade= [True,False]

print('-------------------------------------')
print('Bem vindo ao Tabajara Plus 2.34 XP 9000')
print('-------------------------------------')
print('Teste da fórmula: (A <-> B) ^ ¬(A v B')

linhas=0
verdade=0
mentira=0

for a in vetorPossibilidade:
    for b in vetorPossibilidade:
        if (a or b) == (not a and not  b):
           resultadoF=True
           verdade+=1
        else:
            resultadoF=False
            mentira+=1   
            
        print(f'A = {a} \t B = {b} \t H={resultadoF}') 
        linhas+=1
            
print(f'Total de linhas com resultado VERDADEIRO:{verdade}') 
print(f'Total de linhas com resultados FALSO: {mentira}')
print(f'Total de linhas da tabela: {linhas}')



