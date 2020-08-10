from flask import Flask,jsonify
app=Flask(__name__)




courses=[{'name':"Course on APIs",'course_id':"0",'Description': "API development using Python witH Flask framework ",'price':"$100"},
         {'name':"Automation Testing using Python and Selenium",'course_id':"1",'Description':"Learn more on Selenium Automation Testing using Python with PyTest and UnitTest framework",'price':"$200"},
         {'name':"AWS Solutions Architect Certification",'course_id':"2",'Description':"AWS Cloud Training",'price':"$200"}]



@app.route('/')
def index():
    return "We are in Reshma's course on API"

@app.route("/courses",methods=['GET'])
def get():
    return jsonify({'Courses':courses})

@app.route("/courses/<int:course_id>",methods=['GET'])
def get_course(course_id):
    return jsonify({'course':courses[course_id]})

@app.route("/courses",methods=['POST'])
def create():
    course={
        'name': "AWS Developer Certification",'course_id': "3",'Description': "AWS Cloud Training",
        'price': "$200"
    }

    courses.append(course)
    return jsonify({'Created':courses})

@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description']="AWS Certification Bundle"
    return jsonify({'course':courses[course_id]})

@app.route("/courses/<int:course_id>",methods=['DELETE'])
def course_delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result':True})


if __name__=="__main__":
    app.run(debug=True)





