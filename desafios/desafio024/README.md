# Desafio 24 — Cafeteira Orientada a Objetos

## Descrição

Crie a classe abstrata `BebidaQuente` com os métodos concretos `preparar()` e `ferver_agua()`, além dos métodos abstratos `misturar()` e `servir()`. Implemente as subclasses `Cafe`, `Cha` e `Leite`, cada uma com sua própria forma de mistura e serviço.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 24.
3. Execute o arquivo principal da solução.
4. Teste a preparação de café, chá e leite quente.

```bash
python __main__.py
```

## Critérios de aceitação

- [x] Existe a classe abstrata `BebidaQuente`.
- [x] O método `ferver_agua()` funciona de forma concreta e comum para todas as bebidas.
- [x] O método `preparar()` executa o fluxo completo: ferver, misturar e servir.
- [x] `Cafe`, `Cha` e `Leite` implementam corretamente `misturar()` e `servir()`.
- [x] A solução utiliza polimorfismo, sem depender de `if` para decidir o comportamento.
- [x] A execução mostra o passo a passo completo de cada bebida.

## Execute o código

```bash
bebida = Cafe()
bebida.preparar()

bebida2 = Cha()
bebida2.preparar()

bebida3 = Leite()
bebida3.preparar()
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./__main__.py)

---