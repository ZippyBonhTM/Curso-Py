# Comando básico => print() => Saída de arquivos.
# Mostra no terminal o objeto => print(<obj>).
# OBS: Muito utilizado para debugar o código, ou seja, encontrar falhas e ir testando as partes do código.
#Uma curiosidade do print(), é que ele 
print('Hello, World!')

# palavras chaves para string => \n Quebra de linha \t Tab. (São os mais usados, pesquisa depois mais alguns).

print('Hello,\nGabriel,\n\t teste')

# Variáveis;
# Conceito => <nome da variável> = <tipo(<valor>)>.
# Mas antes saiba que nem sempre é preciso dizer o tipo.
# Existe => str(), int(), floart() => Como tipso -primitivos-.
# Existe também arrays, mas isso é assunto para um próximo arquivo.

inteiro = int(100)
real = float(10.0)
string = str('Texto')
# Entrando em mais um conceito das strings;
print(f'Estas são as variáveis que eu declarei;\n\t{inteiro},\n\t{real},\n\t{string}.') # formatação de string, mais chamadas como -- f-strings --;
# Também chamadas de “strings literais formatadas” (formatted string literals), f-strings são strings com a letra f no início e chaves {} para realizar a interpolação de expressões. font: "https://pythonacademy.com.br/blog/f-strings-no-python".
# OUTPUT =>

# Estas são as variáveis que eu declarei;
# 	100,
# 	10.0,
# 	Texto.

# OBS: Você pode colocar qualquer valor nas váriáveis que não é declarado o tipo.

inteiro2 = 1
real2 = 1.0
string2 = 'Texto'

print(
    f"Tipos das variáveis;"
    f"\n\t{inteiro2} <=> {type(inteiro2)};"
    f"\n\t{real2} <=> {type(real2)};"
    f"\n\t{string2} <=> {type(string2)};"
    )

# A função type() mostra o tipo da variável, objeto ou array.
# A quebra de linha no print() pode ser feita a cada fechamento de "" sem problema, isso pode ser feito em outros casos que vou falar futuramente.

# Duas formas:
inteiro = int()
inteiro = 10
print(inteiro)
# OBS: não é preciso jogar um valor na variável quando declarada, o que significa que, para declarar uma variável, não será preciso dar a ela um valor.
# OUTPUT =>

# 10

# Os => int(), float(), str(), são funções que podem ser usadas para converter os tipos.
inteiro = 100
print(type(inteiro)) # Para mostrar o tipo antes da mudança.
#converter;
string = str(inteiro) # Transforma o valor inteiro para string.
print(type(string)) # Para mostrar o tipo depois da mudança.

# OUTPUT =>

# <class 'int'>
# <class 'str'>

# OBS: Nem tudo pode ser convertido em str()! Vou mostrar isso mais pra frente.