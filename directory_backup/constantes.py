__author__ = 'Arkadoel'
from _datetime import datetime

VERSION = '0.1'

HELP = '''
uso: dirBackup [--help] [-cpone <origen> <destino>]
                [-cpmulti <origenes> <destino>]
                [-cpxml <fich xml>] [-gen_xml_template]

Descripcion de las ordenes:
    --help      Muestra la ayuda por pantalla
    -cpone      Copia un directorio a otro de destino
    -cpmulti    Copia una lista de directorios a uno de destino
                ejem: dirBackup -cpmulti '/home/user/d1;/home/user/d2' '/media/backups'
    -cpxml      Copia en base a un archivo .xml con los directorios y sus destinos
    -gen_xml_template   Genera un archivo .xml con el formato de entrada para el parametro -cpxml

'''


def get_hora():
    horas = datetime.now().hour
    minutos = datetime.now().minute
    segundos = datetime.now().second
    resultado = ''

    if horas <10:
        resultado += '0' + str(horas)
    else:
        resultado += str(horas)

    resultado += '_'

    if minutos <10:
        resultado += '0' + str(minutos)
    else:
        resultado += str(minutos)


    resultado += '_'

    if segundos <10:
        resultado += '0' + str(segundos)
    else:
        resultado += str(segundos)

    return resultado

def get_dia() -> str:
    '''
    Devuelve el dia
    :rtype : basestring
    :return: String
    '''
    resultado = ''
    anyo = datetime.today().year
    mes = datetime.today().month
    dia = datetime.today().day

    resultado += str(anyo)
    resultado += '_'

    if mes <10:
        resultado += '0' + str(mes)
    else:
        resultado += str(mes)

    resultado += '_'

    if dia < 10:
        resultado += '0' + str(dia)
    else:
         resultado += str(dia)

    return resultado
