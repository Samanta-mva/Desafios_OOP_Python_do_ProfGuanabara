# Desafio 23 — Classe Abstrata Polígono

## Descrição

Implemente uma classe abstrata `Poligono` com quantidade de lados e métodos abstratos para cálculo de perímetro e área. Crie subclasses `Quadrado` (com comprimento do lado) e `Circulo` (com raio) que herdam da classe abstrata e implementam os métodos.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 23.
3. Execute o arquivo principal da solução.
4. Teste com quadrado de lado 12 e círculo de raio 20.

```bash
python desafio023.py
```

## Critérios de aceitação

- [x] Existe classe abstrata `Poligono` com `quantidade_lados` e métodos abstratos `perimetro()` e `area()`.
- [x] Classe `Quadrado` herda de `Poligono` com `lado` e implementa perímetro (`4 * lado`) e área (`lado ** 2`).
- [x] Classe `Circulo` herda de `Poligono` com `raio` e implementa perímetro (`2 * pi * raio`) e área (`pi * raio ** 2`).
- [x] Testa quadrado de lado 12, com perímetro 48 e área 144.
- [x] Testa círculo de raio 20, com perímetro aproximado de 125.7 e área aproximada de 1256.
- [x] Usa `abc.ABC` e `@abstractmethod` em Python.
- [x] A execução mostra os cálculos corretos para ambos os casos.

## Exemplo de código

``` bash

```



## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./desafio023.py)

---