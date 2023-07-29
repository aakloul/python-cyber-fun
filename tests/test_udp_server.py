import pytest
import random
import string
from networking.udp_server import UDPClient, UDPServer


@pytest.fixture
def server():
    server = UDPServer()
    yield server
    server.shutdown()  # tearDown


@pytest.fixture
def random_string():
    return "".join(random.choices(population=string.ascii_letters, k=10))


def test_default_banner(server: UDPServer):
    server.listen()
    server.handlers = [server.banner_handler]
    client = UDPClient(port=server.port)
    response, address = client.send_message(msg="random message")
    assert response == server.banner
    assert address[0] == server.ip
    assert address[1] == server.port


def test_echo_banner(server: UDPServer, random_string):
    server.handlers = [server.echo_handler]
    server.listen()
    client = UDPClient(port=server.port)
    response, _ = client.send_message(random_string)
    assert response.decode() == random_string


def test_custom_banner(server: UDPServer, random_string):
    server.banner = random_string.encode()
    server.handlers = [server.banner_handler]
    server.listen()
    client = UDPClient(port=server.port)
    response, _ = client.send_message()
    assert response.decode() == random_string


def test_custom_handler(server: UDPServer, random_string):
    def custom_handler(msg_bytes, _):
        return random_string.encode()

    server.handlers = [custom_handler]
    server.listen()
    client = UDPClient(port=server.port)
    response, _ = client.send_message()
    assert response.decode() == random_string


def test_custom_echo(server: UDPServer):
    random_message = "".join(random.choices(population=string.ascii_letters, k=10))

    def custom_handler(msg_bytes, _):
        return msg_bytes

    server.handlers = [custom_handler]
    server.listen()
    client = UDPClient(port=server.port)
    response, _ = client.send_message(random_message)
    assert response.decode() == random_message
