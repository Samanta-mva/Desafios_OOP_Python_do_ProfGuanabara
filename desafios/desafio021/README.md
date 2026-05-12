# Desafio 21 — Classe Caneta e Comportamento

## Descrição

Crie uma classe `Caneta` que simule o funcionamento de uma caneta colorida. A caneta deve ter cor, estado de tampa e comportamento de escrita, podendo escrever apenas quando estiver destampada.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 21.
3. Execute o arquivo principal da solução.
4. Teste o comportamento de escrever, tampar e destampar.

OBS.: Para este desafio tenho duas soluções uma utilizando IF e outra solução utilizando CASE (que aprendi com a solução do prof. Gustavo Guanabara).

## Com IF
```bash
python desafio021.py
```

## Com CASE
```bash
python desafio021-B.py
```

## Critérios de aceitação

- [x] Existe uma classe `Caneta`.
- [x] A classe aceita uma cor.
- [x] A caneta pode ser tampada e destampada.
- [x] A caneta só escreve quando estiver destampada.
- [x] O método de quebra de linha funciona corretamente.
- [x] O código principal instancia canetas de cores diferentes.
- [x] A saída mostra o comportamento conforme o estado da caneta.

## Exemplo de código

```python
c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c1.escrever("Olá, tudo bem?")

c2.destampar()
c2.escrever("Olá, gafanhoto")

c3.destampar()
c3.escrever("Vamos exercitar")
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução IF](./desafio021.py)

[Ver solução CASE](./desafio021-B.py)
