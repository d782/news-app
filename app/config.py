class Config(object):
    DEBUG=True
    DEVELOPMENT=True
    MONGODB_SETTINGS={
    "db":"app-news",
    "host":"localhost",
    "port":27017,
    "alias":"default"
    }

    JWT_SECRET_KEY="testing"