from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

## security fail for this 
URL_CONNECTION = 'mysql+pymysql://root:12345@localhost/test'

engine = create_engine(URL_CONNECTION)

##autoflush update later after commit
##autocommit make changes automatly without verification
localsession = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()