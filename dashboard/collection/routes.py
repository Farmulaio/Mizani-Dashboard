from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Categories, Collection
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
import datetime


collection = Blueprint('collection',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

# get all collection
@collection.route('/collection', methods=['POST','GET'])
@login_required
def get_collection():
    CollectionItems = db.session.query(Collection).all()
    SituationItems = db.session.query(Situation).all()

    return render_template('collection.html', CollectionItems = CollectionItems, SituationItems = SituationItems)

# add new collection
@collection.route('/collection/new', methods=['POST','GET'])
@login_required
def add_collection():
    if request.method == 'POST':
        NewCollection = Collection(Collection = request.form['CollectionName'], Enabled= request.form['Status'], CreatedAt = datetime.datetime.now())
        try :
            db.session.add(NewCollection)
            db.session.commit()
            flash('Yes !! Collection inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('collection.get_collection'))
        except Exception as err :
            flash('No !! ' + Sad + ' Category did not insert successfully . Please check insertion ' , 'danger')
            print(err)
    return redirect(url_for('collection.get_collection'))

# edit collection
@collection.route('/collection/<int:IdCollection>/edit', methods=['POST','GET'])
@login_required
def edit_collection(IdCollection):
    if request.method == 'POST':
        EditCollection = db.session.query(Collection).filter_by(IdCollection = IdCollection).one()
        EditCollection.Collection = request.form['CollectionName']
        EditCollection.Enabled = request.form['Status']
        try :
            db.session.add(EditCollection)
            db.session.commit()
            flash('Yes !! Collection is edited successfully '+ Happy , 'success')
            return redirect(url_for('collection.get_collection'))
        except Exception as err :
            flash('No !! ' + Sad + ' Category did not edit successfully . Please check insertion ' , 'danger')
          
    return redirect(url_for('collection.get_collection'))

# delete collection
@collection.route('/collection/<int:IdCollection>/delete', methods=['POST','GET'])
@login_required
def delete_collection(IdCollection):
    if request.method == 'GET':
        DeleteCollection = db.session.query(Collection).filter_by(IdCollection = IdCollection).one()
        try :
            db.session.delete(DeleteCollection)
            db.session.commit()
            flash('Yes !! Collection is deleted successfully '+ Happy , 'success')
            return redirect(url_for('collection.get_collection'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
            print(err)
    return redirect(url_for('collection.get_collection'))


# get all collection
@collection.route('/collection/api', methods=['POST', 'GET'])
def get_collection_api():
    if request.method == "GET":
        CollectionApi = db.session.query(Collection).filter(Collection.Enabled == 1).all()
        print(CollectionApi)
        return jsonify(Collection=[i.serialize for i in CollectionApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400
