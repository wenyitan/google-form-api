class GroupQuestion:

    def __init__(self, counter):
        self.group = {
                "createItem": {
                    "item": {
                        "questionGroupItem": {
                            "questions": [],
                            "grid": {
                                "columns": {
                                    "type": "RADIO",
                                    "options": [
                                        {
                                            "value": "Not Applicable"
                                        },
                                        {
                                            "value": "Strongly Disagree"
                                        },
                                        {
                                            "value": "Disagree"
                                        },
                                        {
                                            "value": "Neutral"
                                        },
                                        {
                                            "value": "Agree"
                                        },
                                        {
                                            "value": "Strongly Agree"
                                        }
                                    ],
                                    "shuffle": False
                                    },
                                "shuffleQuestions": False
                            }
                        }
                    },
                    "location": {
                        "index": counter
                    }
                }
            }
        
    def getGroup(self):
        return self.group
    
    def setTitle(self, title):
        self.group["createItem"]["item"]["title"] = title
    
    def addQuestion(self, questionTitle):
        question = {
            "required": True,
            "rowQuestion": {
                "title": questionTitle.strip().replace("\n", "")
            }
        }
        self.group["createItem"]["item"]["questionGroupItem"]["questions"].append(question)
    
    def getQuestionsLength(self):
        return len(self.group["createItem"]["item"]["questionGroupItem"]["questions"])
    