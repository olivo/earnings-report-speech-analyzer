import dialogflow
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

class TextAnalyzer:
    def AnalyzeText(self, text):
        client = language.LanguageServiceClient()
        document = types.Document(
            content = text,
            type = enums.Document.Type.PLAIN_TEXT)

        entitiesAnalysis = client.analyze_entities(document=document)
        syntaxAnalysis = client.analyze_syntax(document=document)

        res = dict()
        #res["entitiesAnalysis"] = entitiesAnalysis
        #res["syntaxAnalysis"] = syntaxAnalysis

        # Intent detection
        projectId = "earnings-reports-analysis"
        sessionId = "1"
        sessionClient = dialogflow.SessionsClient()
        session = sessionClient.session_path(projectId, sessionId)
        #print('Session path: {}\n'.format(session))

        textInput = dialogflow.types.TextInput(text=text, language_code='en')

        queryInput = dialogflow.types.QueryInput(text=textInput)

        response = sessionClient.detect_intent(
            session=session, query_input=queryInput
        )

        #res['intent'] = response
        res['text'] = response.query_result.query_text
        parameters = response.query_result.parameters

        for parameter in response.query_result.parameters:
            res[parameter] = response.query_result.parameters[parameter]

        return res