from coapthon.server.coap import CoAP
from coapthon import defines
from coapthon.resources.resource import Resource
from irc5_client import tcp_client


class AdvancedResource(Resource):
    def __init__(self, tcp=None, name="Advanced"):
        super(AdvancedResource, self).__init__(name)
        self.payload = "Advanced resource"
        self.tcp_client = tcp

    def render_POST_advanced(self, request, response):
        self.payload = request.payload
        from coapthon.messages.response import Response
        assert(isinstance(response, Response))
        msg = request.payload
        data = self.tcp_client.talker(msg)
        response.payload = data
        response.code = defines.Codes.VALID.number
        return self, response


class BasicResource(Resource):
    def __init__(self, tcp=None, name="BasicResource", coap_server=None):
        super(BasicResource, self).__init__(name, coap_server, visible=True,
                                            observable=True, allow_children=True)
        self.payload = "Basic Resource"
        self.tcp_client = tcp

    def render_POST(self, request):
        msg = request.payload
        data = self.tcp_client.talker(msg)
        self.payload = data
        return self


class CoAPServer(CoAP):
    def __init__(self, host, port, tcp):
        CoAP.__init__(self, (host, port))

        # Choose AdvancedResource to get the response
        # self.add_resource('draw/', BasicResource(tcp))
        self.add_resource('draw/', AdvancedResource(tcp))


def main():
    # Connect to robot first
    print('Initializing TCP Client')
    tcp = tcp_client()

    # Initialize the server
    print('Initializing CoAP Server')
    server = CoAPServer("127.0.0.1", 5683, tcp)

    try:
        print('CoAP server is running..')
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")


if __name__ == '__main__':
    main()
