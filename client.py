import http.client

connection = http.client.HTTPConnection('www.python.org', 80, timeout=10)
print(connection)
