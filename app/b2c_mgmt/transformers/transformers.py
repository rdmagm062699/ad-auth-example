
def emails_transform(item):
    if item[0] == 'emails':
        return ('emails', [email['value'] for email in item[1]])
    return item

def franchises_transform(item):
    if isinstance(item[1], dict) and 'franchises' in item[1]:
        return ('franchises', item[1]['franchises'])
    return item

def name_transform(item):
    if item[0] == 'name':
        return ('name', item[1]['formatted'])
    return item

def groups_transform(item):
    if item[0] == 'groups':
        return ('groups', [group['display'] for group in item[1]])
    return item

class Transformers:
    def __init__(self):
        self.transformers = [emails_transform, franchises_transform, name_transform, groups_transform]

    def transform(self, persons):
        return [self._transform_person(person) for person in persons]

    def _transform_person(self, person):
        attributes = list(person.items())
        for transform in self.transformers:
            attributes = [transform(attribute) for attribute in attributes]
        return dict(attributes)
