from flask import jsonify, request
from vendas import app, db
from datetime import date
from .models import Produto, products_schema, product_schema, Cliente, client_schema, clients_schema, Categoria, category_schema, categorys_schema, Fornecedor, supplier_schema, suppliers_schema
from .models import Vendedor, seller_schema, sellers_schema, Pagamento, payment_schema, payments_schema, Venda, sale_schema, sales_schema, Vendas_de_Produtos, product_Sale_schema, product_Sales_schema

# -------------- GET ID ----------------#
@app.route('/produtos/<int:id>', methods=['GET'])
def pegarProduto(id):
    get_product = Produto.query.get(id)
    return jsonify(product_schema.dump(get_product))

@app.route('/clientes/<int:id>', methods=['GET'])
def pegarClientes(id):
    get_client = Cliente.query.get(id)
    return jsonify(client_schema.dump(get_client))

@app.route('/categorias/<int:id>', methods=['GET'])
def pegarCategoria(id):
    get_categoria = Categoria.query.get(id)
    return jsonify(category_schema.dump(get_categoria))

@app.route('/fornecedores/<int:id>', methods=['GET'])
def pegarFornecedor(id):
    get_fornecedor = Fornecedor.query.get(id)
    return jsonify(supplier_schema.dump(get_fornecedor))

@app.route('/vendedores/<int:id>', methods=['GET'])
def pegarVendedor(id):
    get_vendedor = Vendedor.query.get(id)
    return jsonify(seller_schema.dump(get_vendedor))

@app.route('/pagamentos/<int:id>', methods=['GET'])
def pegarPagamento(id):
    get_pagamento = Pagamento.query.get(id)
    return jsonify(payment_schema.dump(get_pagamento))

@app.route('/vendas/<int:id>', methods=['GET'])
def pegarVenda(id):
    get_venda = Venda.query.get(id)
    return jsonify(sale_schema.dump(get_venda))

@app.route('/vendas_de_produtos/<int:id>', methods=['GET'])
def pegarVendas_de_Produtos(id):
    get_vendas_de_produtos = Vendas_de_Produtos.query.get(id)
    return jsonify(product_Sale_schema.dump(get_vendas_de_produtos))

# -------------- GET ALL ----------------#
@app.route('/produtos', methods=['GET'])
def listaProduto():
    all_products = Produto.query.all()
    return jsonify(products_schema.dump(all_products))

@app.route('/clientes', methods=['GET'])
def listaClientes():
    all_client = Cliente.query.all()
    return jsonify(clients_schema.dump(all_client))

@app.route('/categorias', methods=['GET'])
def listaCategoria():
    all_categoria = Categoria.query.all()
    return jsonify(categorys_schema.dump(all_categoria))

@app.route('/fornecedores', methods=['GET'])
def listaFornecedor():
    all_fornecedor = Fornecedor.query.all()
    return jsonify(suppliers_schema.dump(all_fornecedor))

@app.route('/vendedores', methods=['GET'])
def listaVendedor():
    all_vendedor = Vendedor.query.all()
    return jsonify(sellers_schema.dump(all_vendedor))

@app.route('/pagamentos', methods=['GET'])
def listaPagamento():
    all_pagamento = Pagamento.query.all()
    return jsonify(payments_schema.dump(all_pagamento))

@app.route('/vendas', methods=['GET'])
def listaVenda():
    all_venda = Venda.query.all()
    return jsonify(sales_schema.dump(all_venda))

@app.route('/vendas_de_produtos', methods=['GET'])
def listaVendas_de_Produtos():
    all_vendas_de_produtos = Vendas_de_Produtos.query.all()
    return jsonify(product_Sales_schema.dump(all_vendas_de_produtos))

