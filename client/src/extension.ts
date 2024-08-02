// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as path from 'path';
import * as util from 'util';
import { workspace, commands, window, ExtensionContext, LogOutputChannel } from 'vscode';

import {
	LanguageClient,
	LanguageClientOptions,
	ServerOptions,
	TransportKind
} from 'vscode-languageclient/node';

let client: LanguageClient;

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: ExtensionContext) {
	// The server is implemented in node
	const serverModule = "/Users/minhquando/Desktop/pyrex/server/server.py";

	const serverOptions: ServerOptions = {
		command: '/Users/minhquando/Desktop/pyrex/lsp-env/bin/python', // Replace with your own command.
		args: [serverModule],
	};

	const clientOptions: LanguageClientOptions = {
        documentSelector: [
			{ scheme: 'file', language: 'plaintext' },
			{ scheme: 'file', language: 'python' }
		],
        synchronize: {
            fileEvents: workspace.createFileSystemWatcher('**/*.py'),
        },
    };

	client = new LanguageClient(
        'exampleLanguageServer',
        'Example Language Server',
        serverOptions,
        clientOptions
    );

    client.start();
	
	// The command has been defined in the package.json file
	// Now provide the implementation of the command with registerCommand
	// The commandId parameter must match the command field in package.json
	const disposable = commands.registerCommand('extension.helloWorld', () => {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		window.showInformationMessage('Hello World!');
	});

	context.subscriptions.push(disposable);

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "helloworld-sample" is now active!');
}

export function deactivate(): Thenable<void> | undefined {
	if (!client) {
		return undefined;
	}
	return client.stop();
}