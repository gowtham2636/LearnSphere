from flask import Flask,render_template,request
from backend.content.selectvoc import theme_selected_voc
from backend.content.exams import question_for_exams_voc
from dotenv import load_dotenv
import os

app=Flask(__name__)

theme_voc=["Animals","Gardening","Astronomy","Physical description","Family and Friends","Fruits and vegetables","Computer Science","In the house", "Weather", "The human body","Hobbies","Nationality","Science","TOEIC"]
theme_voc_img=["animaux.png","jardinage.png","astronomie.png","descriptionphysique.png","famille.png","legumes.png","informatique.png","maison.png","meteo.png","corpshumain.png","loisirs.png","nationalite.png","la-science.png","toeic.png"]

theme_gram=["Present Simple","Present Continuous","Preterit","Past continuous","Present Perfect","Present Perfect Continuous","Past Perfect","Future Simple","Future Continuous","Modals","Comparative","Superlative"]

theme_culture = ["World War I","World War II","The Vietnam War","Medieval Period","The Cold War","History of USA","History of Britain","The Industrial Age","Ancient Greece"]

app = Flask(__name__)

@app.route("/")
def page_accueil():
    return render_template("accueil/english.html")

@app.route("/culture&history")
def edit2021():
    nb_of_culture_theme = len(theme_culture)
    return render_template("cult/culture.html",theme_culture=theme_culture,nb_of_culture_theme=nb_of_culture_theme)

@app.route("/grammar")
def edit2022():
    nb_of_grammar_theme=len(theme_gram)
    return render_template("gram/grammar.html",theme_gram=theme_gram,nb_of_grammar_theme=nb_of_grammar_theme)

@app.route("/vocabulary")
def editsuivante():
    max_number_of_theme=len(theme_voc)
    return render_template("voc/vocabulary.html",theme_voc=theme_voc,theme_voc_img=theme_voc_img,max_number_of_theme=max_number_of_theme)

@app.route("/train-vocabulary",methods=["GET","POST"])
def card_voc_theme():
    theme_selected = request.args.get("selected_theme")
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    return render_template("voc/stack-voc.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)

@app.route("/train-grammar")
def card_gram_theme():
    theme_selected = request.args.get("selected_theme")
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    if (theme_selected == "Present Simple") :
        return render_template("gram/presentSimple.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Present Continuous") :
        return render_template("gram/presentContinuous.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Preterit") :
        return render_template("gram/preterit.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Past continuous") :
        return render_template("gram/pastContinuous.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Present Perfect") :
        return render_template("gram/presentPerfect.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Present Perfect Continuous") :
        return render_template("gram/presentPerfectContinuous.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Past Perfect") :
        return render_template("gram/pastPerfect.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Future Simple") :
        return render_template("gram/futureSimple.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Future Continuous") :
        return render_template("gram/futureContinuous.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Modals") :
        return render_template("gram/modals.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Comparative") :
        return render_template("gram/comparative.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Superlative") :
        return render_template("gram/superlative.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    else :
        return render_template("errorNotFound.html")

@app.route("/train-culture&history")
def card_cult_theme():
    theme_selected = request.args.get("selected_theme")
    print(theme_selected)
    all_card_theme = theme_selected_voc(theme_selected)
    question = all_card_theme[0]
    answer = all_card_theme[1]
    if (theme_selected == "World War II"):
        return render_template("cult/worldWarII.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "World War I"):
        return render_template("cult/worldWarI.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "The Vietnam War"):
        return render_template("cult/vietnamWar.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Medieval Period"):
        return render_template("cult/medievalPeriod.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "The Cold War"):
        return render_template("cult/coldWar.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "History of USA"):
        return render_template("cult/historyUSA.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "History of Britain"):
        return render_template("cult/historyBritain.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Interwar Period"):
        return render_template("cult/interwarPeriod.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "The Wild West"):
        return render_template("cult/wildWest.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "The Industrial Age"):
        return render_template("cult/industrialAge.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    elif (theme_selected == "Ancient Greece"):
        return render_template("cult/ancientGreece.html",number_of_cards=len(question),question=question,answer=answer,theme_name=theme_selected)
    else :
        return render_template("errorNotFound.html")

@app.route("/exams",methods=["GET","POST"])
def exams():
    listforexams=question_for_exams_voc()
    vocfrenchexams=[]
    vocenglishexams=[]
    for i in range(len(listforexams)):
        vocfrenchexams.append(listforexams[i][0])
        vocenglishexams.append(listforexams[i][1])
    return render_template("exams/exams.html",lenlistforexams=len(listforexams),vocfrenchexams=vocfrenchexams,vocenglishexams=vocenglishexams)

@app.route("/article",methods=["GET","POST"])
def article():
    # Load Environnement from .env file
    load_dotenv()
    apikey = os.getenv('API_KEY')
    return render_template("article/article.html",apikey=apikey)

if __name__=="__main__":
    app.debug=True
    app.run()