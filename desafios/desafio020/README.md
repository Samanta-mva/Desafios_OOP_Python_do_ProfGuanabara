# Desafio 20 — Classe Gamer e Lista de Favoritos

## Descrição

Crie uma classe `Gamer` que permita cadastrar nome, nick e jogos favoritos. O atributo de jogos favoritos deve aceitar múltiplos valores. Crie também um método para mostrar a ficha do gamer.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 20.
3. Execute o arquivo principal da solução.
4. Confira se os jogos favoritos aparecem em ordem organizada.

```bash
python desafio020.py
```

## Critérios de aceitação

- [x] Existe uma classe `Gamer`.
- [x] A classe permite cadastrar nome e nick.
- [x] A classe aceita múltiplos jogos favoritos.
- [x] Existe um método para mostrar a ficha.
- [x] Os jogos aparecem listados de forma organizada.
- [x] O código principal instancia mais de um gamer.
- [x] A saída fica legível e bem formatada.

## Exemplo de código

```python
j1 = Gamer("Fabrício da Silva", "Detonator 2025")
j1.adicionar_favoritos("Mario Bros")
j1.adicionar_favoritos("Sonic")
j1.adicionar_favoritos("God of War")
j1.adicionar_favoritos("Fortnite")

j1.mostrar_ficha()
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./desafio020.py)
