from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Booking, BookingStatus, Hall
from flask import make_response, abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
from sqlalchemy import desc
from sqlalchemy import and_
import random
import string, os
from datetime import datetime


booking = Blueprint('booking',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

def random_string_generator(size=5,  chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# get Bookings
@booking.route('/booking', methods=['POST', 'GET'])
@login_required
def get_booking():
    BookingItems = db.session.query(Booking).all()
    HallItems = db.session.query(Hall).filter_by(Enabled = 1).all()
    BookingStatusItems = db.session.query(BookingStatus).all()
    # PendingBooking = db.session.query(Bookings).join(BookingStatus).filter(BookingStatus.BookingStatus == 'Pending').count()
    # NewBookings = db.session.query(Bookings).join(BookingStatus).filter(BookingStatus.BookingStatus == 'Pending').all()
 
    return render_template('booking.html', BookingItems = BookingItems, HallItems = HallItems, BookingStatusItems = BookingStatusItems)

# add new Booking
@booking.route('/booking/new', methods=['POST', 'GET'])
@login_required
def add_booking():
    if request.method == 'POST':
        NewBooking = Booking(BookingNumber = "B"+random_string_generator(), OrganizationName = request.form['OrganizationName'], Poc = request.form['poc'], PhoneNumber = request.form['phonenumbers'], IdBookingStatus = request.form['BookingStatus'], Price = request.form['Price'], IdHall = request.form['Hall'], Bookingtime = request.form['Bookingtime'], IdUser = current_user.IdUser)
        try :
            BookingItems = db.session.query(Booking).join(BookingStatus).filter(and_(Booking.IdHall == request.form['Hall'] , Booking.Bookingtime == request.form['Bookingtime'], Booking.IdBookingStatus == 2)).one()
            flash('Sorry !! ' + Sad + ' This Hall is Booked in this date . Please choose  another date ', 'danger')
            return redirect(url_for('booking.get_booking'))
        except Exception as err :
            db.session.add(NewBooking)
            db.session.commit()
            flash('Yes !! Booking inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('booking.get_booking'))


        # try :
        #     db.session.add(NewBooking)
        #     db.session.commit()

         
        #     flash('Yes !! Booking inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
        #     return redirect(url_for('booking.get_booking'))
        # except Exception as err :
        #     print(err)
        #     flash('No !! ' + Sad + ' Booking did not insert successfully . Please check insertion ', 'danger')
 
    return redirect(url_for('booking.get_booking'))

# edit Booking
@booking.route('/booking/<int:IdBooking>/edit', methods=['POST', 'GET'])
@login_required
def edit_booking(IdBooking):
    if request.method == 'POST':
        EditBooking = db.session.query(Booking).filter_by(IdBooking = IdBooking).one()
        EditBooking.OrganizationName = request.form['OrganizationName']
        EditBooking.Poc  = request.form['poc']
        EditBooking.PhoneNumber = request.form['phonenumbers']
        EditBooking.IdBookingStatus = request.form['BookingStatus']
        EditBooking.IdHall  = request.form['Hall']
        EditBooking.Price  = request.form['Price']
        EditBooking.Bookingtime  = request.form['Bookingtime']
        try :
            db.session.add(EditBooking)
            db.session.commit()
            flash('Yes !! Booking is edited successfully '+ Happy , 'success')
            return redirect(url_for('booking.get_booking'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('booking.get_booking'))


# edit status Booking
@booking.route('/booking/<int:IdBooking>/status', methods=['POST', 'GET'])
@login_required
def edit_status_booking(IdBooking):
    if request.method == 'POST':
        EditBooking = db.session.query(Booking).filter_by(IdBooking = IdBooking).one()
        EditBooking.IdBookingStatus = request.form['BookingStatusName']
       
        try :
            db.session.add(EditBooking)
            db.session.commit()
            flash('Yes !! Booking status is edited successfully '+ Happy , 'success')
            return redirect(url_for('booking.get_booking'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking status did not edit successfully . Please check insertion ' , 'danger')
         
    return redirect(url_for('booking.get_booking'))


# delete Booking
@booking.route('/booking/<int:IdBooking>/delete', methods=['POST', 'GET'])
@login_required
def delete_booking(IdBooking):
    if request.method == 'GET':
        DeleteBooking = db.session.query(Booking).filter_by(IdBooking = IdBooking).one()
        try :
            db.session.delete(DeleteBooking)
            db.session.commit()
            flash('Yes !! Booking is deleted successfully '+ Happy , 'success')
            return redirect(url_for('booking.get_booking'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
        
    return redirect(url_for('booking.get_booking'))
