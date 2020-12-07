# from dashboard import app, db, bcrypt
# from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup
# from dashboard.models import Crop, Market, Quantity, Role, Users, Farmer, Business, Price, Pricechecksession, Pricemechsession, Situation, Orders, OrderStatus, Prediction, Feedback, Conditions
# from flask_login import login_user, current_user, logout_user, login_required
# import random, string
# from datetime import datetime

# response = ""
# Happy = Markup('<span>&#127881;</span>')
# Sad = Markup('<span>&#128557;</span>')
# Sassy = Markup('<span>&#128540;</span>')


# def random_string_generator(size=5,  chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for _ in range(size))

# # # index page
# # @app.route('/', methods=['POST','GET'])
# # def login():
# #     if current_user.is_authenticated :
# #         return redirect(url_for('index'))
# #     if request.method == 'POST':
# #         User = db.session.query(Users).filter_by(Email = request.form['Email']).first()
# #         if User and bcrypt.check_password_hash(User.Pasword, request.form['Pasword']):
# #             login_user(User)
# #             next_page = request.args.get('next')
# #             return redirect(next_page) if next_page else redirect(url_for('index'))
# #         else :
# #             return render_template('login.html')
# #     return render_template('login.html')

    
# # # index page
# # @app.route('/index', methods=['POST','GET'])
# # @login_required
# # def index():
# #     PriceCheckerNumb = db.session.query(Pricechecksession).count()
# #     FarmerNumber = db.session.query(Farmer).count()
# #     BusinessNumber = db.session.query(Business).count()
# #     OrderNumber = db.session.query(Orders).count()
# #     FeedbackNumber = db.session.query(Feedback).count()

# #     return render_template('index.html', PriceCheckerNumb = PriceCheckerNumb, FarmerNumber = FarmerNumber, BusinessNumber = BusinessNumber, OrderNumber = OrderNumber, FeedbackNumber = FeedbackNumber)


# # # get all crops
# # @app.route('/crop', methods=['POST','GET'])
# # @login_required
# # def get_crop():
# #     CropItems = db.session.query(Crop).all()
# #     SituationItems = db.session.query(Situation).all()
# #     return render_template('crop.html', CropItems = CropItems, SituationItems = SituationItems)

# # # add new crop
# # @app.route('/crop/new', methods=['POST','GET'])
# # @login_required
# # def add_crop():
# #     if request.method =='POST' :
# #         NewCrop = Crop(Name = request.form['CropName'], Enabled = request.form['Status'])
# #         try :
# #             db.session.add(NewCrop)
# #             db.session.commit()
# #             flash('Yes !! Crop inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_crop'))
# #         except:
# #             flash('No !! ' + Sad + ' Crop did not insert successfully . Please check insertion ', 'danger')
 
# #     return redirect(url_for('get_crop'))


# # # edit crop
# # @app.route('/crop/<int:IdCrop>/edit', methods=['POST','GET'])
# # @login_required
# # def edit_crop(IdCrop):
# #     if request.method == 'POST' :
# #         EditCrop = db.session.query(Crop).filter_by(IdCrop = IdCrop).one()
# #         EditCrop.Name = request.form['CropName']
# #         EditCrop.Enabled = request.form['Status']
# #         try :
# #             db.session.add(EditCrop)
# #             db.session.commit()
# #             flash('Yes !! Crop is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_crop'))
# #         except :
# #             flash('No !! ' + Sad + ' Crop did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_crop'))


# # # delete crop
# # @app.route('/crop/<int:IdCrop>/delete', methods=['POST','GET'])
# # @login_required
# # def delete_crop(IdCrop):
# #     if request.method == 'GET':
# #         DeleteCrop = db.session.query(Crop).filter_by(IdCrop = IdCrop).one()
# #         try :
# #             db.session.delete(DeleteCrop)
# #             db.session.commit()
# #             flash('Yes !! Crop is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_crop'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')

# #     return redirect(url_for('get_crop'))

# # # get all markets
# # @app.route('/market', methods=['POST','GET'])
# # @login_required
# # def get_market():
# #     MarketItems = db.session.query(Market).all()
# #     SituationItems = db.session.query(Situation).all()
# #     return render_template('market.html', MarketItems = MarketItems, SituationItems = SituationItems)

# # # add new market
# # @app.route('/market/new', methods=['POST','GET'])
# # @login_required
# # def add_market():
# #     if request.method == 'POST':
# #         NewMarket = Market(Name = request.form['MarketName'], Enabled= request.form['Status'])
# #         try :
# #             db.session.add(NewMarket)
# #             db.session.commit()
# #             flash('Yes !! Market inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_market'))
# #         except :
# #             flash('No !! ' + Sad + ' Market did not insert successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_market'))

# # # edit market
# # @app.route('/market/<int:IdMarket>/edit', methods=['POST','GET'])
# # @login_required
# # def edit_market(IdMarket):
# #     if request.method == 'POST':
# #         EditMarket = db.session.query(Market).filter_by(IdMarket = IdMarket).one()
# #         EditMarket.Name = request.form['MarketName']
# #         EditMarket.Enabled = request.form['Status']
# #         try :
# #             db.session.add(EditMarket)
# #             db.session.commit()
# #             flash('Yes !! Market is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_market'))
# #         except :
# #             flash('No !! ' + Sad + ' Market did not edit successfully . Please check insertion ' , 'danger')
          
# #     return redirect(url_for('get_market'))

