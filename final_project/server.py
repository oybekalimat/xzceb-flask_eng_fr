from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from translator import Translator
import json

load_dotenv()

app = Flask("Web Translator")
translator = Translator()


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    result = translator.englishToFrench(textToTranslate)

    return jsonify(result)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    result = translator.frenchToEnglish(textToTranslate)
    return jsonify(result)


@app.route("/")
def renderIndexPage():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
