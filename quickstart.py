from __future__ import print_function

from apiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
from GroupQuestion import GroupQuestion

def makeForm():
    files = ["WayistSurveyQuestionnaire.txt"]
    SCOPES = "https://www.googleapis.com/auth/forms.body"
    DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

    store = file.Storage('token.json')
    creds = None
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)

    form_service = discovery.build('forms', 'v1', http=creds.authorize(
        Http()), discoveryServiceUrl=DISCOVERY_DOC, static_discovery=False)

    # Request body for creating a form
    NEW_FORM = {
        "info": {
            "title": "Project Discipleship Survey",
        }
    }

    # Creates the initial form
    result = form_service.forms().create(body=NEW_FORM).execute()
    print("Form created with id", result["formId"])

    for txtFile in files:
        f = open(txtFile, "r")
        lines = f.readlines()
        counter = 0
        NEW_QUESTION = {
                "requests": [
                {
                    "updateFormInfo": {
                        "info": {
                            "title": "Project Discipleship survey",
                            "description": f"Survey for {txtFile.replace('.txt', '')}",
                            "documentTitle": "GCMC",
                            },
                        "updateMask": "*"
                        }
                }]
            }
        # for line in lines:
            # Request body to add a multiple-choice question
        counter = 0
        groupQuestion = GroupQuestion(counter)
        for line in lines:
            if "Section:" in line:
                if groupQuestion.getQuestionsLength() != 0:
                    NEW_QUESTION["requests"].append(groupQuestion.getGroup())
                    groupQuestion = GroupQuestion(counter)
                groupQuestion.setTitle(line.split(":")[1].strip())
                counter += 1

            else:
                groupQuestion.addQuestion(line.strip())
        NEW_QUESTION["requests"].append(groupQuestion.getGroup())
        pageBreakItem = {
        }

        question_setting = form_service.forms().batchUpdate(formId=result["formId"], body=NEW_QUESTION).execute()
        get_result = form_service.forms().get(formId=result["formId"]).execute()
        print("Form created with uri:", get_result["responderUri"])

        f.close()

makeForm()

# id = "1wHAXgJj6tF3eXS-h8qvKk7ttWWAfL67Bzs9IP7CARPQ"