# # # delete market
# # @app.route('/market/<int:IdMarket>/delete', methods=['POST','GET'])
# # @login_required
# # def delete_market(IdMarket):
# #     if request.method == 'GET':
# #         DeleteMarket = db.session.query(Market).filter_by(IdMarket = IdMarket).one()
# #         try :
# #             db.session.delete(DeleteMarket)
# #             db.session.commit()
# #             flash('Yes !! Market is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_market'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
 
# #     return redirect(url_for('get_market'))


# # # get all quantity
# # @app.route('/quantity', methods=['POST','GET'])
# # @login_required
# # def get_quantity():
# #     QuantityItems = db.session.query(Quantity).all()
# #     SituationItems = db.session.query(Situation).all()
# #     return render_template('quantity.html', QuantityItems = QuantityItems, SituationItems = SituationItems)

# # # add new Quantity
# # @app.route('/quantity/new', methods=['POST', 'GET'])
# # @login_required
# # def add_quantity():
# #     if request.method == 'POST' :
# #         NewQuantity = Quantity(Qty = request.form['QuantityName'], Enabled = request.form['Status'])
# #         try :
# #             db.session.add(NewQuantity)
# #             db.session.commit()
# #             flash('Yes !! Quantity inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_quantity'))
# #         except :
# #             flash('No !! ' + Sad + ' Quantity did not insert successfully . Please check insertion ' , 'danger')
          
# #     return redirect(url_for('get_quantity'))

# # # edit Quantity
# # @app.route('/quantity/<int:IdQuantity>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_quantity(IdQuantity):
# #     if request.method == 'POST' :
# #         EditQuantity = db.session.query(Quantity).filter_by(IdQty = IdQuantity).one()
# #         EditQuantity.Qty = request.form['QuantityName']
# #         EditQuantity.Enabled = request.form['Status']
# #         try :
# #             db.session.add(EditQuantity)
# #             db.session.commit()
# #             flash('Yes !! Quantity is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_quantity'))
# #         except :
# #             flash('No !! ' + Sad + ' Quantity did not edit successfully . Please check insertion ' , 'danger')
          
# #     return redirect(url_for('get_quantity'))

# # # delete Quantity
# # @app.route('/quantity/<int:IdQuantity>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_quantity(IdQuantity):
# #     if request.method == 'GET' :
# #         DeleteQuantity = db.session.query(Quantity).filter_by(IdQty = IdQuantity).one()
# #         try :
# #             db.session.delete(DeleteQuantity)
# #             db.session.commit()
# #             flash('Yes !! Quantity is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_quantity'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')

# #     return redirect(url_for('get_quantity'))


# # # get all roles
# # @app.route('/role', methods=['POST', 'GET'])
# # @login_required
# # def get_role():
# #     RoleItems = db.session.query(Role).all()
# #     return render_template('role.html', RoleItems = RoleItems)


# # # add new role
# # @app.route('/role/new', methods=['POST', 'GET'])
# # @login_required
# # def add_role():
# #     if request.method == 'POST':
# #         NewRole = Role(Role = request.form['RoleName'])
# #         try :
# #             db.session.add(NewRole)
# #             db.session.commit()
# #             flash('Yes !! Role inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_role'))
# #         except :
# #             flash('No !! ' + Sad + ' Role did not insert successfully . Please check insertion ', 'danger')

# #     return redirect(url_for('get_role'))

# # # edit role
# # @app.route('/role/<int:IdRole>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_role(IdRole):
# #     if request.method == 'POST':
# #         EditRole = db.session.query(Role).filter_by(IdRole = IdRole).one()
# #         EditRole.Role = request.form['RoleName']
# #         try :
# #             db.session.add(EditRole)
# #             db.session.commit()
# #             flash('Yes !! Role is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_role'))
# #         except :
# #             flash('No !! ' + Sad + ' Role did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_role'))

# # # delete role
# # @app.route('/role/<int:IdRole>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_role(IdRole):
# #     if request.method == 'GET':
# #         DeleteRole = db.session.query(Role).filter_by(IdRole = IdRole).one()
# #         try :
# #             db.session.delete(DeleteRole)
# #             db.session.commit()
# #             flash('Yes !! Role is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_role'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
          
# #     return redirect(url_for('get_role'))

# # # get all users
# # @app.route('/users', methods=['POST','GET'])
# # @login_required
# # def get_users():
# #     User = db.session.query(Users).all()
# #     RoleItems = db.session.query(Role).all()
# #     SituationItems = db.session.query(Situation).all()
# #     return render_template("users.html", User = User , RoleItems = RoleItems, SituationItems = SituationItems)

# # # add new user
# # @app.route('/users/new', methods=['POST', 'GET'])
# # @login_required
# # def add_users():
# #     if request.method == 'POST' :
# #         NewUser = Users(IdRole = request.form['Role'], FirstName = request.form['FirstName'], LastName = request.form['LastName'], Email = request.form['Email'], PhoneNumber = request.form['PhoneNumber'], Address = request.form['Address'], Pasword = bcrypt.generate_password_hash(request.form['Pasword']).decode('utf-8'), Enabled = request.form['Status'])
# #         try :
# #             db.session.add(NewUser)
# #             db.session.commit()
# #             flash('Yes !! User inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_users'))
# #         except :
# #             flash('No !! ' + Sad + ' User did not insert successfully . Please check insertion ', 'danger')
           
