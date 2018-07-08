from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key='ChumbaWumba'

# http://localhost:5000 - have this display a nice looking HTML form.  The form should be submitted to '/result'
@app.route('/')
def index():
    return render_template('dojo_survey.html')

#http://localhost:5000/result - have this display a html with the information that was submitted by POST
@app.route('/result', methods=['POST'])
def result():
    # Set up a boolean to let us know if we hit an error or not
    error = False
    if len(request.form['name']) < 1:
        flash("Name is required!")
        error = True
    if len(request.form['comment']) < 1:
        flash("Comment field cannot be empty!")
        error = True
    if len(request.form['comment']) > 120:
        flash("Comment length must be less than 120!")
        error = True
    # If the boolean has been toggled to true we return the user to the index
    if error == True:
        return redirect('/')
    else:
        return render_template('/result.html')

#http://localhost:5000/danger - have this redirect back to "/".
#Before redirecting back print in the terminal/console a message: 
# "a user tried to visit /danger. we have redirected the user to /".
@app.route('/danger')
def danger():
    print("A user tried to visit /danger.  we have redirected the user to /")
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)