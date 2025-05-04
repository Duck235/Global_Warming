from flask import Flask, render_template, request
import random

app = Flask(__name__)

facts_list = ["Парадокс, но если бы парникового эффекта не было, среднегодовая температура воздуха на Земле была бы на 39°С ниже, чем сейчас, т.е. минус 25°С (!)", 
            "За последние сто лет средняя температура Земли увеличилась на 1,2°C.", 
            "2020 год стал одним из самых жарких в истории климата.", 
            "С середины 20 века уровень моря поднялся примерно на 20 сантиметров.",
            "Концентрация углекислого газа в атмосфере достигла рекордного уровня в 2022 году – 417,2 частей на миллион.",
            "За последние 40 лет ледяной покров Арктики сократился примерно на 40%."]
            

@app.route("/random_fact",methods=['GET', 'POST'])
def techdependence():
    random_fact = random.choice(facts_list)
    return render_template('random_fact.html',random_fact=random_fact)

@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/image")
def get_image():
    return f'<img src="https://www.bing.com/images/search?view=detailV2&ccid=8tZ8a1%2bq&id=C527339603E138BD0DF6C3A8FDF7C44A2EB46C43&thid=OIP.8tZ8a1-qHXTFBCRUtWs6TQHaE7&mediaurl=https%3a%2f%2fs.digitalocean.ru%2fupload%2f1639588122_1599pxApple_IIIMG_7064.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.f2d67c6b5faa1d74c5042454b56b3a4d%3frik%3dQ2y0LkrE9%252f2oww%26pid%3dImgRaw%26r%3d0&exph=1065&expw=1599&q=%d0%9a%d0%be%d0%bc%d0%bf%d1%8c%d1%8e%d1%82%d0%b5%d1%80&simid=608056173440747204&FORM=IRPRST&ck=E9FDAF3296B931894C645492E00B46FD&selectedIndex=23&itb=0" alt="Компьютер">'
app.run(debug=True)



