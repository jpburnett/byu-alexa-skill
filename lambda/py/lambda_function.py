"""Simple App providing Facts about BYU"""

import random
import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import (
    AbstractRequestHandler, AbstractExceptionHandler,
    AbstractRequestInterceptor, AbstractResponseInterceptor)
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response


# ===============================================================================================
# Skill Data
# ===============================================================================================

SKILL_NAME = "BYU Facts"
GET_FACT_MESSAGE = "Here's a fact: "
HELP_MESSAGE = "You can say tell me a BYU fact, or, you can say stop and I'll stop... What can I help you with?"
HELP_REPROMPT = "How can I help you?"
STOP_MESSAGE = "Goodbye!"
FALLBACK_MESSAGE = "BYU Facts skill can\'t help you with that.  It can help you get a fact about BYU. What can I help you with?"
FALLBACK_REPROMPT = "What can I help you with?"
EXCEPTION_MESSAGE = "Sorry. I cannot help you with that."

# ===============================================================================================
# Facts
# ===============================================================================================

data = [
  'BYU was founded on October 16, 1875 .',
  'BYU won the NCAA Football championship in 1984.',
  "65% of BYU students have lived outside of the United States.",
  "68% of BYU students speak a second language.",
  "There are 126 different languages spoken on BYU Campus.",
  "BYU's mascot is Cosmo the Cougar.",
  "Cosmo the Cougar recieved his name because BYU was considered to be very Cosmopolitan.",
  "Cosmo the Cougar has his own personal van called the Cosmobile.",
  "BYU is the largest religious University in the United States.",
  "BYU is the largest private University in the United States.",
  "BYU's rival school is the University of Utah located in Salt Lake City.",
  "BYU has a total of 10 NCAA Championships.",
  "Ty Detmer, a heisman trophy winner, is a BYU Alumni.",
  "BYU's has 33,363 students enrolled (as of 2016).",
  "BYU is owned and ran by the Church of Jesus Christ of Latter Day Saints.",
  "BYU offers nearly 200 different majors to students in a variety of areas, fields, and specialties.",
  "The most popular major at BYU is Exercise Science.",
  "BYU is part of the West Coast Conference for most sports, besides football, which is independent.",
  "In 1924 BYU owned two cougars that were on the sidelines of every football game.",
  "52% of BYU students are male, 48% are female.",
  "BYU is ranked as the number 1 stone cold sober campus!",
  "25% of BYU undergraduates are married.",
  "The Spencer W. Kimball Tower is the tallest building on campus, it is also the tallest building in Provo!",
  "The Joseph Smith Religion Building is the only building on campus with a baptismal font.",
  "BYU is located in the city of Provo, Utah",
  "Nearly 50% of all students have lived outside the United States",
  "There are 63 different languages ranging from Arabic to Welsh taught on campus",
  "There is a giant Po the Panda statue stands in the lobby of the Talmage Building"
]

# ===============================================================================================
# Actual Functions
# ===============================================================================================

sb = SkillBuilder()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


# Built-in Intent Handlers
class GetNewFactHandler(AbstractRequestHandler):
    """Handler for Skill Launch and GetNewFact Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_request_type("LaunchRequest")(handler_input) or
                is_intent_name("GetNewFactIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In GetNewFactHandler")

        random_fact = random.choice(data)
        speech = GET_FACT_MESSAGE + random_fact

        handler_input.response_builder.speak(speech).set_card(
            SimpleCard(SKILL_NAME, random_fact))
        return handler_input.response_builder.response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HelpIntentHandler")

        handler_input.response_builder.speak(HELP_MESSAGE).ask(
            HELP_REPROMPT).set_card(SimpleCard(
                SKILL_NAME, HELP_MESSAGE))
        return handler_input.response_builder.response


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (is_intent_name("AMAZON.CancelIntent")(handler_input) or
                is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In CancelOrStopIntentHandler")

        handler_input.response_builder.speak(STOP_MESSAGE)
        return handler_input.response_builder.response

class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for Repeat Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RepeatIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]

        attr = handler_input.attributes_manager.session_attributes
        handler_input.response_builder.speak(
            attr['speech']).ask(
            attr['reprompt'])
        return handler_input.response_builder.response


class FallbackIntentHandler(AbstractRequestHandler):
    """Handler for Fallback Intent.
    AMAZON.FallbackIntent is only available in en-US locale.
    This handler will not be triggered except in that locale,
    so it is safe to deploy on any locale.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")

        handler_input.response_builder.speak(FALLBACK_MESSAGE).ask(
            FALLBACK_REPROMPT)
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In SessionEndedRequestHandler")

        logger.info("Session ended reason: {}".format(
            handler_input.request_envelope.request.reason))
        return handler_input.response_builder.response


