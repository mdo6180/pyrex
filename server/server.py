from pygls.server import LanguageServer
from lsprotocol.types import InitializeParams, InitializeResult



class ExampleLanguageServer(LanguageServer):
    def __init__(self):
        super().__init__('example-server', 'v1.0')

    def initialize(self, params: InitializeParams) -> InitializeResult:
        print(f"Initialized with {params}")
        return super().initialize(params)



server = ExampleLanguageServer()



@server.feature("textDocument/didOpen")
def did_open(server: ExampleLanguageServer, params):
    print(f"Text document opened: {params}")


@server.feature("textDocument/didChange")
def did_change(server: ExampleLanguageServer, params):
    print(f"Text document changed: {params}")



if __name__ == "__main__":
    server.start_io()