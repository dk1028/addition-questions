from flask import Flask, render_template, request
from random import randint
app = Flask(__name__)






correct = []
i = 0
o_cnt, x_cnt = 0,0
@app.route('/', methods=["POST","GET"])
def postTest():
    number1,number2 = randint(0,10),randint(0,100)
    msg = "Start question"
    global correct , i , o_cnt , x_cnt
    correct.append(number1+number2)
    
    get_number = request.form.get('get_number')
    if request.method == "POST":

        if int(get_number) == correct[i]:
            msg = "Correct"
            o_cnt += 1
        else :
            x_cnt -= 1
            msg = "Wrong, the correct answer is %d."%correct[i]
            
        i+=1
    return render_template('index.html'
        , number1=number1 ,number2=number2
        ,msg=msg
        ,o_cnt = o_cnt
        ,x_cnt = x_cnt)


   

if __name__ == "__main__" :
    app.run(host = '127.0.0.1', port = 5000 , debug=True)