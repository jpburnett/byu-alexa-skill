[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://raw.githubusercontent.com/jpburnett/byu-facts-alexa-skill/master/LICENSE)
[![Python 3.8.5](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# BYU Facts Alexa Skill

An Alexa Skill that when invoked will give the user a fact about Brigham Young University (BYU). Facts range from the University, it's mascot, buildings on the campus and much more. 

# To Use
Say, "Alexa, open BYU facts and tell me a fact about BYU"


# When deploying code for the Alexa Skill, make sure to do the following 4 steps:

1. ```pip install -r py/requirements.txt -t skill_env```

2. ```cp -r py/* skill_env/```

3. Zip the contents of the skill_env folder. Zip the contents of the folder and NOT the folder itself. If you zip the folder it will not work

4. Upload the .ZIP file to the AWS Lambda console
