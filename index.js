'use strict';
var Alexa = require('alexa-sdk');

//=========================================================================================================================================
//Header Variables
//=========================================================================================================================================

var APP_ID = "amzn1.ask.skill.6c2f35b5-87e5-4c37-8c0c-91b6c83d4553";

var SKILL_NAME = "BYU Facts";
var GET_FACT_MESSAGE = "Here's a fact: ";
var HELP_MESSAGE = "You can say tell me a BYU fact, or, you can say stop and I'll stop... What can I help you with?";
var HELP_REPROMPT = "How can I help you?";
var STOP_MESSAGE = "Goodbye!";

//=========================================================================================================================================
//Data with all the facts
//=========================================================================================================================================
var data = [
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
//Careful with these things below
//=========================================================================================================================================
exports.handler = function(event, context, callback) {
    var alexa = Alexa.handler(event, context);
    alexa.APP_ID = APP_ID;
    alexa.registerHandlers(handlers);
    alexa.execute();
};

var handlers = {
    'LaunchRequest': function () {
        this.emit('GetNewFactIntent');
    },
    'GetNewFactIntent': function () {
        var factArr = data;
        var factIndex = Math.floor(Math.random() * factArr.length);
        var randomFact = factArr[factIndex];
        var speechOutput = GET_FACT_MESSAGE + randomFact;
        this.emit(':tellWithCard', speechOutput, SKILL_NAME, randomFact)
    },
    'AMAZON.HelpIntent': function () {
        var speechOutput = HELP_MESSAGE;
        var reprompt = HELP_REPROMPT;
        this.emit(':ask', speechOutput, reprompt);
    },
    'AMAZON.CancelIntent': function () {
        this.emit(':tell', STOP_MESSAGE);
    },
    'AMAZON.StopIntent': function () {
        this.emit(':tell', STOP_MESSAGE);
    }
};
