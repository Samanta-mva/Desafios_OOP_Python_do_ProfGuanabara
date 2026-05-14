# Desafio 27 — Batalha RPG

## Descrição

Implemente a classe abstrata `Personagem` com atributos como `nome` e `vida`, além dos métodos concretos `atacar()` e `receber_dano()`. Crie as subclasses `Guerreiro` e `Mago`, cada uma com sua forma específica de `curar()`.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 27.
3. Execute o arquivo principal da solução.
4. Teste ataques e curas entre personagens diferentes.

```bash
python __main__.py
```

## Critérios de aceitação

- [x] Existe classe abstrata `Personagem` com atributos principais e método abstrato `curar()`.
- [x] O método `atacar(alvo, forca_max)` escolhe um golpe e gera dano aleatório.
- [x] O método `receber_dano(dano)` reduz corretamente a vida do alvo.
- [x] `Guerreiro` e `Mago` implementam formas diferentes de cura.
- [x] O sistema permite que um personagem ataque outro objeto personagem.
- [x] A execução mostra o golpe usado, o dano causado e a cura realizada.
- [x] O comportamento utiliza herança e abstração corretamente.

## Exemplo de código

```bash
 player1 = Guerreiro('Kratos', 2000)
    print()
    player2 = Mago('Merlin', 3000)

    player2.mostrar_ficha()
    player1.mostrar_ficha()

    print()
    player1.atacar_alvo(player2, 1000)
    print()
    player2.curar()

    print()
    player2.mostrar_ficha()
    player1.mostrar_ficha()
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./__main__.py)

---