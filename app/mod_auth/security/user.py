class User:
    def __init__(self, data):
        self.__data = data

    def is_authenticated(self):
        return self.__access_token is not None

    def is_active(self):
        return is_authenticated()

    def is_anonymous(self):
        return is_authenticated()

    def get_id(self):
        return self.__data['id']

    def data(self):
        return self.__data

    def franchises(self):
        # Franchise number is currently mangled across multiple definitions
        # you first must understand that we have an archaic local Active Directory
        # Instance that is synchronized to two Azure Active Directory tenants.
        #
        # Azure Active Directory does not expose the same fields as the local Active
        # Directory instance.
        # The fields in the local Active Directory that expose Franchise Number are:
        #   1) Company: Stores the primary franchise associated to the individual
        #   2) extensionAttribute5: Contains a comma separated list of franchise numbers
        #   3) physicalDeliveryOfficeName: Another representation of primary franchise number
        #
        # In Azure Active Directory there have been many changes to the representation
        # of a user.  There is a synchronization tool that handles the mapping from
        # Local Active Directory and Azure Active Directory.  I am un sure of how
        # this mapping equates.  At the end of the day all that you can get from either
        # the Microsoft Graph API (latest way to get to Azure Active Directory) or
        # Azure Graph API (the older way to get to Azure Active Directory) is a single field:
        #   * companyName: I believe this is the same as the Company field declared in
        #                  Local Active Directory.
        #
        # I believe we need to thoughtfully decide how we want to represent what
        # franchises an individual is associated to that supports the direction our
        # tech stack is going.
        #
        # For this spike I am always returning a FranchiseNumber.  Real code should not do this.
        pretendFranchises = ['100']
        primaryFranchise = self.__data['companyName']
        if primaryFranchise:
            return [primaryFranchise]
        return pretendFranchises
