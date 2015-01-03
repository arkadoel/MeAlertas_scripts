__author__ = 'https://github.com/Arkadoel'
__license__ = 'GPLv2'

import sys
import directory_backup.constantes as const
import shutil
import errno
import os

class Ordenes:

    def print_help(self):
        '''
        Imprime por pantalla la ayuda del comando
        :return:
        '''
        print(const.HELP)

    def cpone(self, parametros=None, ignorar=None):
        '''

        :param parametros: tupla con el directorio de origen y el de destino
        :param ignorar: tupla de extensiones a ignorar
        :return:
        '''
        dir_origen = str(parametros[0]).replace("'", "")
        dir_destino = str(parametros[1]).replace("'", "")
        if ignorar is not None:
            extensiones = shutil.ignore_patterns(ignorar)
        else:
            extensiones = None

        dir_destino += os.path.sep + const.get_dia() + '__' + const.get_hora()

        print('copiar ' + dir_origen + ' en ' + dir_destino)
        self.copy_directory(dir_origen, dir_destino, ignora=extensiones)

    def cpmulti(self, parametros):
        lista_origenes = []

        dir_destino = str(parametros[1]).replace("'", "")

        for dir_origen in str(parametros[0]).split(';'):
            lista_origenes.append(dir_origen.replace("'", ""))

        for dir in lista_origenes:
            fecha = os.path.sep + const.get_dia() + '__' + const.get_hora()
            destino = os.path.sep + dir.replace(os.path.sep, "_")
            destino = destino.replace(":", "")
            destino = dir_destino + fecha + destino
            print('Copiando ' + dir + ' en ' + destino)
            self.copy_directory(dir, destino)

    def copy_directory(self, origen=None, destino=None, ignora=None):
        try:
            shutil.copytree(origen, destino, ignore=ignora)
        except OSError as e:
            # si falla puede que sea archivo
            if e.errno == errno.ENOTDIR:
                shutil.copy(origen, destino, ignore=ignora)
            else:
                print('No se pudo copiar el directorio. Error %s' % e)

    def print_falta_parametros(self):
        print('Faltan parametros en la instruccion, revise el comando.')


def main():
    acciones = Ordenes()

    if len(sys.argv) > 1:
        #han pasado parametros al archivo
        orden = sys.argv[1]

        if orden == '--help':
            acciones.print_help()
        elif orden == '-cpone':
            if len(sys.argv) == 4:
                # acciones.cpone(sys.argv[2:], ignorar=('*.txt', '*.tmp'))
                acciones.cpone(sys.argv[2:], ignorar=None)
            else:
                acciones.print_falta_parametros()
        elif orden == '-cpmulti':
            if len(sys.argv) == 4:
                # acciones.cpone(sys.argv[2:], ignorar=('*.txt', '*.tmp'))
                acciones.cpmulti(sys.argv[2:])
            else:
                acciones.print_falta_parametros()
        elif orden == '-cpxml':
            pass
        elif orden == '-gen_xml_template':
            pass
    else:
        #sin parametros, poner ayuda
        acciones.print_help()

if __name__ == '__main__':
    main()


