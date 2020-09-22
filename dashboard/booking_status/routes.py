from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Booking, BookingStatus
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt

booking_status = Blueprint('booking_status',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')


# get  Booking status 
@booking_status.route('/booking_status', methods=['POST', 'GET'])
@login_required
def get_booking_status():
    BookingStatusItems = db.session.query(BookingStatus).all()
    # PendingBooking = db.session.query(Booking).join(BookingStatus).filter(BookingStatus.BookingStatus == 'Pending').count()
    # NewBookings = db.session.query(Booking).join(BookingStatus).filter(BookingStatus.BookingStatus == 'Pending').all()

    return render_template('booking_status.html', BookingStatusItems = BookingStatusItems)


# insert new Booking status 
@booking_status.route('/booking_status/new', methods=['POST', 'GET'])
@login_required
def add_booking_status():
    if request.method == 'POST':
        NewBookingStatus = BookingStatus(BookingStatus = request.form['BookingStatusName'])
        try :
            db.session.add(NewBookingStatus)
            db.session.commit()
            flash('Yes !! Booking status inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('booking_status.get_booking_status'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking status did not insert successfully . Please check insertion ', 'danger')
         
    return redirect(url_for('booking_status.get_booking_status'))


# edit Booking status
@booking_status.route('/booking_status/<int:IdBookingStatus>/edit', methods=['POST', 'GET'])
@login_required
def edit_booking_status(IdBookingStatus):
    if request.method == 'POST':
        EditBookingStatus = db.session.query(BookingStatus).filter_by(IdBookingStatus = IdBookingStatus).one()
        EditBookingStatus.BookingStatus = request.form['BookingStatusName']
        try :
            db.session.add(EditBookingStatus)
            db.session.commit()
            flash('Yes !! Booing status is edited successfully '+ Happy , 'success')
            return redirect(url_for('booking_status.get_booking_status'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking status did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('booking_status.get_booking_status'))


# delete Booking status
@booking_status.route('/booking_status/<int:IdBookingStatus>/delete', methods=['POST', 'GET'])
@login_required
def delete_booking_status(IdBookingStatus):
    if request.method == 'GET':
        DeleteBookingStatus = db.session.query(BookingStatus).filter_by(IdBookingStatus = IdBookingStatus).one()
        try :
            db.session.delete(DeleteBookingStatus)
            db.session.commit()
            flash('Yes !! Booking status is deleted successfully '+ Happy , 'success')
            return redirect(url_for('booking_status.get_booking_status'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
    return redirect(url_for('booking_status.get_booking_status'))
