from Bot import TheRealGearBot
from Util import Configuration, GearbotLogging, Emoji, Pages, Utils, Translator, Converters, Permissioncheckers, \
    VersionInfo, Confirmation, HelpGenerator, InfractionUtils, Archive, DocUtils, JumboGenerator, MessageUtils, Enums, \
    Matchers, Questions
from database import DatabaseConnector

components = [
    Configuration,
    DatabaseConnector,
    GearbotLogging,
    Permissioncheckers,
    Utils,
    VersionInfo,
    Emoji,
    Confirmation,
    HelpGenerator,
    Pages,
    InfractionUtils,
    Archive,
    Translator,
    DocUtils,
    JumboGenerator,
    MessageUtils,
    TheRealGearBot,
    Converters,
    Enums,
    Matchers,
    Questions
]
