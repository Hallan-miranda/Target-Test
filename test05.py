# Usuario insere a letra a ser invertida, configura a index para pegar a ultima carcter da palavra, depois 
# pegamos o tamanho da palavra e por fim a string_invertida guarda a palavra invertida.
string = str(input("Isira a string aqui: "))
index = -1
repeat = len(string)
string_invertida = ""

# Ciclo que repete x(tamanho da palavra) vezes e a cada vez adiciona o ultimo caracter da palvra na string_invertida.
while repeat > 0:
    repeat -= 1
    string_invertida += (string[index])
    index -= 1
print(string_invertida)