import socket
import time
from threading import Thread


class UDPClient:
    IP = "127.0.0.1"
    PORT = 20221
    BUFFERSIZE = 1024
    MSG_CLIENT = "Knock, knock I am a new client"

    def __init__(self, ip=IP, port=PORT, bufferSize=BUFFERSIZE):
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize

    def send_message(self, msg=MSG_CLIENT):
        bytesToSend = msg.encode()
        # Create a UDP socket
        client = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Send data to server
        client.sendto(bytesToSend, (self.ip, self.port))
        msgFromServer = client.recvfrom(self.bufferSize)
        return msgFromServer


class GracefulExitException(Exception):
    "Client requested Server shutdown"
    pass


class UDPServer(Thread):
    IP = "127.0.0.1"
    PORT = 0  # Bind to first available port
    BUFFERSIZE = 1024
    BANNER = b"Welcome UDP client"

    def __init__(self, ip=IP, port=PORT, bufferSize=BUFFERSIZE, banner=BANNER):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.bufferSize = bufferSize
        self.banner: bytes = banner
        self.server = None
        self.handlers = [self.log_handler, self.bye_handler]
        self.daemon = True
        self.status = None

    def listen(self):
        # create a datagram socket
        self.server = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to ip address and port
        self.server.bind((self.ip, self.port))
        self.port = self.server.getsockname()[1]
        self.status = "running"
        self.start()
        # self.handlers = [self.log_handler, self.echo_handler]
        # self.handlers = [self.log_handler]
        # self.handlers = [self.echo_handler]
        # self.handlers = [self.banner_handler]
        return self.port

    def message_handler(self, msg_bytes, address):
        try:
            message = b""
            for handler in self.handlers:
                response = handler(msg_bytes, address)
                if response:
                    message += response
            print(message)
            self.send_message(message, address)
        except GracefulExitException:
            pass
        finally:
            self.shutdown()

    def run(self):
        print(f"UDP server up and listening on port {self.port}")
        try:
            while self.status == "running":
                msg, address = self.receive_message()
                handler = Thread(
                    target=self.message_handler,
                    args=(
                        msg,
                        address,
                    ),
                )
                handler.start()
        except OSError:
            pass

    def receive_message(self):
        # Listem for incoming datagram
        bytesAddressPair = self.server.recvfrom(self.bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        return message, address

    def send_message(self, msg_bytes: bytes, address) -> None:
        # Sending a reply to client
        # bytesToSend = message.encode()
        self.server.sendto(msg_bytes, address)

    def log_handler(self, msg_bytes, address) -> None:
        print("From {} message: {}".format(address, msg_bytes))
        return

    def bye_handler(self, msg_bytes, _) -> None:
        if msg_bytes == b"Bye\n":
            print("Graceful exit received")
            raise GracefulExitException("Gracefully exit")

    def banner_handler(self, msg_bytes, _) -> str:
        return self.banner

    def echo_handler(self, msg_bytes: str, _) -> str:
        return msg_bytes

    def shutdown(self):
        self.status = None
        self.server.close()


if __name__ == "__main__":
    server = UDPServer()
    # server.banner = "Who is that"
    server.listen()
    server.handlers.extend([server.echo_handler])
    while server.status:
        time.sleep(1)
