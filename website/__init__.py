from flask import Flask, render_template, request
def create_app():


    app = Flask(__name__)

    @app.route('/', methods=['POST', 'GET'])
    def home():
        exposed = False
        case_1 = False
        case_2 = False
        case_3 = False
        case_4 = False
        case_5 = False
        case_6 = False
        case_7 = False
        try:
            if request.method == 'POST':
                age = request.form.get('age')
                age = int(age)
                status_vac = request.form.get('status_vac')
                reason_test = request.form.get('reason_test')
                print(age, status_vac, reason_test)
                
                if reason_test == "סיבת הבדיקה" or status_vac == "סטטוס חיסוני": #case_7
                    case_7 = True
                elif reason_test == "Exposed":
                    exposed = True
                elif reason_test != "Exposed" and  age < 3 and (status_vac == "unvaccinated" or status_vac == "healed" or status_vac == "vaccinated"): #case_1
                    print("There is no need for a corona test")
                    case_1 = True
                elif reason_test != "Exposed" and (status_vac == "vaccinated" or status_vac == "healed"): #case_2
                    print("There is no need for a corona test")
                    case_2 = True
                elif ((reason_test == "Cultural and sporting events" or reason_test == "Conferences and exhibitions"
                    or reason_test == "Gyms and pools" or reason_test == "Synagogue" or reason_test == "Halls" or
                    reason_test == "Festivals" or reason_test == "Restaurants" or reason_test == "Museums" or reason_test == "Amusement parks"
                    or reason_test == "Universities") and status_vac == "unvaccinated" and age >= 12): #case_3
                    print("You will have to take a fast corona test and that won't be free")
                    case_3 = True
                elif ((reason_test == "Cultural and sporting events" or reason_test == "Conferences and exhibitions"
                    or reason_test == "Gyms and pools" or reason_test == "Synagogue" or reason_test == "Halls" or
                    reason_test == "Festivals" or reason_test == "Restaurants" or reason_test == "Museums" or reason_test == "Amusement parks"
                    or reason_test == "Universities") and status_vac == "unvaccinated" and age >= 3 and age < 12): #case_4
                    print("You will have to take a fast corona test and that will be free")
                    case_4 = True
                elif reason_test == "Hotels" and status_vac == "unvaccinated" and age >= 3 and age < 12: #case_5
                    print("You will have to take a PCR test that lasts for 72 hours and that will be free")
                    case_5 = True
                elif reason_test == "Hotels" and status_vac == "unvaccinated" and age >= 12: #case_6
                    print("You will have to take a PCR test that lasts for 72 hours and that won't be free")
                    case_6 = True
        except ValueError:
            case_7 = True
            
        return render_template("home.html", exposed=exposed, case_1=case_1, case_2=case_2, case_3=case_3, case_4=case_4, case_5=case_5, case_6=case_6, case_7=case_7)
     
    return app