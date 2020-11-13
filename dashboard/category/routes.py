from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Categories
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
import datetime

category = Blueprint('category',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

# get all category
@category.route('/category', methods=['POST','GET'])
@login_required
def get_category():
    CategoryItems = db.session.query(Categories).all()
    SituationItems = db.session.query(Situation).all()

    return render_template('category.html', CategoryItems = CategoryItems, SituationItems = SituationItems)

# add new Category
@category.route('/category/new', methods=['POST','GET'])
@login_required
def add_category():
    if request.method == 'POST':
        NewCategory = Categories(Category = request.form['CategoryName'], Enabled= request.form['Status'], CreatedAt = datetime.datetime.now())
        try :
            db.session.add(NewCategory)
            db.session.commit()
            flash('Yes !! Category inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('category.get_category'))
        except Exception as err :
            flash('No !! ' + Sad + ' Category did not insert successfully . Please check insertion ' , 'danger')
            print(err)
    return redirect(url_for('category.get_category'))

# edit category
@category.route('/category/<int:IdCategory>/edit', methods=['POST','GET'])
@login_required
def edit_category(IdCategory):
    if request.method == 'POST':
        EditCategory = db.session.query(Categories).filter_by(IdCategory = IdCategory).one()
        EditCategory.Category = request.form['CategoryName']
        EditCategory.Enabled = request.form['Status']
        try :
            db.session.add(EditCategory)
            db.session.commit()
            flash('Yes !! Category is edited successfully '+ Happy , 'success')
            return redirect(url_for('category.get_category'))
        except Exception as err :
            flash('No !! ' + Sad + ' Category did not edit successfully . Please check insertion ' , 'danger')
          
    return redirect(url_for('category.get_category'))

# delete Category
@category.route('/category/<int:IdCategory>/delete', methods=['POST','GET'])
@login_required
def delete_category(IdCategory):
    if request.method == 'GET':
        DeleteCategory = db.session.query(Categories).filter_by(IdCategory = IdCategory).one()
        try :
            db.session.delete(DeleteCategory)
            db.session.commit()
            flash('Yes !! category is deleted successfully '+ Happy , 'success')
            return redirect(url_for('category.get_category'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
            print(err)
    return redirect(url_for('category.get_category'))


# get all Category
@category.route('/category/api', methods=['POST', 'GET'])
def get_category_api():
    if request.method == "GET":
        CategoryApi = db.session.query(Category).filter(Category.Enabled == 1).all()
        print(CategoryApi)
        return jsonify(ProductType=[i.serialize for i in CategoryApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400