# #         return redirect(url_for('get_users'))

# # # edit User
# # @app.route('/users/<int:IdUser>/edit', methods=['POST','GET'])
# # @login_required
# # def edit_user(IdUser):
# #     if request.method == 'POST':
# #         EditUser = db.session.query(Users).filter_by(IdUser = IdUser).one()
# #         EditUser.IdRole = request.form['Role']
# #         EditUser.FirstName = request.form['FirstName']
# #         EditUser.LastName = request.form['LastName']
# #         EditUser.Email = Email = request.form['Email']
# #         EditUser.PhoneNumber = request.form['PhoneNumber']
# #         EditUser.Address =  request.form['Address']
# #         # EditUser.Pasword = bcrypt.generate_password_hash(request.form['Pasword']).decode('utf-8')
# #         EditUser.Enabled = request.form['Status']
# #         try :
# #             db.session.add(EditUser)
# #             db.session.commit()
# #             flash('Yes !! User is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_users'))
# #         except :
# #             flash('No !! ' + Sad + ' User did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_users'))

# # # delete user
# # @app.route('/users/<int:IdUser>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_user(IdUser):
# #     if request.method == 'GET':
# #         DeleteUser  = db.session.query(Users).filter_by(IdUser = IdUser).one()
# #         try :
# #             db.session.delete(DeleteUser)
# #             db.session.commit()
# #             flash('Yes !! User is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_users'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')

# #     return redirect(url_for('get_users'))

# # # edit Passwod User
# # @app.route('/users_password/<int:IdUser>/edit', methods=['POST','GET'])
# # @login_required
# # def edit_password_user(IdUser):
# #     if request.method == 'POST':
# #         EditUser = db.session.query(Users).filter_by(IdUser = IdUser).one()
# #         EditUser.Pasword = bcrypt.generate_password_hash(request.form['Pasword']).decode('utf-8')
# #         try :
# #             db.session.add(EditUser)
# #             db.session.commit()
# #             flash('Yes !! Password is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_users'))
# #         except :
# #             flash('No !! ' + Sad + ' Password did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_users'))

# # # get all farmers
# # @app.route('/farmer', methods=['POST','GET'])
# # @login_required
# # def get_farmer():
# #     FarmerItems = db.session.query(Farmer).all()
# #     CropItems = db.session.query(Crop).filter_by(Enabled = 1).all()

# #     return render_template('farmers.html', FarmerItems = FarmerItems, CropItems = CropItems)

# # # add new farmer
# # @app.route('/farmer/new', methods=['POST','GET'])
# # @login_required
# # def add_farmer():
# #     if request.method == 'POST':
# #         NewFarmer = Farmer(FirstName = request.form['FirstName'], LastName = request.form['LastName'], PhoneNumber = request.form['PhoneNumber'], Address = request.form['Address'], IdCrop = request.form['Crop'], Harvestime = request.form['Harvestime'])
# #         try :
# #             db.session.add(NewFarmer)
# #             db.session.commit()
# #             flash('Yes !! Farmer inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_farmer'))
# #         except :
# #             flash('No !! ' + Sad + ' Farmer did not insert successfully . Please check insertion ', 'danger')
          
# #     return redirect(url_for('get_farmer'))


# # # edit farmer
# # @app.route('/farmer/<int:Idfarmer>/edit', methods=['POST','GET'])
# # @login_required
# # def edit_farmer(Idfarmer):
# #     if request.method == 'POST' :
# #         EditFarmer = db.session.query(Farmer).filter_by(Idfarmer = Idfarmer).one()
# #         EditFarmer.FirstName = request.form['FirstName']
# #         EditFarmer.LastName = request.form['LastName']
# #         EditFarmer.PhoneNumber = request.form['PhoneNumber']
# #         EditFarmer.Address = request.form['Address']
# #         EditFarmer.IdCrop = request.form['Crop']
# #         EditFarmer.Harvestime = request.form['Harvestime']
# #         try :
# #             db.session.add(EditFarmer)
# #             db.session.commit()
# #             flash('Yes !! Farmer is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_farmer'))
# #         except :
# #             flash('No !! ' + Sad + ' Farmer did not edit successfully . Please check insertion ' , 'danger')
          
# #     return redirect(url_for('get_farmer'))


# # # delete farmer
# # @app.route('/farmer/<int:Idfarmer>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_farmer(Idfarmer):
# #     if request.method == 'GET' :
# #         DeleteFarmer = db.session.query(Farmer).filter_by(Idfarmer = Idfarmer).one()
# #         try :
# #             db.session.delete(DeleteFarmer)
# #             db.session.commit()
# #             flash('Yes !! Farmer is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_farmer'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
# #     return redirect(url_for('get_farmer'))

# # # get all business
# # @app.route('/business', methods=['POST', 'GET'])
# # @login_required
# # def get_business():
# #     BusinessItems = db.session.query(Business).all()
# #     return render_template('business.html', BusinessItems = BusinessItems)

# # # add Business
# # @app.route('/business/new', methods=['POST', 'GET'])
# # @login_required
# # def add_business():
# #     if request.method == 'POST' :
# #         NewBusiness = Business(FirstName = request.form['FirstName'], LastName = request.form['LastName'], Email = request.form['Email'], PhoneNumber = request.form['PhoneNumber'], Address = request.form['Address'], BusinesName = request.form['BusinesName'])
# #         try :
# #             db.session.add(NewBusiness)
# #             db.session.commit()
# #             flash('Yes !! Business inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_business'))
# #         except :
# #             flash('No !! ' + Sad + ' Business did not insert successfully . Please check insertion ', 'danger')
        
