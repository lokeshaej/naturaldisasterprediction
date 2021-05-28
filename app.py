import numpy as np
from flask import Flask, request, jsonify, render_template,abort
from joblib import load
import requests
from training import prediction
from sendemail import sendmail
import smtplib


model= load('earthquakee.save')
trans=load('earthquakee')
modelcy=load('cyclone.save')
transcy=load('cyclone')
modelfl=load('floods.save')
transfl=load('floodsk')

location="davangere"   
latitude=int(14.464408) 
longitude=int(76.921761)
URL = "https://geocode.search.hereapi.com/v1/geocode"

api_key = 'Mjrc15J-z2wO8epDN9XEVq76WLBdRj2f3Rs2UilKvgo' # Acquire from developer.here.com
PARAMS = {'apikey':api_key,'q':location} 

# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
data = r.json()
print(data)

#Acquiring the latitude and longitude from JSON 
latitude = data['items'][0]['position']['lat']
#print(latitude)
longitude = data['items'][0]['position']['lng']
#print(longitude)
#Flask code 
class School:
    def __init__(self, key, name, lat, lng):
           self.key  = key
           self.name = name
           self.lat  = lat
           self.lng  = lng
schools = (School('earthquake',  location,   latitude, longitude),)
schools_by_key = {school.key: school for school in schools}
app = Flask(__name__)
@app.route('/')
def homepagea():
    return render_template('homepage.html', schools=schools)
@app.route('/homepage')
def homepage():
    return render_template('homepage.html', schools=schools)


@app.route('/index')
def index():
    return render_template('index.html', schools=schools)
@app.route('/cyclone')
def cyclone():
    return render_template('cyclone.html')
@app.route('/flood')
def flood():
    return render_template('flood.html')
@app.route('/y_predict',methods=['POST'])
def y_predict():
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    if request.method == 'POST' :
        location= request.form['location']
        depth = request.form['depth']
        print(depth)
        print(location)
        
        api_key = 'Mjrc15J-z2wO8epDN9XEVq76WLBdRj2f3Rs2UilKvgo' # Acquire from developer.here.com
        PARAMS = {'apikey':api_key,'q':location} 
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        print(data)
        #Acquiring the latitude and longitude from JSON 
        lat = data['items'][0]['position']['lat']
        print(lat)
        lng = data['items'][0]['position']['lng']
        print(lng)
        xx_test= [[lat,lng,depth]]
        x_test= [[lat,lng,depth]]
        print(x_test)
        test=trans.transform(x_test)
        test=test[:,0:]
        print(test)
        prediction = model.predict(xx_test) 
        print(prediction)
        output=prediction[0] 
        if output < 4 :
            print(output)
            output="No EarthQuake In This Region"
        elif output >4 and output <5.5 :
            print(output)
            output="EarthQuake  In This Region May Occurs Soon"
        else :
            print(output)
            output="EarthQuake In This Region Occurs "
        print(output)
        
        
        #Flask code 
        
        return render_template('index2.html', prediction_text='{}'.format(output),lat=lat,lng=lng)

@app.route("/<school_code>")
def show_school(school_code):
    school = schools_by_key.get(school_code)
    if school:
        return render_template('index.html', school=school)
    else:
        abort(404)




