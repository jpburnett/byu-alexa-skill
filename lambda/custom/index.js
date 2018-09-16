/* eslint-disable  func-names */
/* eslint-disable  no-console */

const Alexa = require('ask-sdk-core');

const SKILL_NAME = "BYU Facts";
const GET_FACT_MESSAGE = "Here's a fact: ";
const HELP_MESSAGE = "You can say tell me a BYU fact, or, you can say stop and I'll stop... What can I help you with?";
const HELP_REPROMPT = "How can I help you?";
const STOP_MESSAGE = "Goodbye!";
const FALLBACK_MESSAGE = 'BYU Facts skill can\'t help you with that.  It can help you get a fact about BYU. What can I help you with?';
const FALLBACK_REPROMPT = 'What can I help you with?';

// A list of all the different BYU facts.
const data = [
  "BYU was founded on October 16, 1875 .",
  "BYU won the NCAA Football championship in 1984.",
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
  "BYU is located in the city of Provo, Utah"
];

//=========================================================================================================================================
//Editing anything below this line might break your skill.
//=========================================================================================================================================

const GetNewFactHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'LaunchRequest'
      || (request.type === 'IntentRequest'
        && request.intent.name === 'GetNewFactIntent');
  },
  handle(handlerInput) {
    const randomFact = getRandomItem(data);
    const speechOutput = GET_FACT_MESSAGE + randomFact;

    return handlerInput.responseBuilder
      .speak(speechOutput)
      .withSimpleCard(SKILL_NAME, randomFact)
      .getResponse();
  },
};

const HelpHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && request.intent.name === 'AMAZON.HelpIntent';
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(HELP_MESSAGE)
      .reprompt(HELP_REPROMPT)
      .getResponse();
  },
};

const FallbackHandler = {
  // 2018-May-01: AMAZON.FallackIntent is only currently available in en-US locale.
  // This handler will not be triggered except in that locale, so it can be
  // safely deployed for any locale.
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && request.intent.name === 'AMAZON.FallbackIntent';
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(FALLBACK_MESSAGE)
      .reprompt(FALLBACK_REPROMPT)
      .getResponse();
  },
};

const ExitHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'IntentRequest'
      && (request.intent.name === 'AMAZON.CancelIntent'
        || request.intent.name === 'AMAZON.StopIntent');
  },
  handle(handlerInput) {
    return handlerInput.responseBuilder
      .speak(STOP_MESSAGE)
      .getResponse();
  },
};

const SessionEndedRequestHandler = {
  canHandle(handlerInput) {
    const request = handlerInput.requestEnvelope.request;
    return request.type === 'SessionEndedRequest';
  },
  handle(handlerInput) {
    console.log(`Session ended with reason: ${handlerInput.requestEnvelope.request.reason}`);

    return handlerInput.responseBuilder.getResponse();
  },
};

const ErrorHandler = {
  canHandle() {
    return true;
  },
  handle(handlerInput, error) {
    console.log(`Error handled: ${error.message}`);

    return handlerInput.responseBuilder
      .speak('Sorry, an error occurred.')
      .reprompt('Sorry, an error occurred.')
      .getResponse();
  },
};


//////////////////////////////////////////////////////////////////////////////
// Helper Functions
//////////////////////////////////////////////////////////////////////////////

function getRandomItem(arrayOfItems) {
  // can take an array, or a dictionary
  if (Array.isArray(arrayOfItems)) {
    // the argument is an array []
    let i = 0;
    i = Math.floor(Math.random() * arrayOfItems.length);
    return (arrayOfItems[i]);
  }

  if (typeof arrayOfItems === 'object') {
    // argument is object, treat as dictionary
    const result = {};
    const key = this.getRandomItem(Object.keys(arrayOfItems));
    result[key] = arrayOfItems[key];
    return result;
  }
  // not an array or object, so just return the input
  return arrayOfItems;
};

//////////////////////////////////////////////////////////////////////////////
// Export
//////////////////////////////////////////////////////////////////////////////

const skillBuilder = Alexa.SkillBuilders.custom();

exports.handler = skillBuilder
  .addRequestHandlers(
    GetNewFactHandler,
    HelpHandler,
    ExitHandler,
    FallbackHandler,
    SessionEndedRequestHandler
  )
  .addErrorHandlers(ErrorHandler)
  .lambda();
