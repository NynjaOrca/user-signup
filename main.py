from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['POST'])
def submit_information():

# FIELD RETRIEVAL
    username = request.form['username']
    password = request.form['password']
    ver_pass = request.form['verify']
    email = request.form['email']

# ERROR DECLARATION
    uError = ''
    pError = ''
    vError = ''
    eError = ''

# CHARACTER LISTS
    whitespace = ' '
    digits = ['0','1','2','3','4','5','6','7','8','9']
    specialChars = ['!','@','#','$','%','^','&','*','?','-','+','=']
    uppercase = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']



# CHECK USERNAME REQUIREMENTS
    if not username:
        uError = "Please enter a username."
        # return redirect('/?uError=' + uError)

    if ((len(username) < 3) or (len(username) > 20)):
        uError = "Username must between 3 - 20 characters."
        # return redirect('/?uError=' + uError)

    if ' ' in str(username):
        uError = "Username must not contain white space." 
        # return redirect('/?uError=' + uError)


# CHECK PASSWORD REQUIREMENTS
    digiChar = 0
    specChar = 0
    whitChar = 0
    upprChar = 0
    
    for char in str(password):
        if char == whitespace:
            whitChar += 1
        elif char in digits:
            digiChar += 1
        elif char in specialChars:
            specChar += 1
        elif char in uppercase:
            upprChar += 1
        else:
            continue

    if not password:
        pError = "Please enter a password."
        # return redirect('/?pError=' + pError)

    if ((len(password) < 3) or (len(password) > 20)):
        pError = "Password must between 3 - 20 characters."
        # return redirect('/?pError=' + pError)

    if digiChar < 1:
        pError = "Password must contain at least 1 digit."
        # return redirect('/?pError=' + pError)

    if specChar < 1:
        pError = "Password must contain at least 1 special character."
        # return redirect('/?pError=' + pError)

    if whitChar != 0:
        pError = "Password must not contain white space."
        # return redirect('/?pError=' + pError)        

    if upprChar < 1:
        pError = "Password must contain at least 1 uppercase character."
        # return redirect('/?pError=' + pError)

# VERIFY THAT THE PASSWORDS MATCH
    if ver_pass != password:
        vError = "Your passwords do not match."
        # return redirect('/?vError=' + vError)
    

# CHECK EMAIL REQUIREMENTS
    atSymbol = '@'
    pdSymbol = '.'

    atCount = 0
    pdCount = 0
    wsCount = 0

    for char in email:
        if char == atSymbol:
            atCount += 1
        elif char == pdSymbol:
            pdCount += 1
        elif char == whitespace:
            wsCount += 1

    if atCount != 1:
        eError = "Invalid Email address."
        # return redirect('/?eError=' + eError) 
    if pdCount != 1:
        eError = "Invalid Email address."
        # return redirect('/?eError=' + eError)
    if wsCount > 0:
        eError = "Invalid Email address."
        # return redirect('/?eError=' + eError)



    if eError or pError or uError or vError:
        return render_template('signup-form.html', username=username, uError=uError, pError=pError, vError=vError, email=email, eError=eError)
    else:
        return render_template('welcome.html', username=username)

@app.route("/")
def user_signup():
    username_error = request.args.get("uError")
    password_error = request.args.get("pError")
    verification_error = request.args.get("vError")
    email_error = request.args.get("eError")
    return render_template('signup-form.html', uError=username_error, pError=password_error, vError=verification_error, eError=email_error)

app.run()