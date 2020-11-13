from flask_login import login_user, current_user, logout_user, login_required
from dashboard.models import  Users,Situation, Products, Concerns
from flask import abort, redirect, url_for, render_template, request, jsonify, flash, Markup, Blueprint
from dashboard import db, bcrypt

concerns = Blueprint('concerns',__name__)

Happy = Markup('<span>&#127881;</span>')
Sad = Markup('<span>&#128557;</span>')
Sassy = Markup('<span>&#128540;</span>')


# get all concerns 
@concerns.route('/concerns', methods=['POST', 'GET'])
@login_required
def get_concerns():
    ConcernsItems = db.session.query(Concerns).all()
    SituationItems = db.session.query(Situation).all()

    return render_template('concerns.html', ConcernsItems = ConcernsItems, SituationItems = SituationItems)


# insert new concerns 
@concerns.route('/concerns/new', methods=['POST', 'GET'])
@login_required
def add_concerns():
    if request.method == 'POST':
        NewConcerns = Concerns(Concerns = request.form['Concerns'], Enabled = request.form['Status'])
        try :
            db.session.add(NewConcerns)
            db.session.commit()
            flash('Yes !! Concerns inserted successfully. Great Job ' + current_user.FirstName + Happy , 'success')
            return redirect(url_for('concerns.get_concerns'))
        except Exception as err :
            print(err)
            flash('No !! ' + Sad + ' Concerns did not insert successfully . Please check insertion ', 'danger')
         
    return redirect(url_for('concerns.get_concerns'))


# edit Concerns status
@concerns.route('/concerns/<int:IdConcerns>/edit', methods=['POST', 'GET'])
@login_required
def edit_concerns(IdConcerns):
    if request.method == 'POST':
        EditConcerns = db.session.query(Concerns).filter_by(IdConcerns = IdConcerns).one()
        EditConcerns.Concerns = request.form['Concerns']
        EditConcerns.Enabled = request.form['Status']
        try :
            db.session.add(EditConcerns)
            db.session.commit()
            flash('Yes !! Concerns is edited successfully '+ Happy , 'success')
            return redirect(url_for('concerns.get_concerns'))
        except Exception as err :
            flash('No !! ' + Sad + ' Concerns did not edit successfully . Please check insertion ' , 'danger')
           
    return redirect(url_for('concerns.get_concerns'))


# delete concerns
@concerns.route('/concerns/<int:IdConcerns>/delete', methods=['POST', 'GET'])
@login_required
def delete_concerns(IdConcerns):
    if request.method == 'GET':
        DeleteConcerns = db.session.query(Concerns).filter_by(IdConcerns = IdConcerns).one()
        try :
            db.session.delete(DeleteConcerns)
            db.session.commit()
            flash('Yes !! Concerns is deleted successfully '+ Happy , 'success')
            return redirect(url_for('concerns.get_concerns'))
        except Exception as err :
            flash('NA NA NA you can delete me. Try again ' + Sassy  , 'danger')
           
    return redirect(url_for('concerns.get_concerns'))


# get all products
@concerns.route('/concerns/api', methods=['POST', 'GET'])
def get_concerns_api():
    if request.method == "GET":
        ConcernsApi = db.session.query(Concerns).filter(Concerns.Enabled == 1).all()
        print(ConcernsApi)
        return jsonify(Concerns=[i.serialize for i in ConcernsApi]), 200   
    else : 
        return jsonify({"result" : "failure", "error" : "400", "Bad Request" : "Use a GET request instead"}), 400