# -------------- POST ----------------#
@app.route('/produto', methods=['POST'])
def incluirProduto():
    produto = request.get_json()
    
    existing_product = Produto.query.filter_by(description=produto["description"]).first()

    if produto["description"] == "" or produto["price"] == "" or produto["qtd_stock"] == "" or produto["category_id"] == "" or produto["supplier_id"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(produto["description"]) != str or type(produto["price"]) != int or type(produto["qtd_stock"]) != int or type(produto["category_id"]) != int or type(produto["supplier_id"]) != int:
        return jsonify(errors="Os campos devem ser do tipo: description(str), price(float/int) e qtd_stock(int) e category_id(int) e supplier_id(int)!")
    
    if existing_product is not None:
        return jsonify(errors="Esse nome já existe!")
        
    produto_add = Produto(description=produto["description"], price=produto["price"], qtd_stock=produto["qtd_stock"], category_id=produto["category_id"], supplier_id=produto["supplier_id"])
    db.session.add(produto_add)
    db.session.commit()

    return jsonify(produto), 201

@app.route('/cliente', methods=['POST'])
def incluirCliente():
    cliente = request.get_json()
    
    existing_client = Cliente.query.filter_by(email=cliente["email"]).first()

    if cliente["name"] == "" or cliente["telephone"] == "" or cliente["email"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(cliente["name"]) != str or type(cliente["telephone"]) != int or type(cliente["email"]) != str:
        return jsonify(errors="Os campos devem ser do tipo: name(str), telephone(int) e email(str)!")
    
    if existing_client is not None:
        return jsonify(errors="Esse email já existe!")
        
    cliente_add = Cliente(name=cliente["name"], telephone=cliente["telephone"], email=cliente["email"])
    db.session.add(cliente_add)
    db.session.commit()

    return jsonify(cliente), 201

@app.route('/categoria', methods=['POST'])
def incluirCategoria():
    categoria = request.get_json()
    
    existing_category = Categoria.query.filter_by(category=categoria["category"]).first()

    if categoria["category"] == "":
        return jsonify(errors="O campos não pode estar vazio!")
    
    if type(categoria["category"]) != str:
        return jsonify(errors="O campo deve ser do tipo: category(str)!")
    
    if existing_category is not None:
        return jsonify(errors="Essa categoria já existe!")
        
    categoria_add = Categoria(category=categoria["category"])
    db.session.add(categoria_add)
    db.session.commit()

    return jsonify(categoria), 201

@app.route('/fornecedor', methods=['POST'])
def incluirFornecedor():
    fornecedor = request.get_json()
    
    existing_fornecedor = Fornecedor.query.filter_by(cnpj=fornecedor["cnpj"]).first()

    if fornecedor["name"] == "" or fornecedor["cnpj"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(fornecedor["name"]) != str or type(fornecedor["cnpj"]) != int:
        return jsonify(errors="O campo deve ser do tipo: name(str) e cnpj(int)!")
    
    if existing_fornecedor is not None:
        return jsonify(errors="Esse fornecedor já existe!")
        
    fornecedor_add = Fornecedor(cnpj=fornecedor["cnpj"], name=fornecedor["name"])
    db.session.add(fornecedor_add)
    db.session.commit()

    return jsonify(fornecedor), 201

@app.route('/vendedor', methods=['POST'])
def incluirVendedor():
    vendedor = request.get_json()
    
    existing_vendedor = Vendedor.query.filter_by(email=vendedor["email"]).first()

    if vendedor["name"] == "" or vendedor["email"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(vendedor["name"]) != str or type(vendedor["email"]) != str:
        return jsonify(errors="O campo deve ser do tipo: name(str) e email(str)!")
    
    if existing_vendedor is not None:
        return jsonify(errors="Esse email já existe!")
        
    vendedor_add = Vendedor(email=vendedor["email"], name=vendedor["name"])
    db.session.add(vendedor_add)
    db.session.commit()

    return jsonify(vendedor), 201

@app.route('/pagamento', methods=['POST'])
def incluirPagamento():
    pagamento = request.get_json()
    
    existing_pagamento = Pagamento.query.filter_by(form_of_payment=pagamento["form_of_payment"]).first()

    if pagamento["form_of_payment"] == "":
        return jsonify(errors="O campo não pode estar vazio!")
    
    if type(pagamento["form_of_payment"]) != str:
        return jsonify(errors="O campo deve ser do tipo: form_of_payment(str)!")
    
    if existing_pagamento is not None:
        return jsonify(errors="Essa forma de pagamento já existe!")
        
    pagamento_add = Pagamento(form_of_payment=pagamento["form_of_payment"])
    db.session.add(pagamento_add)
    db.session.commit()

    return jsonify(pagamento), 201

@app.route('/venda', methods=['POST'])
def incluirVenda():
    venda = request.get_json()

    if venda["amount"] == "" or venda["date"] == "" or venda["client_id"] == "" or venda["seller_id"] == "" or venda["payment_id"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(venda["amount"]) != int or type(venda["date"]) != str or type(venda["client_id"]) != int or type(venda["seller_id"]) != int or type(venda["payment_id"]) != int:
        return jsonify(errors="O campo deve ser do tipo inteiro!")
    
    venda["date"] = date.fromisoformat(venda["date"])
        
    venda_add = Venda(amount=venda["amount"], date=venda["date"], client_id=venda["client_id"], seller_id=venda["seller_id"], payment_id=venda["payment_id"])
    db.session.add(venda_add)
    db.session.commit()

    return jsonify(venda), 201

@app.route('/vendas_de_produto', methods=['POST'])
def incluirVendasProdutos():
    vendas_de_produto = request.get_json()

    if vendas_de_produto["sale_id"] == "" or vendas_de_produto["product_id"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(vendas_de_produto["sale_id"]) != int or type(vendas_de_produto["product_id"]) != int:
        return jsonify(errors="Os campos devem ser do tipo inteiro!")
        
    vendas_de_produto_add = Vendas_de_Produtos(sale_id=vendas_de_produto["sale_id"], product_id=vendas_de_produto["product_id"])
    db.session.add(vendas_de_produto_add)
    db.session.commit()

    return jsonify(vendas_de_produto), 201

# -------------- PUT ----------------#
@app.route('/produto/<int:id>', methods=['PUT'])
def editarProduto(id):
    produto = request.get_json()

    produto_editado = Produto.query.get(id)

    if produto["description"] == "" or produto["price"] == "" or produto["qtd_stock"] == "" or produto["category_id"] == "" or produto["supplier_id"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(produto["description"]) != str or type(produto["price"]) != int or type(produto["qtd_stock"]) != int or type(produto["category_id"]) != int or type(produto["supplier_id"]) != int:
        return jsonify(errors="Os campos devem ser do tipo: description(str), price(float/int) e qtd_stock(int) e category_id(int) e supplier_id(int)!")

    produto_editado.id = id
    produto_editado.description = produto["description"]
    produto_editado.price = produto["price"]
    produto_editado.qtd_stock = produto["qtd_stock"]
    produto_editado.category_id = produto["category_id"]
    produto_editado.supplier_id = produto["supplier_id"]

    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=produto)

@app.route('/cliente/<int:id>', methods=['PUT'])
def editarCliente(id):
    cliente = request.get_json()
    
    cliente_editado = Cliente.query.get(id)

    if cliente["name"] == "" or cliente["telephone"] == "" or cliente["email"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(cliente["name"]) != str or type(cliente["telephone"]) != int or type(cliente["email"]) != str:
        return jsonify(errors="Os campos devem ser do tipo: name(str), telephone(int) e email(str)!")
        
    cliente_editado.id = id
    cliente_editado.name = cliente["name"]
    cliente_editado.telephone = cliente["telephone"]
    cliente_editado.email = cliente["email"]

    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=cliente)

@app.route('/categoria/<int:id>', methods=['PUT'])
def editarCategoria(id):
    categoria = request.get_json()
    
    categoria_editado = Categoria.query.get(id)

    if categoria["category"] == "":
        return jsonify(errors="O campos não pode estar vazio!")
    
    if type(categoria["category"]) != str:
        return jsonify(errors="O campo deve ser do tipo: category(str)!")
        
    categoria_editado.id = id
    categoria_editado.category = categoria["category"]

    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=categoria)

@app.route('/fornecedor/<int:id>', methods=['PUT'])
def editarFornecedor(id):
    fornecedor = request.get_json()
    
    fornecedor_editado = Fornecedor.query.get(id)

    if fornecedor["name"] == "" or fornecedor["cnpj"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(fornecedor["name"]) != str or type(fornecedor["cnpj"]) != int:
        return jsonify(errors="O campo deve ser do tipo: name(str) e cnpj(int)!")
        
    fornecedor_editado.id = id
    fornecedor_editado.cnpj = fornecedor["cnpj"]
    fornecedor_editado.name = fornecedor["name"]

    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=fornecedor)

@app.route('/vendedor/<int:id>', methods=['PUT'])
def editarVendedor(id):
    vendedor = request.get_json()

    vendedor_editado = Vendedor.query.get(id)

    if vendedor["name"] == "" or vendedor["email"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(vendedor["name"]) != str or type(vendedor["email"]) != str:
        return jsonify(errors="O campo deve ser do tipo: name(str) e email(str)!")
    
    vendedor_editado.id = id
    vendedor_editado.email = vendedor["email"]
    vendedor_editado.name = vendedor["name"]
    
    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=vendedor)

@app.route('/pagamento/<int:id>', methods=['PUT'])
def editarPagamento(id):
    pagamento = request.get_json()
    
    pagamento_editado = Pagamento.query.get(id)

    if pagamento["form_of_payment"] == "":
        return jsonify(errors="O campo não pode estar vazio!")
    
    if type(pagamento["form_of_payment"]) != str:
        return jsonify(errors="O campo deve ser do tipo: form_of_payment(str)!")
    
    pagamento_editado.id = id
    pagamento_editado.form_of_payment = pagamento["form_of_payment"]
    
    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=pagamento)

@app.route('/venda/<int:id>', methods=['PUT'])
def editarVenda(id):
    venda = request.get_json()

    venda_editado = Venda.query.get(id)

    if venda["amount"] == "" or venda["date"] == "" or venda["client_id"] == "" or venda["seller_id"] == "" or venda["payment_id"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(venda["amount"]) != int or type(venda["date"]) != str or type(venda["client_id"]) != int or type(venda["seller_id"]) != int or type(venda["payment_id"]) != int:
        return jsonify(errors="O campo deve ser do tipo inteiro!")
    
    venda["date"] = date.fromisoformat(venda["date"])
        
    venda_editado.id = id
    venda_editado.amount = venda["amount"]
    venda_editado.date = venda["date"]
    venda_editado.client_id = venda["client_id"]
    venda_editado.seller_id = venda["seller_id"]
    venda_editado.payment_id = venda["payment_id"]
    
    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=venda)

@app.route('/vendas_de_produto/<int:id>', methods=['PUT'])
def editarVendasProdutos(id):
    vendas_de_produto = request.get_json()

    vendas_de_produto_editado = Vendas_de_Produtos.query.get(id)

    if vendas_de_produto["sale_id"] == "" or vendas_de_produto["product_id"] == "":
        return jsonify(errors="Os campos não podem estar vazios!")
    
    if type(vendas_de_produto["sale_id"]) != int or type(vendas_de_produto["product_id"]) != int:
        return jsonify(errors="Os campos devem ser do tipo inteiro!")
        
    vendas_de_produto_editado.id = id
    vendas_de_produto_editado.sale_id = vendas_de_produto["sale_id"]
    vendas_de_produto_editado.product_id = vendas_de_produto["product_id"]
    
    db.session.commit()
    return jsonify(mensagem="UPDATE SUCESSFUL",dados=vendas_de_produto)

# -------------- DELERTE ----------------#
@app.route('/produto/<int:id>', methods=['DELETE'])
def excluirProduto(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify(mensagem="DELETED PRODUCT!")

@app.route('/cliente/<int:id>', methods=['DELETE'])
def excluirCliente(id):
    cliente = Cliente.query.get(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify(mensagem="DELETED CLIENT!")

@app.route('/Vendedor/<int:id>', methods=['DELETE'])
def excluirVendedor(id):
    vendedor = Vendedor.query.get(id)
    db.session.delete(vendedor)
    db.session.commit()
    return jsonify(mensagem="DELETED SELLER!")