# #     return redirect(url_for('get_business'))

# # # edit business
# # @app.route('/business/<int:IdBusines>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_busines(IdBusines):
# #     if request.method == 'POST':
# #         EditBusiness = db.session.query(Business).filter_by(IdBusines = IdBusines).one()
# #         EditBusiness.FirstName = request.form['FirstName']
# #         EditBusiness.LastName = request.form['LastName']
# #         EditBusiness.Email = request.form['Email']
# #         EditBusiness.PhoneNumber = request.form['PhoneNumber']
# #         EditBusiness.Address = request.form['Address']
# #         EditBusiness.BusinesName = request.form['BusinesName']
# #         try :
# #             db.session.add(EditBusiness)
# #             db.session.commit()
# #             flash('Yes !! Business is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_business'))
# #         except :
# #             flash('No !! ' + Sad + ' Business did not edit successfully . Please check insertion ' , 'danger')
        
# #     return redirect(url_for('get_business'))

        

# # # delete Business
# # @app.route('/business/<int:IdBusines>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_business(IdBusines):
# #     if request.method == 'GET':
# #         DeleteBusines = db.session.query(Business).filter_by(IdBusines = IdBusines).one()
# #         try :
# #             db.session.delete(DeleteBusines)
# #             db.session.commit()
# #             flash('Yes !! Business is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_business'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
          
# #     return redirect(url_for('get_business'))


# # # get market price 
# # @app.route('/market_price', methods=['POST', 'GET'])
# # @login_required
# # def get_market_price():
# #     PriceItems = db.session.query(Price).all()  
# #     QuantityItems = db.session.query(Quantity).filter_by(Enabled = 1).all()
# #     MarketItems = db.session.query(Market).filter_by(Enabled = 1).all()
# #     CropItems = db.session.query(Crop).filter_by(Enabled = 1).all()
# #     ConditionItems = db.session.query(Conditions).all()
# #     return render_template('market_price.html', PriceItems = PriceItems, QuantityItems = QuantityItems ,MarketItems = MarketItems, CropItems = CropItems, ConditionItems=ConditionItems )


# # # add market price
# # @app.route('/market_price/new', methods=['POST', 'GET'])
# # @login_required
# # def add_price():
# #     if request.method == "POST" :
# #         try :
# #             NewPrice = Price(IdCrop = request.form['Crop'], IdMarket = request.form['Market'], IdUser = current_user.IdUser, IdQty = request.form['Qty'], IdCondition = request.form['Condition'], Price = request.form['Price'], CreatedAt = datetime.date(datetime.now()))
# #             db.session.add(NewPrice)
# #             db.session.commit()
            
# #             flash('Yes !! Price inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_market_price'))
# #         except :            
# #             flash('No !! ' + Sad + ' Price did not insert successfully . Please check insertion ' , 'danger')
 
# #     return redirect(url_for('get_market_price'))

# # # edit price
# # @app.route('/market_price/<int:IdPrice>/edit', methods=['POST','GET'])
# # @login_required
# # def edit_price(IdPrice):
# #     if request.method == 'POST' :
# #         EditPrice = db.session.query(Price).filter_by(IdPrice = IdPrice).one()
# #         EditPrice.IdCrop = request.form['Crop']
# #         EditPrice.IdMarket = request.form['Market']
# #         EditPrice.IdQty = request.form['Qty']
# #         EditPrice.IdCondition = request.form['Condition']
# #         EditPrice.Price = request.form['Price']
# #         try :
# #             db.session.add(EditPrice)
# #             db.session.commit()
# #             flash('Yes !! Price is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_market_price'))
# #         except :
# #             flash('No !! ' + Sad + ' Price did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_market_price'))

# # # delete price
# # @app.route('/market_price/<int:IdPrice>/delete', methods=['POST','GET'])
# # @login_required
# # def delete_price(IdPrice):
# #     if request.method == 'GET':
# #         DeletePrice = db.session.query(Price).filter_by(IdPrice = IdPrice).one()
# #     try :
# #         db.session.delete(DeletePrice)
# #         db.session.commit()
# #         flash('Yes !! Price is deleted successfully '+ Happy , 'success')
# #         return redirect(url_for('get_market_price'))
# #     except :
# #         flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')

# #     return redirect(url_for('get_market_price'))


# # # get all price check session
# # @app.route('/price_checker_session', methods=['POST','GET'])
# # @login_required
# # def get_price_checker_session():
# #     PriceSession = db.session.query(Pricechecksession).all()
# #     return render_template('price_checker.html', PriceSession = PriceSession)

# # # get all price mechanism session
# # @app.route('/price_mechasnim_session', methods=['POST','GET'])
# # @login_required
# # def get_price_mechansim_session():
# #     PriceMechanism = db.session.query(Pricemechsession).all()
# #     return render_template('price_mechansim.html', PriceMechanism = PriceMechanism)


# # # report page
# # @app.route('/report', methods=['POST','GET'])
# # @login_required
# # def report():
# #     return render_template('report.html')

# # # get status 
# # @app.route('/situation', methods=['POST', 'GET'])
# # @login_required
# # def get_situation():
# #     SituationItems = db.session.query(Situation).all()
# #     return render_template('status.html', SituationItems = SituationItems)


