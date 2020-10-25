from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Categories
from flask import make_response, abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt
from sqlalchemy import desc
from sqlalchemy import and_
import random
import string, os
from datetime import datetime


product = Blueprint('product',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')

def random_string_generator(size=5,  chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# get Product
@product.route('/product', methods=['POST', 'GET'])
@login_required
def get_product():
    ProductsItems = db.session.query(Products).all()
    # HallItems = db.session.query(Hall).filter_by(Enabled = 1).all()
    # BookingStatusItems = db.session.query(BookingStatus).all()
    # PendingBooking = db.session.query(Bookings).join(BookingStatus).filter(BookingStatus.BookingStatus == 'Pending').count()
    # NewBookings = db.session.query(Bookings).join(BookingStatus).filter(BookingStatus.BookingStatus == 'Pending').all()
 
    return render_template('product.html', ProductsItems = ProductsItems)

# add new Product
@product.route('/product/new', methods=['POST', 'GET'])
@login_required
def add_product():
    if request.method == 'POST':
        NewBooking = Products(BookingNumber = "B"+random_string_generator(), OrganizationName = request.form['OrganizationName'], Poc = request.form['poc'], PhoneNumber = request.form['phonenumbers'], IdBookingStatus = request.form['BookingStatus'], Price = request.form['Price'], IdHall = request.form['Hall'], Bookingtime = request.form['Bookingtime'], IdUser = current_user.IdUser)
        try :
            # BookingItems = db.session.query(Booking).join(BookingStatus).filter(and_(Booking.IdHall == request.form['Hall'] , Booking.Bookingtime == request.form['Bookingtime'], Booking.IdBookingStatus == 2)).one()
            flash('Sorry !! ' + Sad + ' This Hall is Booked in this date . Please choose  another date ', 'danger')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            db.session.add(NewBooking)
            db.session.commit()
            flash('Yes !! Booking inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('product.get_product'))


        # try :
        #     db.session.add(NewBooking)
        #     db.session.commit()

         
        #     flash('Yes !! Booking inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
        #     return redirect(url_for('product.get_product))
        # except Exception as err :
        #     print(err)
        #     flash('No !! ' + Sad + ' Booking did not insert successfully . Please check insertion ', 'danger')
 
    return redirect(url_for('product.get_product'))

# edit Product
@product.route('/product/<int:IdProduct>/edit', methods=['POST', 'GET'])
@login_required
def edit_product(IdProduct):
    if request.method == 'POST':
        EditBooking = db.session.query(Products).filter_by(IdProduct = IdProduct).one()
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
            return redirect(url_for('product.get_product'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('product.get_product'))


# edit status Product
@product.route('/product/<int:IdProduct>/status', methods=['POST', 'GET'])
@login_required
def edit_status_product(IdProduct):
    if request.method == 'POST':
        EditBooking = db.session.query(Products).filter_by(IdBooking = IdBooking).one()
        EditBooking.IdBookingStatus = request.form['BookingStatusName']
       
        try :
            db.session.add(EditBooking)
            db.session.commit()
            flash('Yes !! Booking status is edited successfully '+ Happy , 'success')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            flash('No !! ' + Sad + ' Booking status did not edit successfully . Please check insertion ' , 'danger')
         
    return redirect(url_for('product.get_product'))


# delete Product
@product.route('/product/<int:IdProduct>/delete', methods=['POST', 'GET'])
@login_required
def delete_product(IdProduct):
    if request.method == 'GET':
        DeleteBooking = db.session.query(Products).filter_by(IdProduct = IdProduct).one()
        try :
            db.session.delete(DeleteBooking)
            db.session.commit()
            flash('Yes !! Booking is deleted successfully '+ Happy , 'success')
            return redirect(url_for('product.get_product'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
        
    return redirect(url_for('product.get_product'))
