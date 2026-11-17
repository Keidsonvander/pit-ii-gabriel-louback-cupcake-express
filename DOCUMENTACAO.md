# Documentação do Projeto — PIT II

## Identificação
**Aluno:** Gabriel Felipe dos Santos Louback  
**RGM:** 33966117  
**Projeto:** Cupcake Express — Sistema Web para Loja Virtual de Cupcakes Gourmet

## 1. Continuidade da PIT I
A PIT II dá continuidade à solução desenvolvida na PIT I para uma loja de cupcakes gourmet.

A proposta utiliza uma abordagem de MVP, com foco em uma solução simples, responsiva e de rápida implantação.

## 2. Objetivo
Manter e aprimorar a solução funcional planejada na PIT I, permitindo que o cliente visualize produtos, monte o carrinho, preencha dados de entrega, escolha uma forma de pagamento simulada e visualize o resumo final.

## 3. Personas
### Cliente
Necessita comprar cupcakes de forma rápida pelo celular ou computador.

### Administrador da loja
Necessita organizar pedidos e manter os produtos disponíveis.

### Atendente/entregador
Necessita consultar os dados do pedido, o endereço e as informações necessárias para a entrega.

## 4. Histórias de usuário principais
- visualizar a vitrine de cupcakes;
- identificar produtos e categorias;
- adicionar produtos ao carrinho;
- alterar quantidades e remover itens;
- visualizar o total;
- preencher nome, telefone e endereço;
- escolher pagamento simulado;
- receber resumo do pedido;
- utilizar o sistema em celular e computador;
- receber mensagens de validação.

## 5. Backlog priorizado
1. Criar tela inicial e vitrine.
2. Cadastrar produtos.
3. Implementar inclusão no carrinho.
4. Alterar quantidade e remover itens.
5. Calcular subtotal, taxa de entrega e total.
6. Criar formulário do cliente e endereço.
7. Criar seleção de pagamento simulado.
8. Gerar resumo do pedido.
9. Criar layout responsivo.
10. Implementar mensagens de validação.
11. Testar fluxo completo.
12. Preparar documentação, GitHub e publicação.

## 6. Requisitos Funcionais
**RF01:** Visualizar cupcakes com nome, descrição e preço.  
**RF02:** Adicionar produtos ao carrinho.  
**RF03:** Alterar quantidades e remover itens.  
**RF04:** Calcular subtotal, taxa de entrega e total.  
**RF05:** Preencher nome, telefone e endereço.  
**RF06:** Selecionar forma de pagamento simulada.  
**RF07:** Exibir resumo do pedido finalizado.

## 7. Requisitos Não Funcionais
**RNF01:** A aplicação deve ser responsiva.  
**RNF02:** O MVP não depende de backend obrigatório.  
**RNF03:** A interface deve ser simples e clara.  
**RNF04:** O carregamento deve ser leve para uso em redes móveis.

## 8. Regras de negócio
**RN01:** Cobrar taxa fixa de entrega de R$ 8,00 quando houver itens no carrinho.  
**RN02:** O pedido só pode ser finalizado se houver pelo menos um item no carrinho.  
**RN03:** Nome, telefone e endereço são obrigatórios.  
**RN04:** O total deve considerar produtos, quantidades e taxa de entrega.  
**RN05:** O pagamento é simulado e pode ser Pix, cartão ou dinheiro.

## 9. Critérios de aceitação
- produto incluído deve aparecer no carrinho com preço e quantidade;
- ausência de endereço deve gerar mensagem de validação;
- pedido válido deve gerar resumo final;
- alteração de quantidade deve recalcular o total.

## 10. Mapa navegacional
Home/Vitrine → Detalhes do produto → Carrinho → Dados de entrega → Pagamento simulado → Resumo do pedido

## 11. Modelo conceitual
Principais entidades:
- Cliente;
- Produto;
- Carrinho;
- ItemPedido;
- Pedido;
- Pagamento.

## 12. Arquitetura da PIT II
A PIT II mantém o front-end em React/Vite e acrescenta um back-end em Python com Flask e banco de dados SQLite para registro e consulta de pedidos. A taxa fixa de entrega de R$ 8,00 também é aplicada no back-end.

## 13. Publicação
A versão demonstrativa do front-end é publicada no GitHub Pages. O código do back-end Flask e do banco SQLite permanece disponível no repositório como parte da implementação acadêmica, pois o GitHub Pages executa apenas conteúdo estático.

## 14. Controle de versão
As melhorias, testes e correções serão registrados neste repositório por meio do histórico de commits.
