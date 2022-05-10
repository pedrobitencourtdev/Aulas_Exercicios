def vermelho(tex=0,cor=True):
    vermelho = f'\033[1;31m{tex}\033[m'
    return vermelho


def verde(tex=0):
    verde = f'\033[1;32m{tex}\033[m'
    return verde


def azul(tex=0):
    azul = f'\033[1;34m{tex}\033[m'
    return azul
