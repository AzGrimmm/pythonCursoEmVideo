cdt = 'Controle de terreno'
tam = len(cdt) + 4
def linha(tam):
    tam = len(tam) + 4
    print('-' * tam)
linha(cdt)
print(cdt.center(tam))
linha(cdt)

def area(largura, comprimento):
    area = largura * comprimento
    return area



largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))

print(f'A ârea de um terreno {largura}x{comprimento} é de: {area(largura, comprimento)}m²')