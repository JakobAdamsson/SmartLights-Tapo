from PyP100 import PyL530

# Import to run webbapp
from flask import Flask, jsonify, render_template, request, redirect, url_for
import requests
import json


# Instanciate flask app
app = Flask(__name__)

# Load json file with ip, email and password
jsonfile = open("secure.json")
data = json.load(jsonfile)

jsonfile2 = open("ip.json")
piip = json.load(jsonfile2)


class lightbulb:
    def __init__(self, ip, email, password):
        self.ip = ip
        self.email = email
        self.password = password
        self.bulb = PyL530.L530(self.ip, self.email, self.password)
        self.bulb.handshake()
        self.bulb.login()

    def turn_on(self):
        self.bulb.turnOn()

    def turn_off(self):
        self.bulb.turnOff()

    def set_brightness(self, value):
        self.bulb.setBrightness(value)

    def get_info(self):
        return [
            self.bulb.getDeviceInfo()["result"]["device_on"],
            self.bulb.getDeviceInfo()["result"]["brightness"],
        ]


#################################################################################################
# CREATE YOUR BULBS HERE:
# bulb = lightbulb(ip, email, password)

lamp1 = lightbulb(
    data["bulb1"][0]["ip"], data["bulb1"][0]["email"], data["bulb1"][0]["password"]
)


lamp2 = lightbulb(
    data["bulb2"][0]["ip"], data["bulb2"][0]["email"], data["bulb2"][0]["password"]
)

##################################################################################################


# For flask
@app.route("/")
def home_page():
    return render_template("index.html")


# ------------>bulb1<-------------#
# On of settings
@app.route("/b1on")
def turn_onb1():
    lamp1.turn_on()
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1off")
def turn_offb1():
    lamp1.turn_off()
    return redirect(piip["pi4_ip"][0]["ip"])


# Brightness
@app.route("/b1_5")
def brightness_5():
    lamp1.set_brightness(5)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_10")
def brightness_10():
    lamp1.set_brightness(10)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_15")
def brightness_15():
    lamp1.set_brightness(15)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_20")
def brightness_20():
    lamp1.set_brightness(20)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_25")
def brightness_25():
    lamp1.set_brightness(25)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_30")
def brightness_30():
    lamp1.set_brightness(30)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_35")
def brightness_35():
    lamp1.set_brightness(35)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_40")
def brightness_40():
    lamp1.set_brightness(40)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_45")
def brightness_45():
    lamp1.set_brightness(45)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_50")
def brightness_50():
    lamp1.set_brightness(50)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_55")
def brightness_55():
    lamp1.set_brightness(55)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_60")
def brightness_60():
    lamp1.set_brightness(60)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_65")
def brightness_65():
    lamp1.set_brightness(65)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_70")
def brightness_70():
    lamp1.set_brightness(70)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_75")
def brightness_75():
    lamp1.set_brightness(75)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_80")
def brightness_80():
    lamp1.set_brightness(80)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_85")
def brightness_85():
    lamp1.set_brightness(85)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_90")
def brightness_90():
    lamp1.set_brightness(90)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_95")
def brightness_95():
    lamp1.set_brightness(95)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b1_100")
def brightness_100():
    lamp1.set_brightness(100)
    return redirect(piip["pi4_ip"][0]["ip"])


# Timers
@app.route("/t1_60")
def timer1_60():
    try:
        for i in range(1, 100):
            lamp1.set_brightness(i)
            time.sleep(36)
    except KeyError:  # To avoid KeyError -1301, dont know what it means :)
        return render_template("index.html")


@app.route("/t1_30")
def timer1_30():
    try:
        for i in range(1, 100):
            lamp1.set_brightness(i)
            time.sleep(18)
    except KeyError:  # To avoid KeyError -1301, dont know what it means :)
        return render_template("index.html")


# ------------>bulb2<-------------#
@app.route("/b2on")
def turn_onb2():
    lamp2.turn_on()
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2off")
def turn_offb2():
    lamp2.turn_off()
    return redirect(piip["pi4_ip"][0]["ip"])


# Brightness
@app.route("/b2_5")
def brightness2_5():
    lamp2.set_brightness(5)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_10")
def brightness2_10():
    lamp2.set_brightness(10)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_15")
def brightness2_15():
    lamp2.set_brightness(15)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_20")
def brightness2_20():
    lamp2.set_brightness(20)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_25")
def brightness2_25():
    lamp2.set_brightness(25)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_30")
def brightness2_30():
    lamp2.set_brightness(30)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_35")
def brightness2_35():
    lamp2.set_brightness(35)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_40")
def brightness2_40():
    lamp2.set_brightness(40)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_45")
def brightness2_45():
    lamp2.set_brightness(45)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_50")
def brightness2_50():
    lamp2.set_brightness(50)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_55")
def brightness2_55():
    lamp2.set_brightness(55)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_60")
def brightness2_60():
    lamp2.set_brightness(60)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_65")
def brightness2_65():
    lamp2.set_brightness(65)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_70")
def brightness2_70():
    lamp2.set_brightness(70)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_75")
def brightness2_75():
    lamp2.set_brightness(75)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_80")
def brightness2_80():
    lamp2.set_brightness(80)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_85")
def brightness2_85():
    lamp2.set_brightness(85)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_90")
def brightness2_90():
    lamp2.set_brightness(90)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_95")
def brightness2_95():
    lamp2.set_brightness(95)
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/b2_100")
def brightness2_100():
    lamp2.set_brightness(100)
    return redirect(piip["pi4_ip"][0]["ip"])


# Timers
@app.route("/t2_60")
def timer2_60():
    try:
        for i in range(1, 100):
            lamp1.set_brightness(i)
            time.sleep(36)
    except KeyError:  # To avoid KeyError -1301, dont know what it means :)
        return render_template("index.html")


@app.route("/t2_30")
def timer2_30():
    try:
        for i in range(1, 100):
            lamp1.set_brightness(i)
            time.sleep(18)
    except KeyError:  # To avoid KeyError -1301, dont know what it means :)
        return render_template("index.html")


# ------------>All bulbs<-------------#
@app.route("/terminateall")
def terminate_all():
    lamp1.turn_off()
    lamp2.turn_off()
    return redirect(piip["pi4_ip"][0]["ip"])


@app.route("/enableall")
def enable_all():
    lamp1.turn_on()
    lamp2.turn_on()
    return redirect(piip["pi4_ip"][0]["ip"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6969)
