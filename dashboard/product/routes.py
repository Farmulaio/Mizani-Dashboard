from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Categories, Size, Collection, Concerns, ProductType
from flask import make_response, abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
from sqlalchemy import desc
from sqlalchemy import and_
import random
import string, os
from dashboard import create_app
import datetime

product = Blueprint('product',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

def random_string_generator(size=5,  chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

app = create_app()

# get Product
@product.route('/product', methods=['POST', 'GET'])
@login_required
def get_product():
    ProductsItems = db.session.query(Products).all()
    SituationItems = db.session.query(Situation).all()
    CategoriesItems = db.session.query(Categories).all()
    CollectiomItems = db.session.query(Collection).all()
    ConcernsItems  = db.session.query(Concerns).all()
    ProductTypeItems = db.session.query(ProductType).all()
    SizeItems = db.session.query(Size).all()
 
    return render_template('product.html', ProductsItems = ProductsItems, SituationItems = SituationItems, CategoriesItems = CategoriesItems, SizeItems = SizeItems, CollectiomItems = CollectiomItems, ConcernsItems = ConcernsItems, ProductTypeItems = ProductTypeItems)

# add new Product
@product.route('/product/new', methods=['POST', 'GET'])
@login_required
def add_product():
    if request.method == 'POST':
        file = request.files['ImageUrl']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] , file.filename))
        NewProduct = Products(Name = request.form['ProductName'], Description = request.form['Description'], Enabled = request.form['Status'], Price = request.form['Price'], IdCategory = request.form['Category'], IdCollection = request.form['Collection'], IdProductType = request.form['ProductType'], IdConcerns = request.form['Concerns'], IdSize = request.form['Size'], IdUser = current_user.IdUser, ImageUrl = "https://mizani.farmula.io/static/img/" + file.filename, CreatedAt = datetime.datetime.now())
        try :
            db.session.add(NewProduct)
            db.session.commit()

            flash('Yes !! Product inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            print(err)
            flash('No !! ' + Sad + ' Prodcut did not insert successfully . Please check insertion ', 'danger')
 
    return redirect(url_for('product.get_product'))

# edit Product
@product.route('/product/<int:IdProduct>/edit', methods=['POST', 'GET'])
@login_required
def edit_product(IdProduct):
    if request.method == 'POST':
        file = request.files['ImageUrl']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'] , file.filename))
        
        EditProduct = db.session.query(Products).filter_by(IdProduct = IdProduct).one()
        EditProduct.Name = request.form['ProductName']
        EditProduct.Description  = request.form['Description']
        EditProduct.IdCategory = request.form['Category']
        EditProduct.IdCollection = request.form['Collection']
        EditProduct.IdProductType = request.form['ProductType']
        EditProduct.IdConcerns = request.form['Concerns']
        EditProduct.Enabled  = request.form['Status']
        EditProduct.Price  = request.form['Price']
        EditProduct.IdSize  = request.form['Size']
        EditProduct.ImageUrl  =  "https://mizani.farmula.io/static/img/" + file.filename
        try :
            db.session.add(EditProduct)
            db.session.commit()
            flash('Yes !! Product is edited successfully '+ Happy , 'success')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            flash('No !! ' + Sad + ' Product did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('product.get_product'))


# edit status Product
@product.route('/product/<int:IdProduct>/status', methods=['POST', 'GET'])
@login_required
def edit_status_product(IdProduct):
    if request.method == 'POST':
        EditProduct = db.session.query(Products).filter_by(IdProduct = IdProduct).one()
        EditProduct.Enabled = request.form['Status']
       
        try :
            db.session.add(EditProduct)
            db.session.commit()
            flash('Yes !! Product status is edited successfully '+ Happy , 'success')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            flash('No !! ' + Sad + ' Product status did not edit successfully . Please check insertion ' , 'danger')
         
    return redirect(url_for('product.get_product'))


# delete Product
@product.route('/product/<int:IdProduct>/delete', methods=['POST', 'GET'])
@login_required
def delete_product(IdProduct):
    if request.method == 'GET':
        DeleteProduct = db.session.query(Products).filter_by(IdProduct = IdProduct).one()
        try :
            db.session.delete(DeleteProduct)
            db.session.commit()
            flash('Yes !! Product is deleted successfully '+ Happy , 'success')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
        
    return redirect(url_for('product.get_product'))


# get all products
@product.route('/product/api', methods=['POST', 'GET'])
def get_product_api():
    if request.method == "GET":
        ProductsApi = db.session.query(Products).filter(Products.Enabled == 1).all()
        print(ProductsApi)
        return jsonify(Products=[i.serialize for i in ProductsApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400


# get all products by Category
@product.route('/product/<int:IdCategory>/category', methods=['POST', 'GET'])
def get_product_by_category_api(IdCategory):
    if request.method == "GET":
        ProductsApi = db.session.query(Products).filter(Products.IdCategory == IdCategory).all()
        print(ProductsApi)
        return jsonify(Products=[i.serialize for i in ProductsApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400


# get all products by collection
@product.route('/product/<int:IdCollection>/collection', methods=['POST', 'GET'])
def get_product_by_collection_api(IdCollection):
    if request.method == "GET":
        ProductsApi = db.session.query(Products).filter(Products.IdCollection == IdCollection).all()
        print(ProductsApi)
        return jsonify(Products=[i.serialize for i in ProductsApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400



# get all products by concerns
@product.route('/product/<int:IdConcerns>/concerns', methods=['POST', 'GET'])
def get_product_by_concerns_api(IdConcerns):
    if request.method == "GET":
        ProductsApi = db.session.query(Products).filter(Products.IdConcerns == IdConcerns).all()
        print(ProductsApi)
        return jsonify(Products=[i.serialize for i in ProductsApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400



# get all products by product type
@product.route('/product/<int:IdProductType>/ProductType', methods=['POST', 'GET'])
def get_product_by_product_type_api(IdProductType):
    if request.method == "GET":
        ProductsApi = db.session.query(Products).filter(Products.IdProductType == IdProductType).all()
        print(ProductsApi)
        return jsonify(Products=[i.serialize for i in ProductsApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400