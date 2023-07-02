# Comando básico => print() => Saída de arquivos.
# Mostra no terminal o objeto => print(<obj>)

print('Hello, World!')

# palavras chaves para string => \n Quebra de linha \t Tab. (São os mais usados, pesquisa depois mais alguns).

print('Hello,\nGabriel,\n\t teste')

# Variáveis;
# Conceito => <nome da variável> = <tipo(<valor>)>
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
