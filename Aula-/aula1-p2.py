# Uso do input() =>
nome = input('Digite seu nome: ') # Fará uma pergunta no terminal e colocará dentro da variável "nome".
print(f'Olá {nome}, como você está?')

#OUTPUT =>

# Digite seu nome: John 
# Olá John, como você está?

# Você pode declara o tipo =>

nome2 = str(input('Digite seu nome: ')) # Se você digitar um valor que não seja str, ele vai converter para str.
print(f'Olá {nome2}, como você está?')

# OUTPUT =>

# Digite seu nome: 100  
# Olá 100, como você está?
