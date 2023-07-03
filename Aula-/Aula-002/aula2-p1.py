var_verdade = True
var_falso = False

if var_verdade == True: # Essa maneira diz se a variavel tem o valor boolean True.
    print('var_verdade é verdadeiro')

if var_verdade: # Essa maneira funciona porém com uma mecânica diferente. Ela verifica se var_verdade foi definida (se tem valor dentro OU não é False).
    print('var_verdade é verdadeiro') 

# if => se
'''
Dizendo o código em português;

var_verdadeiro = verdadeiro

se var_verdadeiro é igual a verdadeiro, faça;
    mostre('A var_verdadeiro é verdadeiro')
'''

# OBS: Os síbulos = e == são diferentes (O = se chama "Recebe" e o == se chama "igual".)

# Os booleans values são:
# True  = Verdadeiro
# False = Falso
# None  = Nulo


'''
----- Operadores lógicos -----
== Igual
!= Diferente
> Maior que
< Menor que
>= Maior ou igual a
<= Menor ou igual a
'''

# Mais uma coisa:

if 1 == 1 and 1 == 2: # -- O  "And" significa "e", ou seja, 1 == 1 e 1 == 2?
    print(False)
else: # ------------------ Significa "Se não, faça;"
    print(False)

# Sendo assim essa esrtutura vai cair no "else" e printar falso já que o "if" não passou.

# Existe também o "Or":
if 1 == 1 or 1 == 2: # O "Or" significa "ou", ou seja, 1 == 1 ou 1 == 2?
    print(True)
else:
    print(False)

