def test_port_27017_is_listening(Socket):
    socket = Socket("tcp://0.0.0.0:27017")
    assert socket.is_listening

def test_mongodb_server_is_running(Service):
    service = Service("mongod")
    assert service.is_running
    assert service.is_enabled
