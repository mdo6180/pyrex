from pygls.server import LanguageServer
from lsprotocol.types import InitializeParams, InitializeResult
from lsprotocol import types

import logging


class ExampleLanguageServer(LanguageServer):
    def __init__(self):
        super().__init__('example-server', 'v1.0')

    def initialize(self, params: InitializeParams) -> InitializeResult:
        print(f"Initialized with {params}")
        return super().initialize(params)



server = ExampleLanguageServer()

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def log_to_output(message: str, msg_type: types.MessageType = types.MessageType.Info) -> None:
    server.show_message_log(message, msg_type)


@server.feature(types.INITIALIZE)
def initialized(server: ExampleLanguageServer, params):
	log_to_output(f"Extension initialized")


@server.feature(types.TEXT_DOCUMENT_DID_OPEN)
def did_open(server: ExampleLanguageServer, params):
	log_to_output(f"Text document opened")
	#print(f"Text document opened: {params}", flush=True)


@server.feature(types.TEXT_DOCUMENT_DID_CHANGE)
def did_change(server: ExampleLanguageServer, params):
	log_to_output(f"Text document changed")
	#print(f"Text document changed: {params}", flush=True)



if __name__ == "__main__":
	server.start_io()