@app.route('/y_predictt',methods=['POST'])
def y_predictt():
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    if request.method == 'POST' :
        location= request.form['location']
        pressure = request.form['pressure']
        ne= request.form['ne']
        nw = request.form['nw']
        se= request.form['se']
        sw= request.form['sw']
        
        print(pressure)
        print(location)
        
        api_key = 'Mjrc15J-z2wO8epDN9XEVq76WLBdRj2f3Rs2UilKvgo' # Acquire from developer.here.com
        PARAMS = {'apikey':api_key,'q':location} 
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        print(data)
        #Acquiring the latitude and longitude from JSON 
        lat = data['items'][0]['position']['lat']
        print(lat)
        lng = data['items'][0]['position']['lng']
        print(lng)
        xx_test= [[lat,lng,pressure,ne,nw,se,sw]]
        x_test= [[lat,lng,pressure,ne,nw,se,sw]]
        print(x_test)
        test=transcy.transform(x_test)
        test=test[:,0:]
        print(test)
        prediction = modelcy.predict(xx_test) 
        print(prediction)
        output=prediction[0] 
        if output < 3.9 :
            print(output)
            output="No Cyclone In This Region"
        elif output >3.9 and output <4.5 :
            print(output)
            output="Tropical Cyclone of intensity is greater than 64 knots"
        elif output >4.5 and output <7.5 :
            print(output)
            output="No Cyclone In This Region"
        elif output >7.5 and output <8.8 :
            print(output)
            output="Tropical Cyclone of intensity is greater than 34 knots"
        elif output >8.8 and output <10.9 :
            print(output)
            output="Tropical Cyclone of intensity is less than 34 knots"
        elif output >10.9 and output <12 :
            print(output)
            output="Tropical Cyclone of intensity is between 34-64 knots"
        
        else :
            print(output)
            output="No Cyclone In This Region"
        print(output)
        
        
        #Flask code 
        
        return render_template('cyclone.html', prediction_text='{}'.format(output),lat=lat,lng=lng)




@app.route('/y_predicttt',methods=['POST'])
def y_predicttt():
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    if request.method == 'POST' :
        location= request.form['location']
        annual= request.form['annual']
        jan= request.form['jan']
        jun= request.form['jun']
        
        
        print(location)
        
        api_key = 'Mjrc15J-z2wO8epDN9XEVq76WLBdRj2f3Rs2UilKvgo' # Acquire from developer.here.com
        PARAMS = {'apikey':api_key,'q':location} 
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()
        print(data)
        #Acquiring the latitude and longitude from JSON 
        lat = data['items'][0]['position']['lat']
        print(lat)
        lng = data['items'][0]['position']['lng']
        print(lng)
        final = prediction.get_data(lat, lng)
        final[4] *= 15
        temp=round(final[0], 2)
        maxt=round(final[1], 2) 
        wspd=round(final[2], 2) 
        cloudcover=round(final[3], 2) 
        percip=round(final[4], 2) 
        humidity=round(final[5], 2)
        temp=round(final[0], 2)
        templ=(temp-32)*5/9
        tempc=float("{:.2f}".format(templ))
        mtemp=round(final[1], 2)
        mtempl=(mtemp-32)*5/9
        mtempc=float("{:.2f}".format(mtempl))
        
        
        
        xx_test= [[tempc,humidity,cloudcover,annual,jan,jun]]
        x_test= [[tempc,humidity,cloudcover,annual,jan,jun]]
        print(x_test)
        test=transfl.transform(x_test)
        test=test[:,0:]
        print(test)
        predictionk = modelfl.predict(xx_test) 
        print(predictionk)
        output=predictionk[0] 
        if output < 0.7 :
            print(output)
            output="No Floods In "+location+" Region and Safe zone"
        
        else :
            print(output)
            output="Floods May Occurs in "+location+" Region and Danger Zone" 
        print(output)
        
        
        #Flask code 
        
        return render_template('flood.html', temp=tempc, maxt=mtempc, wspd=wspd, cloudcover=cloudcover, percip=percip, humidity=humidity, prediction_text='{}'.format(output))


@app.route('/contactus', methods =['GET', 'POST'])
def contactus():
    global userid
    msg = 'Contact Sucessfully , We will try to connect soon as possible early' 
   
  
    if request.method == 'POST' :
        username = request.form['username']
        email = request.form['email']
        message = request.form['message']
        tt=message
        TEXT = "Hello "+username + ",\n\n"+ """Thanks for contacting us for prediction of Natural Disaster Prediction, as soon possible early we will contact you """ 
        message  = 'Subject: {}\n\n{}'.format("Disaster Prediction", TEXT)
        xy="Disaster Prediction"
        sendmail(TEXT,email,xy,tt)
    return render_template('contactus.html', msg = msg)  
        




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True,port = 5000)