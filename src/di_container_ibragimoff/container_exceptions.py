class FrozenServiceException(Exception):
    pass


class UnknownIdentifierException(Exception):
    pass


class InvalidServiceIdentifierException(Exception):
    pass


class TagAlreadyRegisteredForTheService(Exception):
    pass
