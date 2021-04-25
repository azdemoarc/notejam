from notejam import app
from notejam.configbuild import DevelopmentConfig

app.config.from_object(DevelopmentConfig)

if __name__ == '__main__':
    app.run()
