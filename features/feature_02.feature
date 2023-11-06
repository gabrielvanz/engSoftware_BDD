# language: pt

Funcionalidade: Buscar produto na página inicial Magazine Luiza

Esquema do Cenário: Validar busca de um produto
    Dado que esteja na página inicial da Magazine Luiza 
    Quando buscar pelo produto '<produto>'
    E selecionar o primeiro produto
    Então deverá ser direcionado para a página do produto

    Exemplos:
    | produto                                             |
    | Geladeira/Refrigerador Esmaltec Degelo Manual       |
    # | Smart TV 32” HD LED Semp R6500 Wi-Fi - 3 HDMI 1 USB |
    # | Apple iPhone 13 128GB Estelar Tela 6,1” 12MP        |