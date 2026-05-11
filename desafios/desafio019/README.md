# Desafio 19 — Classe Livro e Controle de Páginas

## Descrição

Crie uma classe `Livro` que simule a passagem de páginas. Ao criar o objeto, informe o total de páginas do livro. O programa deve permitir avançar páginas, mas sem ultrapassar o fim do livro.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 19.
3. Execute o arquivo principal da solução.
4. Teste a navegação entre as páginas.

```bash
python main.py
```

## Critérios de aceitação

- [x] Existe uma classe `Livro`.
- [x] A classe recebe título e total de páginas.
- [x] O livro começa na página 1.
- [x] Existe um método para avançar páginas.
- [x] O programa impede ultrapassar o total de páginas.
- [x] A mensagem final informa quando o livro chega ao fim.
- [x] A saída mostra a página atual corretamente.

## Exemplo de código

```python
l1 = Livro("10 coisas que aprendi", 20)

l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./desafios/desafio019/desafio019.py)
