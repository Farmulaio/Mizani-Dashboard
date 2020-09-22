from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Booking, BookingStatus, Hall
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt

halls = Blueprint('halls',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

# get all Halls
@halls.route('/halls', methods=['POST','GET'])
@login_required
def get_halls():
    HallItems = db.session.query(Hall).all()
    SituationItems = db.session.query(Situation).all()

    return render_template('halls.html', HallItems = HallItems, SituationItems = SituationItems)

# add new Hall
@halls.route('/halls/new', methods=['POST','GET'])
@login_required
def add_halls():
    if request.method == 'POST':
        NewHall = Hall(Name = request.form['HallName'], Enabled= request.form['Status'])
        try :
            db.session.add(NewHall)
            db.session.commit()
            flash('Yes !! Hall inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('halls.get_halls'))
        except Exception as err :
            flash('No !! ' + Sad + ' Hall did not insert successfully . Please check insertion ' , 'danger')

    return redirect(url_for('halls.get_halls'))

# edit halls
@halls.route('/halls/<int:IdHall>/edit', methods=['POST','GET'])
@login_required
def edit_halls(IdHall):
    if request.method == 'POST':
        EditHall = db.session.query(Hall).filter_by(IdHall = IdHall).one()
        EditHall.Name = request.form['HallName']
        EditHall.Enabled = request.form['Status']
        try :
            db.session.add(EditHall)
            db.session.commit()
            flash('Yes !! Hall is edited successfully '+ Happy , 'success')
            return redirect(url_for('halls.get_halls'))
        except Exception as err :
            flash('No !! ' + Sad + ' Hall did not edit successfully . Please check insertion ' , 'danger')
          
    return redirect(url_for('halls.get_halls'))

# delete Hall
@halls.route('/halls/<int:IdHall>/delete', methods=['POST','GET'])
@login_required
def delete_halls(IdHall):
    if request.method == 'GET':
        DeleteHall = db.session.query(Hall).filter_by(IdHall = IdHall).one()
        try :
            db.session.delete(DeleteHall)
            db.session.commit()
            flash('Yes !! Hall is deleted successfully '+ Happy , 'success')
            return redirect(url_for('halls.get_halls'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
 
    return redirect(url_for('halls.get_halls'))