# Exception Handler
class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.info("In CatchAllExceptionHandler")
        logger.error(exception, exc_info=True)

        handler_input.response_builder.speak(EXCEPTION_MESSAGE).ask(
            HELP_REPROMPT)

        return handler_input.response_builder.response

class YesIntentHandler(AbstractRequestHandler):
    """Handler for the YesIntent."""
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.YesIntent")(handler_input)

    def handle(self, handler_input):
        logger.debug("In YesIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        session_attr = handler_input.attributes_manager.session_attributes

        #Get what the previous intent was
        prev_intent = session_attr.get("PREV_INTENT")

        if prev_intent == "LaunchIntent":
            speech = data.HELP_MESSAGE
            reprompt = data.FALLBACK_MESSAGE

            handler_input.response_builder.speak(speech) \
            .set_should_end_session(False).ask(reprompt)
            return handler_input.response_builder.response

        if (prev_intent == "RecipeIntent"
            or prev_intent == "RandomItemIntent"
            or prev_intent == "AMAZON.YesIntent"
            or prev_intent == "AMAZON.NoIntent"):
            speech = data.HELP_MESSAGE
            reprompt = data.FALLBACK_MESSAGE

            handler_input.response_builder.speak(speech) \
            .set_should_end_session(False).ask(reprompt)
            return handler_input.response_builder.response

class NoIntentHandler(AbstractRequestHandler):
    """Handler for the NoIntent. Sometimes its okay to say no"""
    def can_handle(self, handler_input):
        return is_intent_name("AMAZON.NoIntent")(handler_input)

    def handle(self, handler_input):
        logger.debug("In NoIntentHandler")
        _ = handler_input.attributes_manager.request_attributes["_"]
        
        speech = data.STOP_MESSAGE
        handler_input.response_builder.speak(_(speech))
            .set_should_end_session(True)

        return handler_input.response_builder.response

class LocalizationInterceptor(AbstractRequestInterceptor):
    """Add function to request attributes, that can load locale specific data."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        locale = handler_input.request_envelope.request.locale
        logger.info("Locale is {}".format(locale))
        i18n = gettext.translation(
            'data', localedir='locales', languages=[locale], fallback=True)
        handler_input.attributes_manager.request_attributes["_"] = i18n.gettext

# Request and Response loggers
class RequestLogger(AbstractRequestInterceptor):
    """Log the alexa requests."""
    def process(self, handler_input):
        # type: (HandlerInput) -> None
        logger.debug("Alexa Request: {}".format(
            handler_input.request_envelope.request))


class ResponseLogger(AbstractResponseInterceptor):
    """Log the alexa responses."""
    def process(self, handler_input, response):
        # type: (HandlerInput, Response) -> None
        logger.debug("Alexa Response: {}".format(response))


# Register intent handlers
sb.add_request_handler(GetNewFactHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(LocalizationInterceptor())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(NoIntentHandler())
sb.add_request_handler(YesIntentHandler())
sb.add_request_handler(RepeatIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

# Register exception handlers
sb.add_exception_handler(CatchAllExceptionHandler())

# TODO: Uncomment the following lines of code for request, response logs.
# sb.add_global_request_interceptor(RequestLogger())
# sb.add_global_response_interceptor(ResponseLogger())

# Handler name that is used on AWS lambda
lambda_handler = sb.lambda_handler()