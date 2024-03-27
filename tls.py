
import ssl
import socket

server_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
server_context.load_cert_chain(certfile="server_cert.pem", keyfile="server_key.pem")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as server_socket:
    server_socket.bind(('localhost', 443))
    server_socket.listen(5)
    print("Server listening...")

    while True:
        conn, addr = server_socket.accept()
        with conn:
            with server_context.wrap_socket(conn, server_side=True) as secure_socket:
                print("Connection secured with:", addr)
                data = secure_socket.recv(1024)
                print("Received:", data.decode())
                secure_socket.sendall(b"Message received!")

client_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
with socket.create_connection(('localhost', 443)) as client_socket:
    with client_context.wrap_socket(client_socket, server_hostname='localhost') as secure_socket:
        secure_socket.sendall(b"Hello, server!")
        data = secure_socket.recv(1024)
        print("Server response:", data.decode())
