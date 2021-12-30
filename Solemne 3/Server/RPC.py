import xmlrpc.server
from xmlrpc.server import SimpleXMLRPCServer

def agregar(a):
    return a *1000

def main():
    print("Servidor de Procesamientos iniciado ")
    server = SimpleXMLRPCServer(("192.168.18.3",9000))
    server.register_function(agregar)
    server.serve_forever()

if __name__ == "__main__":
    main()