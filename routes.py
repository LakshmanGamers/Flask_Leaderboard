from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

# two decorators, same function
@app.route('/')
@app.route('/base.html')
def index():
    df = pd.read_csv("progress.csv")

    sname = list(df["Student Name"].values)
    es = df["Enrolment Status"].values
    cc = df["# of Courses Completed"].values
    sbc = df["# of Skill Badges Completed"].values

    ls = [sname, es , cc , sbc]
    
    return render_template('base.html', ls=ls)


if __name__ == '__main__':
    app.run(debug=True)
