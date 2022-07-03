from io import BytesIO
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote, urlparse, parse_qs
import sqlite3

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        import models 
        import views.client as client_view

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        if ("clients" in self.path):

            import views.all_clients as all_clients_view

            try:
                sqlite_connection = sqlite3.connect('./database/Database.db')
                cursor = sqlite_connection.cursor()
                print("Successfully Connected to SQLite")

                cursor.execute("SELECT * FROM Clients")
                clients = cursor.fetchall()
                cursor.close()

                #for row in result:
                #    for el in row:
                #        print(el, end="\t")
                #    print("")

                result = all_clients_view.render_client(clients)
                result = bytes(result, 'utf-8')
                self.wfile.write(result)

            except sqlite3.Error as err:
                print(err)
                cursor.close()
        
            finally:
                if (sqlite_connection):
                    sqlite_connection.close()

        else:

            c = models.client.Client('Ирина', 'Сорокина', 'vektorinaaa@gmail.com', 'Чамзинка', 431700, 'Пролетарская, 70') 
            result = client_view.render_client(c)
            result = bytes(result, 'utf-8')
            self.wfile.write(result)

    def do_POST(self):

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()

        # Парсим в словарь
        parsed_body = parse_qs(unquote(body.decode('utf-8')))
        print(parsed_body)
        # Индекс сохраняется как строка -> нужно преобрзовать
        parsed_body["index"][0] = int(parsed_body["index"][0])

        # Сохраняем в БД
        try:
            sqlite_connection = sqlite3.connect('./database/Database.db')
            cursor = sqlite_connection.cursor()
            print("Successfully Connected to SQLite")

            sql = """
                INSERT INTO 
                Clients(`firstname`, `lastname`, `email`, `city`, `index`, `address`)
                VALUES (?, ?, ?, ?, ?, ?)
            """

            cursor.execute(sql, (parsed_body["firstname"][0], parsed_body["lastname"][0], parsed_body["email"][0],
                parsed_body["city"][0], parsed_body["index"][0], parsed_body["address"][0]))
            sqlite_connection.commit()
            print("INSERTED")
            cursor.close()

        except sqlite3.Error as err:
            print(err)
            cursor.close()
        
        finally:
            if (sqlite_connection):
                sqlite_connection.close()

        # Отправляем ОК
        self.wfile.write("OK".encode('utf-8'))



httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()