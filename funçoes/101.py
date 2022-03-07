def voto():
    from datetime import date
    nasc = int(input('Digite o ano de nascemento xxxx: '))
    anoAtual = date.today().year
    idade = anoAtual - nasc
    if idade < 16:
        print(f'Você tem {idade} anos  Situção: <NEGADO>')
    elif idade < 18 or idade > 70:
        print(f'Você tem {idade} anos  Situação: <OPÇIONAL>')
    else:
        print(f'Você tem {idade} anos  Situação: <PERMITIDO>')


voto()
