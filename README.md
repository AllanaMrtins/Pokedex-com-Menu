<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pokédex com API Pokémon</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
            color: #333;
            background-color: #f8f9fa;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            border-bottom: 2px solid #ddd;
            padding-bottom: 10px;
        }
        h2 {
            color: #34495e;
            margin-top: 30px;
            border-left: 4px solid #34495e;
            padding-left: 10px;
        }
        ul {
            padding-left: 20px;
        }
        code {
            background-color: #f1f1f1;
            padding: 2px 5px;
            border-radius: 4px;
        }
        pre {
            background-color: #f4f4f4;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
        }
        .info p {
            margin: 5px 0;
        }
        footer {
            text-align: center;
            margin-top: 40px;
            color: #666;
            font-size: 14px;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>Pokédex com API Pokémon</h1>
    <h2>Informações Acadêmicas</h2>
    <div class="info">
        <p><strong>Universidade:</strong> Universidade Federal do Piauí (UFPI)</p>
        <p><strong>Curso:</strong> Bacharelado em Sistemas de Informação</p>
        <p><strong>Disciplina:</strong> Programação Orientada a Objetos</p>
        <p><strong>Professor:</strong>Thiago José Barbosa Lima</p>
        <p><strong>Aluna:</strong> Allana Camily de Sousa Martins</p>
    </div>
    <h2>Descrição</h2>
    <p>
        Este projeto consiste no desenvolvimento de uma Pokédex em Python utilizando
        Programação Orientada a Objetos e integração com a PokéAPI.
        O sistema permite consultar Pokémons por nome ou ID, armazená-los durante
        a execução do programa e exibir suas informações e imagens oficiais.
    </p>
    <h2>Funcionalidades</h2>
    <ul>
        <li>Consultar Pokémon por nome ou ID</li>
        <li>Cadastrar Pokémons</li>
        <li>Listar Pokémons cadastrados</li>
        <li>Exibir dados detalhados dos Pokémons</li>
        <li>Exibir imagem oficial do Pokémon</li>
        <li>Mostrar quantidade de Pokémons cadastrados</li>
    </ul>
    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li>Python 3</li>
        <li>Requests</li>
        <li>Pillow (PIL)</li>
        <li>Matplotlib</li>
        <li>Rich</li>
        <li>PokéAPI</li>
    </ul>
    <h2>Estrutura do Projeto</h2>
    <pre>
pokedex/
│
├── main.py
├── menu.py
├── pokedex.py
├── pokemon.py
├── pokeapi.py
└── requirements.txt
    </pre>
    <h2>Instalação</h2>
    <pre>
pip install requests pillow matplotlib rich
    </pre>
    <h2>Execução</h2>
    <pre>
python main.py
    </pre>
    <h2>API Utilizada</h2>
    <p>PokéAPI:</p>
    <pre>
https://pokeapi.co/api/v2/pokemon/pikachu
https://pokeapi.co/api/v2/pokemon/ditto
https://pokeapi.co/api/v2/pokemon/charizard
    </pre>
    <h2>Conceitos Aplicados</h2>
    <ul>
        <li>Classes e Objetos</li>
        <li>Encapsulamento</li>
        <li>Atributos Privados</li>
        <li>@property</li>
        <li>@staticmethod</li>
        <li>__slots__</li>
        <li>Consumo de API REST</li>
        <li>Modularização</li>
    </ul>
    <h2>Objetivo</h2>
    <p>
        Aplicar os conceitos estudados na disciplina de Programação Orientada a Objetos
        por meio do desenvolvimento de uma aplicação integrada a uma API REST real.
    </p>
    <footer>
        Projeto desenvolvido para fins acadêmicos – UFPI
    </footer>

</div>

</body>
</html>