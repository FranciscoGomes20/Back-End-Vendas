from vendas import db, ma

class Cliente(db.Model):
    __tablename__ = 'Client'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.Integer, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    
    def init(self, name, telephone, email):
       self.name = name
       self.telephone = telephone
       self.email = email
        
    def json(self):
        return {'name':self.name, 'telephone':self.telephone, 'email':self.email}
    
class ClienteSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "telephone", "email")

client_schema  = ClienteSchema()
clients_schema = ClienteSchema(many=True)
    
class Vendedor(db.Model):
    __tablename__ = 'Seller'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    
    def init(self, name, email):
        self.name = name
        self.email = email
        
    def json(self):
        return {'name':self.name, 'email':self.email}

class VendedorSchema(ma.Schema):
    class Meta:
        fields = ("id", "name", "email")

seller_schema  = VendedorSchema()
sellers_schema = VendedorSchema(many=True)
    
class Pagamento(db.Model):
    __tablename__ = 'Payment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    form_of_payment = db.Column(db.String(90), unique=True, nullable=False)
    
    def init(self, form_of_payment):
	    self.form_of_payment = form_of_payment
        
    def json(self):
        return {'form_of_payment':self.form_of_payment}

class PagamentoSchema(ma.Schema):
    class Meta:
        fields = ("id", "form_of_payment")

payment_schema  = PagamentoSchema()
payments_schema = PagamentoSchema(many=True)

class Venda(db.Model):
    __tablename__ = 'Sale'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('Client.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('Seller.id'), nullable=False)
    payment_id = db.Column(db.Integer, db.ForeignKey('Payment.id'), nullable=False)
    
    def init(self, amount, date, client_id, seller_id, payment_id):
        self.amount = amount
        self.date = date
        self.client_id = client_id
        self.seller_id = seller_id
        self.payment_id = payment_id
        
    def json(self):
        return {'amount':self.amount, 'date':self.date, 'client_id':self.client_id, 'seller_id':self.seller_id, 'payment_id':self.payment_id}

class VendaSchema(ma.Schema):
    class Meta:
        fields = ("id", "amount", "date", "client_id", "seller_id", "payment_id")

sale_schema  = VendaSchema()
sales_schema = VendaSchema(many=True)
    
class Vendas_de_Produtos(db.Model):
    __tablename__ = 'Product_Sales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('Sale.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'), nullable=False)

    def init(self, sale_id, product_id):
        self.sale_id = sale_id
        self.product_id = product_id

    def json(self):
        return {'sale_id':self.sale_id, 'product_id':self.product_id}

class Vendas_de_ProdutosSchema(ma.Schema):
    class Meta:
        fields = ("id", "sale_id", "product_id")

product_Sale_schema  = Vendas_de_ProdutosSchema()
product_Sales_schema = Vendas_de_ProdutosSchema(many=True)

class Categoria(db.Model):
    __tablename__ = "Category"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category = db.Column(db.String(90), unique=True, nullable=False)

    def init(self, category):
        self.category = category

    def json(self):
        return {'category':self.category}
    
class CategoriaSchema(ma.Schema):
    class Meta:
        fields = ("id", "category")

category_schema  = CategoriaSchema()
categorys_schema = CategoriaSchema(many=True)

class Fornecedor(db.Model):
    __tablename__ = 'Supplier'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cnpj = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    
    def init(self, cnpj, name):
        self.cnpj = cnpj
        self.name = name
    
    def json(self):
        return {'cnpj':self.cnpj, 'name':self.name}

class FornecedorSchema(ma.Schema):
    class Meta:
        fields = ("id", "cnpj", "name")

supplier_schema  = FornecedorSchema()
suppliers_schema = FornecedorSchema(many=True)

class Produto(db.Model):
    __tablename__ = 'Product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    qtd_stock = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('Category.id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('Supplier.id'), nullable=False)
    
    def init(self, description, price, qtd_stock, category_id, supplier_id):
        self.description = description
        self.price = price
        self.qtd_stock = qtd_stock
        self.category_id = category_id
        self.supplier_id = supplier_id
    
    def json(self):
        return {'description':self.description, 'price':self.price, 'qtd_stock':self.qtd_stock, 'category_id':self.category_id, 'supplier_id':self.supplier_id}

class ProdutoSchema(ma.Schema):
    class Meta:
        fields = ("id", "description", "price", "qtd_stock", "category_id", "supplier_id")

product_schema  = ProdutoSchema()
products_schema = ProdutoSchema(many=True)