# # # insert new status 
# # @app.route('/situation/new', methods=['POST', 'GET'])
# # @login_required
# # def add_situation():
# #     if request.method == 'POST':
# #         NewSituation = Situation(Situation = request.form['SituationName'])
# #         try :
# #             db.session.add(NewSituation)
# #             db.session.commit()
# #             flash('Yes !! Status inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_situation'))
# #         except :
# #             flash('No !! ' + Sad + ' Status did not insert successfully . Please check insertion ' , 'danger')
          
# #     return redirect(url_for('get_situation'))


# # # edit status
# # @app.route('/situation/<int:IdSituation>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_situation(IdSituation):
# #     if request.method == 'POST':
# #         EditSituation = db.session.query(Situation).filter_by(IdSituation = IdSituation).one()
# #         EditSituation.Situation = request.form['SituationName']
# #         try :
# #             db.session.add(EditSituation)
# #             db.session.commit()
# #             flash('Yes !! Status is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_situation'))
# #         except :
# #             flash('No !! ' + Sad + ' Status did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_situation'))


# # # delete status
# # @app.route('/situation/<int:IdSituation>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_situation(IdSituation):
# #     if request.method == 'GET':
# #         DeleteSituation = db.session.query(Situation).filter_by(IdSituation = IdSituation).one()
# #         try :
# #             db.session.delete(DeleteSituation)
# #             db.session.commit()
# #             flash('Yes !! Status is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_situation'))
# #         except :
# #            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
         
# #     return redirect(url_for('get_situation'))

# # # get orders
# # @app.route('/order', methods=['POST', 'GET'])
# # @login_required
# # def get_order():
# #     OrdersItems = db.session.query(Orders).all()
# #     CropItems = db.session.query(Crop).filter_by(Enabled = 1).all()
# #     MarketItems = db.session.query(Market).filter_by(Enabled = 1).all()
# #     QuantityItems = db.session.query(Quantity).filter_by(Enabled = 1).all()
# #     OrderStatusItems = db.session.query(OrderStatus).all()
# #     return render_template('orders.html', OrdersItems = OrdersItems, CropItems = CropItems, MarketItems = MarketItems, QuantityItems = QuantityItems, OrderStatusItems = OrderStatusItems)

# # # add new order
# # @app.route('/order/new', methods=['POST', 'GET'])
# # @login_required
# # def add_order():
# #     if request.method == 'POST':
# #         NewOrder = Orders(OrderNumber = "O"+random_string_generator(), BusinesName = request.form['BusinesName'], PhoneNumber = request.form['PhoneNumber'], Address = request.form['Address'], IdCrop = request.form['Crop'], IdMarket = request.form['Market'],  IdQty = request.form['Qty'], IdOrderStatus = request.form['OrderStatus'], Price = request.form['Price'])
# #         try :
# #             db.session.add(NewOrder)
# #             db.session.commit()
# #             flash('Yes !! Order inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_order'))
# #         except :
# #             flash('No !! ' + Sad + ' Order did not insert successfully . Please check insertion ', 'danger')
          
# #     return redirect(url_for('get_order'))

# # # edit order
# # @app.route('/order/<int:IdOrder>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_order(IdOrder):
# #     if request.method == 'POST':
# #         EditOrder = db.session.query(Orders).filter_by(IdOrder = IdOrder).one()
# #         EditOrder.BusinesName = request.form['BusinesName']
# #         EditOrder.PhoneNumber = request.form['PhoneNumber']
# #         EditOrder.Address = request.form['Address']
# #         EditOrder.IdCrop  = request.form['Crop']
# #         EditOrder.IdMarket = request.form['Market']
# #         EditOrder.IdQty = request.form['Qty']
# #         EditOrder.Price  = request.form['Price']
# #         try :
# #             db.session.add(EditOrder)
# #             db.session.commit()
# #             flash('Yes !! Order is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_order'))
# #         except :
# #             flash('No !! ' + Sad + ' Order did not edit successfully . Please check insertion ' , 'danger')
           
# #     return redirect(url_for('get_order'))


# # # edit status order
# # @app.route('/order/<int:IdOrder>/status', methods=['POST', 'GET'])
# # @login_required
# # def edit_status_order(IdOrder):
# #     if request.method == 'POST':
# #         EditOrder = db.session.query(Orders).filter_by(IdOrder = IdOrder).one()
# #         EditOrder.IdOrderStatus = request.form['OrderStatusName']
       
# #         try :
# #             db.session.add(EditOrder)
# #             db.session.commit()
# #             flash('Yes !! Order status is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_order'))
# #         except :
# #             flash('No !! ' + Sad + ' Order status did not edit successfully . Please check insertion ' , 'danger')
         
# #     return redirect(url_for('get_order'))


# # # delete Order
# # @app.route('/order/<int:IdOrder>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_order(IdOrder):
# #     if request.method == 'GET':
# #         DeleteOrder = db.session.query(Orders).filter_by(IdOrder = IdOrder).one()
# #         try :
# #             db.session.delete(DeleteOrder)
# #             db.session.commit()
# #             flash('Yes !! Order is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_order'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
        
# #     return redirect(url_for('get_order'))


# # # get  order status 
# # @app.route('/order_status', methods=['POST', 'GET'])
# # @login_required
# # def get_order_status():
# #     OrderStatusItems = db.session.query(OrderStatus).all()
# #     return render_template('order_status.html', OrderStatusItems = OrderStatusItems)


