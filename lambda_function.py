import json
import os
import requests
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response
from ask_sdk_model.ui import SimpleCard
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# URL de l'endpoint web
WEB_ENDPOINT = os.getenv('WEB_ENDPOINT', 'http://votre-endpoint.com/api')

class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech_text = "Bienvenue. Je peux vous aider à communiquer avec le service web. Que souhaitez-vous dire ?"
        
        return handler_input.response_builder.speak(speech_text).ask(speech_text).response

class DialogIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("DialogIntent")(handler_input)

    def handle(self, handler_input):
        # Récupération du dialogue de l'utilisateur
        slots = handler_input.request_envelope.request.intent.slots
        user_dialog = slots.get("dialog", {}).value

        if not user_dialog:
            speech_text = "Je n'ai pas compris ce que vous avez dit. Pouvez-vous répéter ?"
            return handler_input.response_builder.speak(speech_text).ask(speech_text).response

        try:
            # Envoi du dialogue à l'endpoint web
            response = requests.post(
                WEB_ENDPOINT,
                json={"dialog": user_dialog},
                timeout=5
            )
            response.raise_for_status()
            
            # Récupération de la réponse
            web_response = response.json()
            speech_text = web_response.get("response", "Je n'ai pas reçu de réponse valide du service.")
            
        except Exception as e:
            print(f"Erreur lors de la communication avec l'endpoint: {str(e)}")
            speech_text = "Désolé, quelque chose n'a pas fonctionné. Veuillez réessayer."

        return handler_input.response_builder.speak(speech_text).response

class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speech_text = "Vous pouvez me dire ce que vous souhaitez communiquer au service web. Je transmettrai votre message et vous donnerai la réponse."
        
        return handler_input.response_builder.speak(speech_text).ask(speech_text).response

class CancelAndStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speech_text = "Au revoir !"
        return handler_input.response_builder.speak(speech_text).response

class SessionEndedRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        return handler_input.response_builder.response

class ErrorHandler(AbstractRequestHandler):
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        print(f"Erreur: {str(exception)}")
        speech_text = "Désolé, une erreur s'est produite. Veuillez réessayer."
        
        return handler_input.response_builder.speak(speech_text).ask(speech_text).response

# Création du skill
sb = SkillBuilder()

# Ajout des handlers
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(DialogIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelAndStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(ErrorHandler())

# Handler Lambda
lambda_handler = sb.lambda_handler() 