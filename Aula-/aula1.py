# Comando básico => print() => Saída de arquivos.
# Mostra no terminal o objeto => print(<obj>).
# OBS: Muito utilizado para debugar o código, ou seja, encontrar falhas e ir testando as partes do código.

print('Hello, World!')

# palavras chaves para string => \n Quebra de linha \t Tab. (São os mais usados, pesquisa depois mais alguns).

print('Hello,\nGabriel,\n\t teste')

# Variáveis;
# Conceito => <nome da variável> = <tipo(<valor>)>.
# Mas antes saiba que nem sempre é preciso dizer o tipo.
# Existe => str(), int(), floart() => Como tipo -primitivos-.
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