# # # insert new order status 
# # @app.route('/order_status/new', methods=['POST', 'GET'])
# # @login_required
# # def add_order_status():
# #     if request.method == 'POST':
# #         NewOrderStatus = OrderStatus(OrderStatus = request.form['OrderStatusName'])
# #         try :
# #             db.session.add(NewOrderStatus)
# #             db.session.commit()
# #             flash('Yes !! Order status inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_order_status'))
# #         except :
# #             flash('No !! ' + Sad + ' Order status did not insert successfully . Please check insertion ', 'danger')
         
# #     return redirect(url_for('get_order_status'))


# # # edit order status
# # @app.route('/order_status/<int:IdOrderStatus>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_order_status(IdOrderStatus):
# #     if request.method == 'POST':
# #         EditOrderStatus = db.session.query(OrderStatus).filter_by(IdOrderStatus = IdOrderStatus).one()
# #         EditOrderStatus.OrderStatus = request.form['OrderStatusName']
# #         try :
# #             db.session.add(EditOrderStatus)
# #             db.session.commit()
# #             flash('Yes !! Order status is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_order_status'))
# #         except :
# #             flash('No !! ' + Sad + ' Order status did not edit successfully . Please check insertion ' , 'danger')
           
# #     return redirect(url_for('get_order_status'))


# # # delete order status
# # @app.route('/order_status/<int:IdOrderStatus>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_order_status(IdOrderStatus):
# #     if request.method == 'GET':
# #         DeleteOrderStatus = db.session.query(OrderStatus).filter_by(IdOrderStatus = IdOrderStatus).one()
# #         try :
# #             db.session.delete(DeleteOrderStatus)
# #             db.session.commit()
# #             flash('Yes !! Order status is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_order_status'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
# #     return redirect(url_for('get_order_status'))


# # # get all predictions 
# # @app.route('/prediction', methods=['POST', 'GET'])
# # @login_required
# # def prediction():
# #     CropItems = db.session.query(Crop).all()
# #     PredictionItems = db.session.query(Prediction).all()
# #     return render_template('prediction.html', CropItems = CropItems, PredictionItems = PredictionItems)

# # # add new prediction
# # @app.route('/prediction/new', methods=['POST', 'GET'])
# # @login_required
# # def add_prediction():
# #     if request.method == 'POST':
# #         NewPrediction = Prediction(IdCrop = request.form['Crop'], PredictionDate = request.form['PredictionDate'], AvgPrice = request.form['AveragePrice'], PrePrice = request.form['PredictPrice'])
# #         try :
# #             db.session.add(NewPrediction)
# #             db.session.commit()
# #             flash('Yes !! Prediction inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('prediction'))
# #         except :
# #             flash('No !! ' + Sad + ' Prediction did not insert successfully . Please check insertion ', 'danger')
           
# #     return redirect(url_for('prediction'))


# # # edit prediction
# # @app.route('/prediction/<int:IdPred>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_prediction(IdPred):
# #     if request.method == 'POST':
# #         EditPrediction = db.session.query(Prediction).filter_by(IdPred = IdPred).one()
# #         EditPrediction.IdCrop = request.form['Crop']
# #         EditPrediction.PredictionDate = request.form['PredictionDate']
# #         EditPrediction.AvgPrice = request.form['AveragePrice']
# #         EditPrediction.PrePrice = request.form['PredictPrice']
# #         try :
# #             db.session.add(EditPrediction)
# #             db.session.commit()
# #             flash('Yes !! Prediction is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('prediction'))
# #         except :
# #             flash('No !! ' + Sad + ' Prediction did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('prediction'))

        
# # # delete prediction
# # @app.route('/prediction/<int:IdPred>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_prediction(IdPred):
# #     if request.method == 'GET':
# #         DetelePred = db.session.query(Prediction).filter_by(IdPred = IdPred).one()
# #         try :
# #             db.session.delete(DetelePred)
# #             db.session.commit()
# #             flash('Yes !! Prediction is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('prediction'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
        
# #     return redirect(url_for('prediction'))

# # # get feedback
# # @app.route('/feedback', methods=['POST', 'GET'])
# # @login_required
# # def get_feedback():
# #     BusinessItems = db.session.query(Business).all()    
# #     FeedbackItems = db.session.query(Feedback).all()      
# #     return render_template('feedback.html', BusinessItems = BusinessItems, FeedbackItems = FeedbackItems)

# # # add Feedback
# # @app.route('/feedback/new', methods=['POST', 'GET'])
# # @login_required
# # def add_feedback():
# #     if request.method == 'POST' :
# #         NewFeedback = Feedback(IdBusines = request.form['Business'], Feedback = request.form['Feedback'], IdUser = current_user.IdUser)
# #         try :
# #             db.session.add(NewFeedback)
# #             db.session.commit()
# #             flash('Yes !! Feedback inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_feedback'))
# #         except :
# #             flash('No !! ' + Sad + ' Feedback did not insert successfully . Please check insertion ', 'danger')
        
# #     return redirect(url_for('get_feedback'))


