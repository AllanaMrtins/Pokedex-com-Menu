from pokemon import Pokemon
from pokeapi import PokeAPIService
from pokemons import BancoPokemons
from menu import Menu

class Pokedex:
    def consultar_pk(self):
        nome = input("\nNome ou ID do Pokémon: ")

        try:
            dados = PokeAPIService.buscar(nome)

            pokemon = Pokemon(
                dados["name"],
                dados["id"],
                dados["height"],
                dados["weight"],
                [t["type"]["name"]
                 for t in dados["types"]],
                dados["sprites"]["front_default"]
            )

            BancoPokemons.pokemons.append(pokemon)
            Menu.sucesso(f'{pokemon.nome.title()} cadastrado!')

        except Exception as erro:
            Menu.erro(str(erro))

    def listar(self):
        if not BancoPokemons.pokemons:
            Menu.erro("Nenhum Pokémon cadastrado.")
            return
        print("\nPOKÉMONS CADASTRADOS")

        for indice, pokemon in enumerate( BancoPokemons.pokemons, start=1):
            print(f'{indice} - ' f'{pokemon.nome.title()}')

    
    def exibir_dados(self):
        self.listar()

        indice = int(input("\nEscolha:")) - 1

        BancoPokemons.pokemons[indice].exibir_dados()


    def exibir_imagem(self):

        self.listar()

        indice = int(
            input("\nEscolha: ")) - 1

        BancoPokemons.pokemons[indice].mostrar_imagem()

    def quantidade(self):

        print( "\nTotal:",Pokemon.total_cad())