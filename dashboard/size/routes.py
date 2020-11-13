from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Size
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
import datetime

size = Blueprint('size',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')


# get all size 
@size.route('/size', methods=['POST', 'GET'])
@login_required
def get_size():
    SizeItems = db.session.query(Size).all()
    SituationItems = db.session.query(Situation).all()

    return render_template('size.html', SizeItems = SizeItems, SituationItems = SituationItems)


# insert new size 
@size.route('/size/new', methods=['POST', 'GET'])
@login_required
def add_size():
    if request.method == 'POST':
        NewSize = Size(Size = request.form['Size'], Enabled = request.form['Status'], CreatedAt = datetime.datetime.now())
        try :
            db.session.add(NewSize)
            db.session.commit()
            flash('Yes !! Size inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('size.get_size'))
        except Exception as err :
            flash('No !! ' + Sad + ' Size did not insert successfully . Please check insertion ', 'danger')
         
    return redirect(url_for('size.get_size'))


# edit Booking status
@size.route('/size/<int:IdSize>/edit', methods=['POST', 'GET'])
@login_required
def edit_size(IdSize):
    if request.method == 'POST':
        EditSize = db.session.query(Size).filter_by(IdSize = IdSize).one()
        EditSize.Size = request.form['Size']
        EditSize.Enabled = request.form['Status']
        try :
            db.session.add(EditSize)
            db.session.commit()
            flash('Yes !! Size is edited successfully '+ Happy , 'success')
            return redirect(url_for('size.get_size'))
        except Exception as err :
            flash('No !! ' + Sad + ' Size did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('size.get_size'))


# delete Size
@size.route('/size/<int:IdSize>/delete', methods=['POST', 'GET'])
@login_required
def delete_size(IdSize):
    if request.method == 'GET':
        DeleteSize = db.session.query(Size).filter_by(IdSize = IdSize).one()
        try :
            db.session.delete(DeleteSize)
            db.session.commit()
            flash('Yes !! Size is deleted successfully '+ Happy , 'success')
            return redirect(url_for('size.get_size'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
    return redirect(url_for('size.get_size'))
