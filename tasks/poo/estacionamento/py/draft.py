from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, hora_entrada: int, tipo : str):
        self.id = id
        self.hora_entrada: int = hora_entrada
        self.tipo = tipo

class Bike(Veiculo):
    def __init__(self, id : str):
        super().__init__(id, 0, "Bike")

class Moto(Veiculo):
    def __init__(self, id : str):
        super().__init__(id, 0, "Moto")

class Carro(Veiculo):
    def __init__(self, id : str):
        super().__init__(id, 0, "Carro")

class Estacionamento:
    def __init__(self):
        self.veiculos:list[Veiculo]

def main():
    estacionamento = Estacionamento()
    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break

        elif args[0] == "estacionar":
            tipo = args[1].lower()
            id = args[2]

        elif args[0] == "bike":
            res = estacionamento.estacionar(Bike(id))
            if res is not None:
                print(res)

        elif args[0] == "moto":
            res = estacionamento.estacionar(Moto(id))
            if res is not None:
                print(res)

        elif args[0] == "carro":
            res = estacionamento.estacionar(Carro(id))
            if res is not None:
                print(res)

        elif args[0] == "pagar":
            id = args[1]
            print(estacionamento.pagar(id))

        elif args[0] == "sair": 
            id = args{1}
            print(estacionamento.sair(id))

        elif args[0] == "tempo":
            tempo = float(args[1])
            estacionamento.passarTempo(tempo)

        elif args[0] == "show":
            print(estacionamento)
            
main()
        