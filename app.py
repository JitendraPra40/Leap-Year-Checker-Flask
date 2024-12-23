from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('app.html')

@app.route('/leap', methods=['POST'])
def leap_year():
    year = int(request.form['year'])
    if (year % 400 == 0) and (year % 100 == 0):
        return jsonify({'year' :f"{year} is a leap year"})
    elif (year % 4 == 0) and (year % 100 != 0):
        return jsonify({'year' :f"{year} is a leap year"})
    else:
        return jsonify({'year' :f"{year} is not a leap year"})


if __name__ == "__main__":
    app.run(debug=True)