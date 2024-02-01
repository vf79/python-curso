# callable - funcao(..), obj(..), (lambda)(..)
# environ, start_response
# return iterable


def application(environ, start_response):
    print(environ)

    # montar o response
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    body = b"<strong>WSGI</strong>"
    start_response(status, headers)
    return [body]


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    server = make_server("0.0.0.0", 8000, application)
    server.serve_forever()
