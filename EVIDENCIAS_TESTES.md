# Evidências dos Testes e Correções — PIT II

**Aluno:** Gabriel Felipe dos Santos Louback  
**RGM:** 33966117  
**Projeto:** Cupcake Express  
**Data dos testes:** 17/11/2026

## Participantes
- Thiago Roberto Mendes
- Amanda Caroline Freitas
- Rodrigo César Martins
- Isabela Cristina Rocha
- Marcelo Augusto Vieira

## 1. Mensagem de inclusão no carrinho
**Problema identificado:** a mensagem apresentada depois da inclusão do produto possuía pouco destaque visual.

**Correção aplicada:** foram criadas mensagens específicas de sucesso e erro, com maior contraste visual e texto mais claro.

**Evidência:** classes `msg ok` e `msg erro`, além da função `mensagem()`, adicionadas ao arquivo `index.html`.

## 2. Destaque da taxa de entrega
**Problema identificado:** a taxa fixa de R$ 8,00 aparecia no resumo, porém poderia ser mais facilmente identificada pelo usuário.

**Correção aplicada:** a linha da taxa de entrega recebeu destaque próprio no resumo do carrinho, mantendo separado o subtotal e o total.

**Evidência:** classe `taxa` e atualização do resumo do carrinho no `index.html`.

## 3. Orientação e validação do telefone
**Problema identificado:** o campo de telefone aceitava diferentes formatos sem orientação clara.

**Correção aplicada:** foi adicionado exemplo de preenchimento, indicação de DDD e validação de 10 ou 11 dígitos antes da finalização.

**Evidência:** placeholder, texto auxiliar e validação `telefoneLimpo` no formulário.

## 4. Responsividade dos controles do carrinho
**Problema identificado:** os botões de aumentar, diminuir e remover itens ficavam próximos em telas pequenas.

**Correção aplicada:** os controles passaram a quebrar linha quando necessário, receberam maior espaçamento e área de toque.

**Evidência:** ajustes nas classes `acoes` e `mini` dentro do media query para telas de até 600 pixels.

## 5. Resumo final com itens e quantidades
**Problema identificado:** a confirmação final apresentava dados do pedido, mas não listava os cupcakes escolhidos e suas quantidades.

**Correção aplicada:** o resumo final passou a exibir cada produto, quantidade, valor correspondente, taxa de entrega, total, cliente, endereço, pagamento e status.

**Evidência:** novo bloco `confirmacao-itens` gerado na finalização do pedido.

## Nova verificação
Após as correções, foram revistos:
- vitrine virtual;
- inclusão de produtos;
- alteração de quantidade;
- remoção de itens;
- subtotal;
- taxa de entrega;
- total;
- validação de nome, telefone, endereço e pagamento;
- comportamento em telas menores;
- resumo final do pedido.

O fluxo principal apresentou funcionamento satisfatório e maior clareza após os ajustes.

## Funcionalidades previstas para evolução futura
- login e cadastro de clientes;
- pagamento real;
- cálculo de entrega por endereço ou distância;
- rastreamento em tempo real;
- painel administrativo;
- histórico de pedidos;
- testes em maior variedade de dispositivos e navegadores.
