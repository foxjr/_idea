'''
    This is the start of it all: the _idea.
'''

class _idea:
    def __init__(self, idea=None, intent=None, entity=None, relationship=None):
        self.idea = idea.synthesize() if type(idea) == _idea else None
        self.intent = intent.synthesize() if type(intent) == _idea else None
        self.entity = entity.synthesize() if type(entity) == _idea else None
        self.relationship = relationship if type(relationship) == _idea else None

    def synthesize():
        pass
    
        
