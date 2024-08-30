#Usuario inseri o numero incial e depois quantas vezes a soma ocorre.
n_inicial = int(input("insira o numero incial: "))
repeticao = int(input("Somar quantaos vezes? "))
repetir = 0
sequencia = [0, n_inicial]



while repetir < repeticao:
    #Adicona +1 a varialvel repetir, pega os ultimo e penultimo numero do array sequencia e adiciona a varialvel ultimo e penultimo
    repetir += 1
    ultimo = sequencia[-1]
    penultimo = sequencia[-2]
    # Soma os dois ultimos numeros do array sequencia e adiciona no final do array
    sequencia.append(ultimo + penultimo)
#imprime o resultado
print(sequencia)