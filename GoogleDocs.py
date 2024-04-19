function createDocWithChatGPTContent() {
    var apiKey = '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';
    var prompt = 'Creáme una entrada que hable sobre IA generativa para un blog de especializado';
    var response = UrlFetchApp.fetch('https://api.openai.com/v1/chat/completions', {
        method: 'post',
        contentType: 'application/json',
        headers: {
            'Authorization': 'Bearer ' + apiKey
        },
        payload: JSON.stringify({
            model: "gpt-3.5-turbo", // Adjust the model name as per the latest available model suitable for chat
            messages: [{
                role: "system",
                content: "Eres un asistente diligente y muy creativo"
            }, {
                role: "user",
                content: prompt
            }]
        }),
        muteHttpExceptions: true
    });

    var content = JSON.parse(response.getContentText());

    if (content.choices && content.choices.length > 0 && content.choices[0].message) {
        var text = content.choices[0].message.content;
        // Create the Document
        var doc = DocumentApp.create('Nombre del fichero');
        var body = doc.getBody();
        body.appendParagraph(text);

        Logger.log('Documento creado con ID: ' + doc.getId());
    } else {
        Logger.log('No se ha generado contenido o ha habido un error');
    }
}
