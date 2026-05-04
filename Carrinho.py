class CarrinhoDeCompras:
    def __init__(self):
        self.itens = []
    

    def adicionar_produto(self, produto):
        self.itens.append(produto)
        print(f"🛒 {produto.nome} foi adicionado ao carrinho.")

    
    def exibir_resumo(self):
        print("\n --- RESUMO DO CARRINHO ---")
        total = 0

        for item in self.itens:
            item.exibir_detalhes()
            total += item.get_preco()
            
        print(f"TOTAL A PAGAR: R$ {total}")
        print("-"*45)