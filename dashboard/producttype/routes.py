from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Categories, ProductType
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt

producttype = Blueprint('producttype',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

# get all category
@producttype.route('/product_type', methods=['POST','GET'])
@login_required
def get_producttype():
    ProductTypeItems = db.session.query(ProductType).all()
    SituationItems = db.session.query(Situation).all()

    return render_template('product_type.html', ProductTypeItems = ProductTypeItems, SituationItems = SituationItems)

# add new ProductType
@producttype.route('/product_type/new', methods=['POST','GET'])
@login_required
def add_producttype():
    if request.method == 'POST':
        NewProductType = ProductType(ProductType = request.form['ProductTypeName'], Enabled= request.form['Status'])
        try :
            db.session.add(NewProductType)
            db.session.commit()
            flash('Yes !! Product Type inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('producttype.get_producttype'))
        except Exception as err :
            flash('No !! ' + Sad + ' Produtc Type did not insert successfully . Please check insertion ' , 'danger')
            print(err)
    return redirect(url_for('producttype.get_producttype'))

# edit category
@producttype.route('/product_type/<int:IdProductType>/edit', methods=['POST','GET'])
@login_required
def edit_producttype(IdProductType):
    if request.method == 'POST':
        EditProductType = db.session.query(ProductType).filter_by(IdProductType = IdProductType).one()
        EditProductType.ProductType = request.form['ProductTypeName']
        EditProductType.Enabled = request.form['Status']
        try :
            db.session.add(EditProductType)
            db.session.commit()
            flash('Yes !! Product Type is edited successfully '+ Happy , 'success')
            return redirect(url_for('producttype.get_producttype'))
        except Exception as err :
            flash('No !! ' + Sad + ' Produtc Type did not edit successfully . Please check insertion ' , 'danger')
          
    return redirect(url_for('producttype.get_producttype'))

# delete Category
@producttype.route('/product_type/<int:IdProductType>/delete', methods=['POST','GET'])
@login_required
def delete_producttype(IdProductType):
    if request.method == 'GET':
        DeleteProductType = db.session.query(ProductType).filter_by(IdProductType = IdProductType).one()
        try :
            db.session.delete(DeleteProductType)
            db.session.commit()
            flash('Yes !! Product Type is deleted successfully '+ Happy , 'success')
            return redirect(url_for('producttype.get_producttype'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
            print(err)
    return redirect(url_for('producttype.get_producttype'))


# get all collection
@producttype.route('/producttype/api', methods=['POST', 'GET'])
def get_producttype_api():
    if request.method == "GET":
        ProductTypeApi = db.session.query(ProductType).filter(ProductType.Enabled == 1).all()
        print(ProductTypeApi)
        return jsonify(ProductType=[i.serialize for i in ProductTypeApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400
