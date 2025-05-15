#SEM FUNÇÕES
print('¬'*85)
print('¬'*31, 'OLÁ MUNDO', '¬'*43)
print('¬'*85)
#COM FUNÇÕES, SEM PARÂMETROS
def lin():
    print('¬'*85)
lin()
print('¬'*31, 'OLÁ MUNDO', '¬'*43)
lin()
#COM FUNÇÕES, COM PARÂMETROS
def men(msg):
    print('¬'*85)
    print('¬'*31, (msg), '¬'*43)
    print('¬'*85)
print(men('OLÁ MUNDO'))