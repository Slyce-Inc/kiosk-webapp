from flask import Flask, render_template, flash
from control import ActionButtons
from Naked.toolshed.shell import execute_js, muterun_js


app = Flask(__name__)

app.config['SECRET_KEY'] = '857c97a793ec5f9010971b2e0b4a68bf'


@app.route('/', methods=['GET','POST'])
def LoadPanel():
	form = ActionButtons()
	if form.is_submitted(): 
		if form.event01.data:
			print('event 1 triggered')
			success = execute_js('play.js', ' -i 0.0.0.0 -e ./events/1.evt')
			if success:
				flash('Event 1 sent.')

		elif form.event02.data:
			print('event 2 triggered')
			success = execute_js('play.js', ' -i 0.0.0.0 -e ./events/2.evt')
			if success:
				flash('Event 2 sent.')
		elif form.event03.data:
			print('event 3 triggered')
			success = execute_js('play.js', ' -i 0.0.0.0 -e ./events/3.evt')
			if success:
				flash('Event 3 sent.')
		elif form.event04.data:
			print('event 4 triggered')
			success = execute_js('play.js', ' -i 0.0.0.0 -e ./events/4.evt')
			if success:
				flash('Event 4 sent.')
		elif form.event05.data:
			print('event 5 triggered')
			success = execute_js('play.js', ' -i 0.0.0.0 -e ./events/5.evt')
			if success:
				flash('Event 5 sent.')
		elif form.activate.data:
			success = execute_js('serve.js')
	
		#elif form.deactivate.data:
			#print('Server deactivated...')
		

	return render_template("panel.html", form=form)




if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=8000)