from flask import Flask, request, render_template_string
import datetime

app = Flask("stats418hello106181188world")

visitor_count = 0

PAGE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello World App</title>
</head>
<body>
    <h1>{{ greeting }}</h1>
    <p>This page has been visited {{ count }} times.</p>
    <form action="/reset" method="post">
        <button type="submit">Reset Counter</button>
    </form>
</body>
</html>
"""

@app.route("/")
def hello():
    global visitor_count
    visitor_count += 1
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 12:
        part_of_day = 'morning'
    elif 12 <= current_hour < 18:
        part_of_day = 'afternoon'
    elif 18 <= current_hour < 21:
        part_of_day = 'evening'
    else:
        part_of_day = 'night'

    greeting = f"Hello World! Good {part_of_day}."
    return render_template_string(PAGE_HTML, greeting=greeting, count=visitor_count)

@app.route("/reset", methods=['POST'])
def reset():
    global visitor_count
    visitor_count = 0
    return "Visit counter has been reset."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