# # # edit Feedback
# # @app.route('/Feedback/<int:IdFeed>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_feedback(IdFeed):
# #     if request.method == 'POST':
# #         EditFeedback = db.session.query(Feedback).filter_by(IdFeed = IdFeed).one()
# #         EditFeedback.IdBusines = request.form['Business']
# #         EditFeedback.Feedback = request.form['Feedback']
# #         EditFeedback.IdUser = current_user.IdUser
# #         try :
# #             db.session.add(EditFeedback)
# #             db.session.commit()
# #             flash('Yes !! Feedback is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_feedback'))
# #         except :
# #             flash('No !! ' + Sad + ' Feedback did not edit successfully . Please check insertion ' , 'danger')

# #     return redirect(url_for('get_feedback'))


# # # delete Feedback
# # @app.route('/Feedback/<int:IdFeed>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_feedback(IdFeed):
# #     if request.method == 'GET':
# #         DeteleFeedback = db.session.query(Feedback).filter_by(IdFeed = IdFeed).one()
# #         try :
# #             db.session.delete(DeteleFeedback)
# #             db.session.commit()
# #             flash('Yes !! Feedback is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_feedback'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
        
# #     return redirect(url_for('get_feedback'))


# # # get  condition
# # @app.route('/condition', methods=['POST', 'GET'])
# # @login_required
# # def get_condition():
# #     conditionItems = db.session.query(Conditions).all()
# #     return render_template('condition.html', conditionItems = conditionItems)


# # # insert new condition
# # @app.route('/condition/new', methods=['POST', 'GET'])
# # @login_required
# # def add_condition():
# #     if request.method == 'POST':
# #         NewCondition = Conditions(ConditionName = request.form['ConditionName'])
# #         try :
# #             db.session.add(NewCondition)
# #             db.session.commit()
# #             flash('Yes !! Condition inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
# #             return redirect(url_for('get_condition'))
# #         except :
# #             flash('No !! ' + Sad + ' Condition did not insert successfully . Please check insertion ', 'danger')
         
# #     return redirect(url_for('get_condition'))


# # # edit Condition
# # @app.route('/condition/<int:IdCondition>/edit', methods=['POST', 'GET'])
# # @login_required
# # def edit_condition(IdCondition):
# #     if request.method == 'POST':
# #         EditCondition = db.session.query(Conditions).filter_by(IdCondition = IdCondition).one()
# #         EditCondition.ConditionName = request.form['ConditionName']
# #         try :
# #             db.session.add(EditCondition)
# #             db.session.commit()
# #             flash('Yes !! Condition is edited successfully '+ Happy , 'success')
# #             return redirect(url_for('get_condition'))
# #         except :
# #             flash('No !! ' + Sad + ' Condition did not edit successfully . Please check insertion ' , 'danger')
           
# #     return redirect(url_for('get_condition'))


# # # delete order status
# # @app.route('/condition/<int:IdCondition>/delete', methods=['POST', 'GET'])
# # @login_required
# # def delete_condition(IdCondition):
# #     if request.method == 'GET':
# #         DeleteCondition = db.session.query(Conditions).filter_by(IdCondition = IdCondition).one()
# #         try :
# #             db.session.delete(DeleteCondition)
# #             db.session.commit()
# #             flash('Yes !! Condition is deleted successfully '+ Happy , 'success')
# #             return redirect(url_for('get_condition'))
# #         except :
# #             flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
# #     return redirect(url_for('get_condition'))



# # logout route
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('login'))


# # # ussd route
# # @app.route('/ussd', methods=['POST', 'GET'])
# # def ussd_callback():
# #     global respsone 
# #     session_id = request.values.get("sessionId", None)
# #     service_code = request.values.get("serviceCode", None)
# #     phone_number = request.values.get("phoneNumber", None)
# #     text =  request.values.get("text", "default")

# #     PriceAll = []
# #     PriceFarmula = []
# #     PriceFarmula10 = []

# #     # FarmulaPrice = db.session.query(Price).filter_by(CreatedAt = datetime.date(datetime.now())).all()
# #     AllMarketPrice = db.session.query(Price).filter_by(CreatedAt = datetime.date(datetime.now())).all()

    
# #     if text == "":
# #         respsone = "CON Welcome to Farmula , place your order \n"
# #         for PriceItem in AllMarketPrice:
# #             if PriceItem.market.Name == 'Farmula' and '10' in PriceItem.qty.Qty :
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 respsone += "1. Order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + PriceItem.market.Name + "=" + str(PriceItem.Price) + "Ksh" + "\n"

# #             elif PriceItem.market.Name == 'Farmula' and PriceItem.qty.Qty == '20kg peeled':
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 respsone += "2. Order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + PriceItem.market.Name + "=" + str(PriceItem.Price) + "Ksh" + "\n"
            
# #             elif PriceItem.market.Name == 'Farmula' and  PriceItem.qty.Qty == '20kg unpeeled':
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 respsone += "3. Order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + PriceItem.market.Name + "=" + str(PriceItem.Price) + "Ksh" + "\n"  

# #             elif PriceItem.market.Name == 'Farmula' and '50'  in PriceItem.qty.Qty :
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 respsone += "4. Order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + PriceItem.market.Name + "=" + str(PriceItem.Price) + "Ksh" + "\n"

# #         respsone += "5. Check Price \n"
    
# #     elif text == '1':
# #         for PriceItem in AllMarketPrice:
# #             if PriceItem.market.Name == 'Farmula' and '10' in PriceItem.qty.Qty :
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 NewOrder = Orders(OrderNumber = "O"+random_string_generator(), BusinesName = '', PhoneNumber = phone_number, Address = '', IdCrop = PriceItem.crop.IdCrop, IdMarket = PriceItem.market.IdMarket, IdQty = PriceItem.qty.IdQty, IdOrderStatus = '1', Price = PriceItem.Price)
# #                 db.session.add(NewOrder)
# #                 db.session.commit()
# #                 respsone = "END Thanks for using Farmula services to order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + str(PriceItem.Price) + "Ksh" + "\n"
  
