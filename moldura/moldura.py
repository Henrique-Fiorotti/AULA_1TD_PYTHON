txt = input("Digite algo para fazer a moldura: \n")
ch = '\u2588'

for i in range(len(txt) + 4):
    print(ch, end= '')
print(f'\n{ch} {txt} {ch}')
for i in range(len(txt) ):
    print(ch, end='')

