from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Portion
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt

portion = Blueprint('portion',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')


# get  Booking status 
@portion.route('/portion', methods=['POST', 'GET'])
@login_required
def get_portion():
    PortionItems = db.session.query(Portion).all()
    # PendingBooking = db.session.query(Booking).join(Portion).filter(Portion.Portion == 'Pending').count()
    # NewBookings = db.session.query(Booking).join(Portion).filter(Portion.Portion == 'Pending').all()

    return render_template('portion.html', PortionItems = PortionItems)


# insert new Booking status 
@portion.route('/portion/new', methods=['POST', 'GET'])
@login_required
def add_portion():
    if request.method == 'POST':
        NewPortion = Portion(Portion = request.form['PortionName'])
        try :
            db.session.add(NewPortion)
            db.session.commit()
            flash('Yes !! Booking status inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('portion.get_portion'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking status did not insert successfully . Please check insertion ', 'danger')
         
    return redirect(url_for('portion.get_portion'))


# edit Booking status
@portion.route('/portion/<int:IdPortion>/edit', methods=['POST', 'GET'])
@login_required
def edit_portion(IdPortion):
    if request.method == 'POST':
        EditPortion = db.session.query(Portion).filter_by(IdPortion = IdPortion).one()
        EditPortion.Portion = request.form['PortionName']
        try :
            db.session.add(EditPortion)
            db.session.commit()
            flash('Yes !! Booing status is edited successfully '+ Happy , 'success')
            return redirect(url_for('portion.get_portion'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking status did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('portion.get_portion'))


# delete Booking status
@portion.route('/portion/<int:IdPortion>/delete', methods=['POST', 'GET'])
@login_required
def delete_portion(IdPortion):
    if request.method == 'GET':
        DeletePortion = db.session.query(Portion).filter_by(IdPortion = IdPortion).one()
        try :
            db.session.delete(DeletePortion)
            db.session.commit()
            flash('Yes !! Booking status is deleted successfully '+ Happy , 'success')
            return redirect(url_for('portion.get_portion'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
    return redirect(url_for('portion.get_portion'))
