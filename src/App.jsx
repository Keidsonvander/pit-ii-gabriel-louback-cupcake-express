import React, { useMemo, useState } from "react";

const taxaEntrega = 8;
const produtos = [
  { id: 1, nome: "Chocolate Belga", preco: 9.9 },
  { id: 2, nome: "Morango Cream", preco: 9.9 },
  { id: 3, nome: "Limão Siciliano", preco: 9.9 },
  { id: 4, nome: "Red Velvet", preco: 11.5 }
];

export default function App() {
  const [carrinho, setCarrinho] = useState([]);
  const subtotal = useMemo(() => carrinho.reduce((s, i) => s + i.preco * i.quantidade, 0), [carrinho]);
  const total = carrinho.length ? subtotal + taxaEntrega : 0;

  function adicionar(produto) {
    setCarrinho(atual => {
      const existente = atual.find(i => i.id === produto.id);
      return existente
        ? atual.map(i => i.id === produto.id ? { ...i, quantidade: i.quantidade + 1 } : i)
        : [...atual, { ...produto, quantidade: 1 }];
    });
  }

  return (
    <main>
      <h1>Cupcake Express</h1>
      <p>MVP acadêmico desenvolvido a partir da PIT I.</p>
      <section>
        {produtos.map(p => (
          <article key={p.id}>
            <h2>{p.nome}</h2>
            <p>R$ {p.preco.toFixed(2)}</p>
            <button onClick={() => adicionar(p)}>Adicionar</button>
          </article>
        ))}
      </section>
      <section>
        <h2>Carrinho</h2>
        {carrinho.map(i => <p key={i.id}>{i.nome} x {i.quantidade}</p>)}
        <p>Subtotal: R$ {subtotal.toFixed(2)}</p>
        <p>Taxa de entrega: R$ {carrinho.length ? taxaEntrega.toFixed(2) : "0.00"}</p>
        <strong>Total: R$ {total.toFixed(2)}</strong>
      </section>
    </main>
  );
}
