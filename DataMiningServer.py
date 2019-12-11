from flask import Flask, request,jsonify, render_template
import CTextSearch as ts
import CNaiveBayes as nb


app = Flask(__name__)

SearchObj = ts.CTextSearch()
FileHandlingObj = SearchObj.getFileReadObj()
naiveObj = nb.CNaivebase()


@app.route('/')
def WelcomeToDataMining():
   return 'Welcome To Data Mining'


@app.route('/search',methods=['GET','POST'])
def searchText():
    if request.method== 'POST':
        req_data = request.form['search']
        print(req_data)
        if 'searchString' in req_data:
            searchQ = req_data['searchString']

        ResultData = SearchQuery(searchQ)
        if ResultData == []:
            ResultData = {"Tweet": ["NA","NA","NA","NA","NA"],
                "description": ["NA", "NA" ,"NA","NA" ,"NA"]}
        if type(ResultData) != str:
      
            return render_template("searched.html", query=req_data, result = ResultData.to_html())
        else:
            return render_template("searched.html", query=req_data, result=ResultData)
    elif request.method == 'GET':
        return render_template("search.html")
    
@app.route('/classification',methods=['GET','POST'])
def classificationdata():
    if request.form == 'POST':
        req_data = request.form['classification']
        print(req_data)
        if 'classification' in req_data:
            searchQ = req_data['classification']

        ResultData = ClassificationT(searchQ)
        if ResultData == []:
            ResultData = {"Tweet": ["NA", "NA", "NA", "NA", "NA"],
                      "Type": ["NA", "NA", "NA", "NA", "NA"]}
        return render_template("classified.html", review=req_data, result=dict(ResultData))
    elif request.method == 'GET':
        return render_template("classify.html") 

def InitialiseSearchObject():
    print("Initialising search Object")
    SearchObj.Read_and_initialise_document()
    print("Initialising term frequency")
    SearchObj.Calculating_Document_frequency()
    print("Search Initialise")

def InitializeClassificationObject():
    print("Initialising Classification Object")
    naiveObj.setFileReadObj(FileHandlingObj)
    naiveObj.Initialize()
    naiveObj.CalculateClassProbability()
    print("Classification Initialise")

def SearchQuery(query):
    print("Inside Search Query Server: DataMiningServer.py")
    return SearchObj.Search(query)

def ClassificationT(query):
    print("Inside ClassificationT Server: DataMiningServer.py")
    PredictedClass = naiveObj.CalculateTermProbablity(query)
    print(PredictedClass)
    return PredictedClass

InitialiseSearchObject()
InitializeClassificationObject()

if __name__ == '__main__':
   app.run()

