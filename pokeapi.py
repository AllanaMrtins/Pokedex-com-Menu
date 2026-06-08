import requests

class PokeAPIService:
    URL = "https://pokeapi.co/api/v2/pokemon/"

    @staticmethod
    def buscar(nome_id):
        resp = requests.get(
            f'{PokeAPIService.URL}{str(nome_id).lower()}'
        )

        if resp.status_code != 200:
            raise ValueError("Pokémon não encontrado.")
        
        return resp.json()