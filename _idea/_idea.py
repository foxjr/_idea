'''
    This is the start of it all: the _idea.
'''

class _idea:
    def __init__(self, idea=None, intent=None, entity=None, relationship=None):
        if idea and type(idea) == _idea:
            self.idea = idea.synthesize()
        else:
            self.idea = None
        if intent and type(intent) == _idea:
            self.intent = intent.synthesize()
        else:
            self.intent = None
        if entity and type(entity) == _idea:
            self.entity = entity.synthesize()
        else:
            self.entity = None
        if relationship and type(relationship) == _idea:
            self.relationship = relationship.synthesize()
        else:
            self.relationship = None
            
    def synthesize(self):
        print('in base class')
