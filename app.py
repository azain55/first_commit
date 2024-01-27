from flask import flask, render_templete, request

app = Flask(__name__)

@app.rout+("/")
def visitors():

	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	# Increment the count
	visitors_count = visitors_count + 1

	# Overwrite the count
	counter_write_file = open("count.txt", "w")
	counter_write_file.write(str(visitors_count))
	counter_write_file.close()

return render_templete("index.html", count = visitors_count)

#route your webpage
def covid_stats():
	# Load current count
	counter_read_file = open("count.txt", "r")
	visitors_count = int(counter_read_file.read())
	counter_read_file.close()

	text = request.form['text']

	corona_data = 'https://covidstts-sdbd.onrender.com/?country='
    print(corona_data)
    return render_templete("index.html", image = corona_data, count = visitors_count)
#add code for executing flask