

def render_client(clients):

	from jinja2 import Template 
	

	# template = env.get_template('layout.html')
	

	template = Template(
        '<html><head><title> {{ title }} </title>'
            '<meta charset="utf-8"></head><body>'
            '<table border = "0" cellspacing = 30">'
            '{% for row in cls %}'
                '<tr>'
                '{% for el in row %}'
                    '<td> {{ el }} </td>'
                '{% endfor %}'
                '</tr>'
            '{% endfor %}'
            '</table>'
		'</body></html>')
	s = template.render(title="Зарегистрированные пользователи", cls=clients)

	# s = f'<html><head><meta charset="utf-8"></head>Hello, {str(client)}</html>'

	return s