# #     elif text == '2':
# #         for PriceItem in AllMarketPrice:
# #             if PriceItem.market.Name == 'Farmula' and PriceItem.qty.Qty == '20kg peeled' :
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 NewOrder = Orders(OrderNumber = "O"+random_string_generator(), BusinesName = '', PhoneNumber = phone_number, Address = '', IdCrop = PriceItem.crop.IdCrop, IdMarket = PriceItem.market.IdMarket, IdQty = PriceItem.qty.IdQty, IdOrderStatus = '1', Price = PriceItem.Price)
# #                 db.session.add(NewOrder)
# #                 db.session.commit()
# #                 respsone = "END Thanks for using Farmula services to order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + str(PriceItem.Price) + "Ksh" + "\n"

# #     elif text == '3':
# #         for PriceItem in AllMarketPrice:
# #             if PriceItem.market.Name == 'Farmula' and  PriceItem.qty.Qty == '20kg unpeeled' :
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 NewOrder = Orders(OrderNumber = "O"+random_string_generator(), BusinesName = '', PhoneNumber = phone_number, Address = '', IdCrop = PriceItem.crop.IdCrop, IdMarket = PriceItem.market.IdMarket, IdQty = PriceItem.qty.IdQty, IdOrderStatus = '1', Price = PriceItem.Price)
# #                 db.session.add(NewOrder)
# #                 db.session.commit()
# #                 respsone = "END Thanks for using Farmula services to order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + str(PriceItem.Price) + "Ksh" + "\n"
  
# #     elif text == '4':
# #         for PriceItem in AllMarketPrice:
# #             if PriceItem.market.Name == 'Farmula' and '50'  in PriceItem.qty.Qty :
# #                 PriceFarmula10.append([PriceItem.market.Name, PriceItem.crop.Name ,PriceItem.qty.Qty, PriceItem.Price])
# #                 NewOrder = Orders(OrderNumber = "O"+random_string_generator(), BusinesName = '', PhoneNumber = phone_number, Address = '', IdCrop = PriceItem.crop.IdCrop, IdMarket = PriceItem.market.IdMarket, IdQty = PriceItem.qty.IdQty, IdOrderStatus = '1', Price = PriceItem.Price)
# #                 db.session.add(NewOrder)
# #                 db.session.commit()
# #                 respsone = "END Thanks for using Farmula services to order " + PriceItem.crop.Name + " "+ PriceItem.qty.Qty + "@" + str(PriceItem.Price) + "Ksh" + "\n"
  

# #     elif text == "5":
# #         respsone = "CON "
# #         respsone += "1. 50Kg \n"
# #         respsone += "2. 90Kg \n"
# #         respsone += "3. 120Kg \n"

# #     elif text == "5*1":
# #         respsone = "END Price in different markets \n"
# #         for MarketPrice in AllMarketPrice:
# #             if '50' in MarketPrice.qty.Qty and MarketPrice.market.Name != 'Farmula':
# #                 PriceAll.append([MarketPrice.market.Name, MarketPrice.crop.Name ,MarketPrice.qty.Qty, MarketPrice.Price])
# #                 respsone += " " + MarketPrice.crop.Name + " "+ MarketPrice.qty.Qty + "@" + MarketPrice.market.Name + "=" + str(MarketPrice.Price) + "Ksh" + "\n"
# #             CheckSession = Pricechecksession(PhoneNumber = phone_number, Hooks = text)
# #             db.session.add(CheckSession)
# #             db.session.commit()

# #     elif text == "5*2":
# #         respsone = "END Price in different markets \n"
# #         for MarketPrice in AllMarketPrice:
# #             if '90' in MarketPrice.qty.Qty and MarketPrice.market.Name != 'Farmula':
# #                 PriceAll.append([MarketPrice.market.Name, MarketPrice.crop.Name ,MarketPrice.qty.Qty, MarketPrice.Price])
# #                 respsone += " " + MarketPrice.crop.Name + " "+ MarketPrice.qty.Qty + "@" + MarketPrice.market.Name + "=" + str(MarketPrice.Price) + "Ksh" + "\n"
# #             CheckSession = Pricechecksession(PhoneNumber = phone_number, Hooks = text)
# #             db.session.add(CheckSession)
# #             db.session.commit()  

# #     elif text == "5*3":
# #         respsone = "END Price in different markets \n"
# #         for MarketPrice in AllMarketPrice:
# #             if '120' in MarketPrice.qty.Qty and MarketPrice.market.Name != 'Farmula':
# #                 PriceAll.append([MarketPrice.market.Name, MarketPrice.crop.Name ,MarketPrice.qty.Qty, MarketPrice.Price])
# #                 respsone += " " + MarketPrice.crop.Name + " "+ MarketPrice.qty.Qty + "@" + MarketPrice.market.Name + "=" + str(MarketPrice.Price) + "Ksh" + "\n"
# #             CheckSession = Pricechecksession(PhoneNumber = phone_number, Hooks = text)
# #             db.session.add(CheckSession)
# #             db.session.commit()  

# #     return respsone
