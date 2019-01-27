

from api import Base,engine
Base.metadata.drop_all(bind=engine)

