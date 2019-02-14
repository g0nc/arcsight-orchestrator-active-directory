from pypsexec.client import Client
import os
import time
import sys
funcao = sys.argv[1]
usuario = sys.argv[2]

if funcao == "ativar":
    c = Client("192.168.0.1", username="domain\\arcsight", password="arcsight@M31", encrypt=False, port=445)
    c.connect()

    try:
            c.create_service()
            stdout = c.run_executable("cmd.exe", arguments="/c net user "+str(usuario)+" /ACTIVE:YES /domain")
            #saida = stdout[0].decode("utf-8")
            #print(str(saida))
            for item in stdout:
                    print(item)
            sys.exit()
    except KeyboardInterrupt:
            c.cleanup()
            c.remove_service()
            c.disconnect()
elif funcao == "desativar":

    c = Client("192.168.0.1", username="domain\\arcsight", password="arcsight@M31", encrypt=False, port=445)
    c.connect()

    try:
            c.create_service()
            stdout = c.run_executable("cmd.exe", arguments="/c net user "+str(usuario)+" /ACTIVE:NO /domain")
            #saida = stdout[0].decode("utf-8")
            #print(str(saida))
            for item in stdout:
                    print(item)
            sys.exit()
    except KeyboardInterrupt:
            c.cleanup()
            c.remove_service()
            c.disconnect()
else:
    print("Opcao invalida")
