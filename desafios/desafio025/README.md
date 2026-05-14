# Desafio 25 — Cálculo de Fretes

## Descrição

Implemente a classe abstrata `Transporte`, com atributo `distancia` e método abstrato `calcular_frete()`. Crie as subclasses `Moto`, `Caminhao` e `Drone`, cada uma com seu fator multiplicador e suas próprias regras de distância.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 25.
3. Execute o arquivo principal da solução.
4. Teste diferentes distâncias para cada tipo de transporte.

```bash
python __main__.py
```

## Critérios de aceitação

- [x] Existe classe abstrata `Transporte` com `distancia` e método `calcular_frete()`.
- [x] `Moto` calcula o frete com fator `0.5`, sem limite de distância.
- [x] `Caminhao` calcula o frete com fator `1.2`, aceitando apenas distâncias a partir de 50 km.
- [x] `Drone` calcula o frete com fator `9.5`, aceitando apenas distâncias de até 10 km.
- [x] Os fatores são definidos como atributos de classe.
- [x] O programa informa quando o frete não pode ser realizado por violar as regras de distância.
- [x] A execução mostra o veículo, a distância e o valor do frete calculado.

## Exmplo de código

```bash
dist = 10
entrega = Moto(dist)
print(f'Frete de {type(entrega).__name__} em {dist}km = {entrega.calc_frete()}')

entrega2 = Caminhao(dist)
print(f'Frete de {type(entrega2).__name__} em {dist}km = {entrega2.calc_frete()}')

entrega3 = Drone(dist)
print(f'Frete de {type(entrega3).__name__} em {dist}km = {entrega3.calc_frete()}')
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./__main__.py)

---
