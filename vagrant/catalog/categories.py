from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup1 import User, Categories, Items, Base

engine = create_engine('sqlite:///sportingequipment.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="Shawon Dunston", email="shawon@cubs.com")
session.add(User1)
session.commit()


# Category for Soccer
category1 = Categories(user_id=1, name="Soccer")
session.add(category1)
session.commit()

#items for soccer
item1 = Items(user_id=1, title="Nike Pitch Training Soccer Ball",
description="""Built for intense training sessions and improving your footwork, the Nike Pitch Training Soccer Ball features a butyl bladder that ensures consistent shape retention and enhanced protection against tears and abrasions. Durable and smooth casing delivers long-lasting performance that resists tears and abrasions 12-panel design offers durability and true flight. Butyl bladder ensures consistent shape retention for responsive, powerful touches. High contrast graphics allow enhanced visibility to predict trajectory with ease.""", categories=category1)
session.add(item1)
session.commit()

item2 = Items(user_id=1, title="adidas Youth Ghost Soccer Shin Guards",
description="Built to ensure full ankle support and coverage when your player battles for possession on the pitch, the adidas Youth Ghost Soccer Shin Guards are a great option for any position while offering a seamless, comfortable fit throughout each match.", categories=category1)
session.add(item2)
session.commit()

# Category for Football
category2 = Categories(user_id=1, name="Football")
session.add(category2)
session.commit()

#items for Football
item3 = Items(user_id=1, title="Riddell Speedflex Helmet",
description="""The goal was to design a helmet with fully integrated components and innovations for peak athlete performance and state-of-the-art protection. We looked at the players' wants and needs at all levels of competition. The result: The Riddell SpeedFlex. Backed by extensive research, including our 2+ million data points of on-field impacts, the SpeedFlex introduces many technical features that are new to the field.""", categories=category2)
session.add(item3)
session.commit()

item4 = Items(user_id=1, title="Champro AMT 1000 Pads",
description="Low-profile cantilever pad construction. Built-in clavicle pads for added protection. Padded epaulet. Integrated deltoid pads.", categories=category2)
session.add(item4)
session.commit()

print "added categories and items!"
