import io
from urllib.parse import urlencode

def run_wsgi(app, event, context):
    """Convert a Vercel request (event) into a WSGI environ, invoke the
    Django WSGI application, and translate the response back to Vercel format.
    """
    # Build environ dict according to WSGI spec
    environ = {
        "REQUEST_METHOD": event.get("httpMethod", "GET"),
        "SCRIPT_NAME": "",
        "PATH_INFO": event.get("path", "/"),
        "QUERY_STRING": urlencode(event.get("queryStringParameters") or {}),
        "SERVER_NAME": event.get("headers", {}).get("host", "vercel"),
        "SERVER_PORT": "443",
        "SERVER_PROTOCOL": "HTTP/1.1",
        "wsgi.version": (1, 0),
        "wsgi.url_scheme": "https",
        "wsgi.input": io.BytesIO(event.get("body", "").encode()),
        "wsgi.errors": io.StringIO(),
        "wsgi.multithread": False,
        "wsgi.multiprocess": False,
        "wsgi.run_once": False,
    }
    # Add HTTP_ prefixed headers
    for k, v in (event.get("headers") or {}).items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v

    status = []
    response_headers = []

    def start_response(s, h, exc_info=None):
        status.append(s)
        response_headers.extend(h)
        return lambda data: None

    result = app(environ, start_response)
    body = b"".join(result).decode()

    status_code = int(status[0].split()[0]) if status else 200
    headers = {k.lower(): v for k, v in response_headers}
    return {
        "statusCode": status_code,
        "headers": headers,
        "body": body,
    }
