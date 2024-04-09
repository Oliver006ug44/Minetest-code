import socket

# Define host and port
HOST = '192.168.1.129'  # Replace 'your_ip_address' with your actual IP address
PORT = 30000

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Bind the socket to the address and port
        s.bind((HOST, PORT))
        print(f"Server started on {HOST}:{PORT}")

        # Listen for incoming connections
        s.listen()

        # Accept connections and echo back received data
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)
                    print("Received:", data.decode())

if __name__ == "__main__":
    start_server()
