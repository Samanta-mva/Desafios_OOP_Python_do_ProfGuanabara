# Desafio 26 — Sistema de Funcionários

## Descrição

Crie a classe abstrata `Funcionario` com os atributos `nome` e `salario_bruto`, além do método abstrato `calcular_salario()` e do método concreto `analisar_salario()`. Implemente as subclasses `FuncionarioHorista` e `FuncionarioMensalista`, cada uma com sua lógica de cálculo.

## Instruções de setup

1. Clone ou baixe o repositório.
2. Acesse a pasta do desafio 26.
3. Execute o arquivo principal da solução.
4. Teste com um funcionário horista e um mensalista.

```bash
python __main__.py
```

## Critérios de aceitação

- [x] Existe classe abstrata `Funcionario` com `nome`, `salario_bruto` e método abstrato `calcular_salario()`.
- [x] Existe método concreto `analisar_salario()` para exibir o salário líquido e sua equivalência em salários mínimos.
- [x] `FuncionarioHorista` calcula o salário com base em valor da hora e horas trabalhadas.
- [x] `FuncionarioMensalista` calcula o salário com base no salário bruto mensal.
- [x] O desconto de INSS é aplicado corretamente.
- [x] O salário mínimo e o desconto são definidos como atributos de classe.
- [x] A execução mostra os dados calculados de forma legível.

## Exemplo de código

```bash
f1 = Horista( 'Paulo', 12, 200)
f1.analisar_salario()


f2 = Mensalista('Amanda', 9500)
f2.analisar_salario()
```

## Status

- [ ] Pendente
- [x] Feito

## Solução

[Ver solução](./__main__.py)

---