from PIL import Image
from io import BytesIO
import requests
import matplotlib.pyplot as plt

class Pokemon:
    __slots__ = (
        "_nome",
        "_id", 
        "_altura",
        "_peso",
        "_tipos",
        "_imagem"
    )

    qtd_pk = 0
    
    def __init__(self, nome, id_, altura, peso, tipos, imagem):
        self._nome = nome
        self._id = id_
        self._altura = altura
        self._peso = peso
        self._tipos = tipos
        self._imagem = imagem

        Pokemon.qtd_pk += 1


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def id(self):
        return self._id

    @property
    def altura(self):
        return self._altura

    @property
    def peso(self):
        return self._peso

    @property
    def tipos(self):
        return self._tipos

    @property
    def imagem(self):
        return self._imagem
    
    def exibir_dados(self):
        print("\n" + "=" * 40)
        print(f'Nome: {self.nome.title()}')
        print(f'ID: {self.id}')
        print(f'Altura: {self.altura}')
        print(f'Peso: {self.peso}')
        print(f'Tipos: `{", ".join(self.tipos)}')
        print("=" * 40)

    def mostrar_imagem(self):
        resp = requests.get(self.imagem)
        imagem = Image.open(
            BytesIO(resp.content)
        )

        plt.imshow(imagem)
        plt.axis("off")
        plt.title(self.nome.title())
        plt.show()

    @staticmethod
    def total_cad():
        return Pokemon.qtd_pk