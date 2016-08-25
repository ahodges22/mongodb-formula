def test_port_27017_is_listening(Socket):
    socket = Socket("tcp://0.0.0.0:27017")
    assert socket.is_listening

def test_mongodb_server_is_running(Service, Pillar):
    service_name = Pillar('mongodb-norepo.sls')['mongodb']['mongod']
    service = Service(service_name)
    assert service.is_running
    assert service.is_enabled
