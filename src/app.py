
from flask import Flask, render_template, request
from process import calc_density

app = Flask(__name__)



@app.route('/', methods=["get","post"])
def hello():
    message=""
    if request.method == "POST":
        area=request.form.get("area")
        density=request.form.get("density")
        modulus=request.form.get("modulus")
        hardener=request.form.get("hardener")
        epoxy=request.form.get("epoxy")
        surf_density=request.form.get("surf_density")
        resin=request.form.get("resin")
        angle=request.form.get("angle")
        step=request.form.get("step")
        stitch_dens=request.form.get("stitch_dens")        
        dens=calc_density(area,density,modulus,hardener,epoxy,surf_density,resin,angle,step,stitch_dens)
        message = f'Прочность при растяжении {dens}'
    return render_template("index.html",message=message)

#@app.route('/login/',methods=["get","post"])
#def login():
#    message = "Место под сообщение"
#    if request.method == "POST":
#        username = request.form.get("username")
#        password = request.form.get("password")
#        if username != "123":
#            message="Неправильное имя пользователя"
#        else:
#            message=f'Имя пользователя {username}, пароль {password}'
#
#    message = "место под сообщение"
#    return render_template("login.html",message = message)

#if __name__ == "__main__":
app.run()