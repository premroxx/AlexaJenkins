import jenkins
import random


def lambda_handler(event, context):
    server = jenkins.Jenkins('http://54.85.232.121:8080/', username='deloitteadmin', password='')
    server.build_job('deploy_pizza_to_prod_app_server',
                     {'ip_address': '34.198.25.2', 'deploy_db': 'True', 'deploy_backend': 'True',
                      'deploy_frontend': 'True'})
    return handle_session_end_request()


def handle_session_end_request():
    session_attributes = {}
    random_string = ["Skynet is Active",
                     "Hope you know what you are doing",
                     "Lets Party!!"]
    card_title = "Thanks"
    speech_output = "Building App in Production. " + random.choice(random_string)
    print speech_output
    reprompt_text = None
    should_end_session = True
    return build_response(session_attributes,
                          build_speechlet_response(card_title, speech_output, reprompt_text, should_end_session))


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response
    }


if __name__ == '__main__':
    lambda_handler(event=None, context=None)
