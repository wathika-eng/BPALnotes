from flask import redirect, url_for, app, flash, render_template, request, get_db, res, escape, views


@views.route('/search', methods=['GET'])
def search():
    
    db = get_db()
    qTerm = request.args.get('s')
    if not qTerm:
        flash("You did not search for anything")
        return redirect(url_for('home'))
    elif qTerm:
        cleanQuery = escape(qTerm)
        dbQuery = db.execute('select * from entries where title LIKE ? order by id limit 10', ['%'+ cleanQuery +'%'])
        res = dbQuery.fetchall()
    return render_template('search.html', res=res)