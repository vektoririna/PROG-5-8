

def render_client(client)->str:

	from jinja2 import Template 
	

	# template = env.get_template('layout.html')
	

	template = Template('<html><head><title> {{ title }} </title>'
		'<meta charset="utf-8"></head><body>'
		'<form method="POST" action="">'
		'<br>Имя: </br>'
		'<input name="firstname" type="text" value="{{ cl.firstname }}">'
		'<br>Фамилия: </br>'
		'<input name="lastname" type="text" value="{{ cl.lastname }}">'
		'<br>Почта: </br>'
		'<input name="email" type="text" value="{{ cl.email }}">'
		'<br>Город: </br>'
		'<input name="city" type="text" value="{{ cl.city }}">'
		'<br>Индекс: </br>'
		'<input name="index" type="number" value="{{ cl.index }}">'
		'<br>Адрес: </br>'
		'<input name="address" type="text" value="{{ cl.address }}">'
		'</br></br>'
		'<input type="submit">'
		'</form>'
		'</body></html>')
	s = template.render(title="Индексная страница", cl=client)

	# s = f'<html><head><meta charset="utf-8"></head>Hello, {str(client)}</html>'

	return s