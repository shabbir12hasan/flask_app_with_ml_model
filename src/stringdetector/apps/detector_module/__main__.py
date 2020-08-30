from detector_app import StringDetector
from flask import Flask


app = Flask(__name__)
main_app = StringDetector()


@app.route('/')
def main():
    print("main file")
    return main_app.run()

if __name__=="__main__":
    main()


# set pythonpath="C:\Users\Hasan\Documents\Personal_Git\Flask API\StringDetector\src"