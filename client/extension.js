// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
const vscode = require('vscode');

const path = require('path');

// Import the language client, which is the module that communicates with the language server
const { LanguageClient, LanguageClientOptions, ServerOptions, TransportKind } = require('vscode-languageclient/node');


// this method is called when your extension is activated
// your extension is activated the very first time the command is executed

let client;

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
    // The server is implemented in Python
    // let serverModule = context.asAbsolutePath(path.join('server', 'server.py'));
    let serverModule = ''

    // The debug options for the server
    // --inspect=6009: runs the server in Node's Inspector mode so VS Code can attach to the server for debugging
    let debugOptions = { execArgv: ['--nolazy', '--inspect=6009'] };

    let serverOptions = {
        command: 'python',
        args: [serverModule],
    };

    let clientOptions = {
        documentSelector: [{ scheme: 'file', language: 'plaintext' }],
        synchronize: {
            fileEvents: vscode.workspace.createFileSystemWatcher('**/.clientrc'),
        },
    };

    client = new LanguageClient(
        'exampleLanguageServer',
        'Example Language Server',
        serverOptions,
        clientOptions
    );

    client.start();

	// Use the console to output diagnostic information (console.log) and errors (console.error)
	// This line of code will only be executed once when your extension is activated
	console.log('Congratulations, your extension "helloworld-minimal-sample" is now active!');

	// The command has been defined in the package.json file
	// Now provide the implementation of the command with  registerCommand
	// The commandId parameter must match the command field in package.json
	let disposable = vscode.commands.registerCommand('extension.helloWorld', () => {
		// The code you place here will be executed every time your command is executed

		// Display a message box to the user
		vscode.window.showInformationMessage('Hello World Bitch!');
	});

	context.subscriptions.push(disposable);
}

// this method is called when your extension is deactivated
function deactivate() {
    if (!client) {
        return undefined;
    }
    return client.stop();
}

// eslint-disable-next-line no-undef
module.exports = {
	activate,
	deactivate
}