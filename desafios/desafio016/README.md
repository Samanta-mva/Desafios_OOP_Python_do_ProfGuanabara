# Desafio 16 — Classe Funcionário

## Descrição

Crie uma classe `Funcionario`, onde seja possível cadastrar nome, setor e cargo dos funcionários. Crie também um método que permita ao funcionário se apresentar.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 16.
3. Execute o arquivo principal da solução.
4. Verifique se a apresentação do funcionário está sendo exibida corretamente.

```bash
python main.py
```

## Critérios de aceitação

- [x] Existe uma classe `Funcionario`.
- [x] A classe permite cadastrar nome, setor e cargo.
- [x] Existe um método de apresentação.
- [x] A apresentação exibe nome, cargo, setor e empresa.
- [x] O código principal instancia pelo menos dois funcionários.
- [x] A saída está formatada de forma clara e legível.

## Exemplo de código

```python
c1 = Funcionario("Maria", "administração", "diretora")
c2 = Funcionario("Pedro", "TI", "programador")

c1.apresentar()
c2.apresentar()
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

desafios/desafio016/desafio016.py
