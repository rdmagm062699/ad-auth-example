class Transformers:
    def transform(self, persons):
        return [self._transform_person(person) for person in persons]

    def _transform_person(self, person):
        dict = {
            'id': person['id'],
            'login': person['profile']['login'],
            'first_name': person['profile']['firstName'],
            'last_name': person['profile']['lastName'],
            'status': person['status']
        }
        if 'franchises' in person['profile']:
            dict['franchises'] = person['profile']['franchises']
        return dict
