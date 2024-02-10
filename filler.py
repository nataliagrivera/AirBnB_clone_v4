#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.review import Review

# creation of a State
state_1 = State(name="Miami")
state_1.save()
state_2 = State(name="Puerto Rico")
state_2.save()

# creation of a City
city_1 = City(state_id=state_1.id, name="Fort Lauderdale")
city_1.save()
city_2 = City(state_id=state_2.id, name="San Juan")
city_2.save()

# creation of a User with email and password
#home Owners
user_1 = User(email="hector@example.com", password="hectorpwd", first_name="Hector", last_name="Rodriguez")
user_1.save()
user_2 = User(email="christian@example.com", password="christianpwd", first_name="Christian", last_name="Rosario")
user_2.save()
user_3 = User(email="lexi@example.com", password="lexipwd", first_name="Lexi", last_name="Lafargue")
user_3.save()

#Guest 

user_santos = User(email="santos.martinez@example.com", password="santos123", first_name="Santos", last_name="Martínez")
user_santos.save()
user_marquito = User(email="marquito.sepulveda@example.com", password="marquito123", first_name="Marquito", last_name="Sepúlveda")
user_marquito.save()
user_bryan = User(email="bryan.rivera@example.com", password="bryan123", first_name="Bryan", last_name="Rivera")
user_bryan.save()
user_kenneth = User(email="kenneth.navedo@example.com", password="kenneth123", first_name="Kenneth", last_name="Navedo")
user_kenneth.save()
user_canito = User(email="canito.loco@example.com", password="canito123", first_name="Canito", last_name="Loco")
user_canito.save()
user_steven = User(email="steven.rodriguez@example.com", password="steven123", first_name="Steven", last_name="Rodriguez")
user_steven.save()

# creation of 2 Places with additional attributes
place_3 = Place(user_id=user_1.id, city_id=city_2.id, name="Mountain House",
                description="A cozy house nestled in the mountains, in a quiet neighborhood.<br> \
Offers amenities including WiFi, cable TV, internet, HVAC, and parking for 10 vehicles.", 
                number_rooms=6, number_bathrooms=2, max_guest=8, price_by_night=500, 
                latitude=37.7749, longitude=-122.4194)
place_3.save()

place_2 = Place(user_id=user_2.id, city_id=city_2.id, name="Big White House",
                description="Modern, beautiful white house in a quiet neighborhood.<br> \
Features include a small basketball court nearby, WiFi, cable TV, and internet access.", 
                number_rooms=3, number_bathrooms=2, max_guest=3, price_by_night=600, 
                latitude=37.7749, longitude=-122.4194)
place_2.save()

place_1 = Place(user_id=user_3.id, city_id=city_1.id, name="Beachfront Studio",
                description="Studio with a stunning beach view, offering WiFi, cable TV, and modern amenities.", 
                number_rooms=1, number_bathrooms=1, max_guest=2, price_by_night=150, 
                latitude=18.4655, longitude=-66.1057)
place_1.save()



# creation of 3 various Amenity
amenity_1 = Amenity(name="Wifi")
amenity_1.save()
amenity_2 = Amenity(name="Cable Tv")
amenity_2.save()
amenity_3 = Amenity(name="Internet")
amenity_3.save()
amenity_4 = Amenity(name="HVAC")
amenity_4.save()
amenity_5 = Amenity(name="Parcking")
amenity_5.save()
amenity_6 = Amenity(name="Dildo")
amenity_6.save()

# Create reviews for places
review_1 = Review(place_id=place_3.id, user_id=user_kenneth.id, text="Lovely place, had a great time!")
review_1.save()

review_2 = Review(place_id=place_2.id, user_id=user_canito.id, text="The house is beautiful and well-located.\
                   Ugly Loud dog")
review_2.save()

review_3 = Review(place_id=place_1.id, user_id=user_bryan.id, text="Perfect for a weekend getaway.\
                   Wonderful view!")
review_3.save()

review_4 = Review(place_id=place_3.id, user_id=user_marquito.id, text="it has a crazy from neighbor")
review_4.save()

review_5 = Review(place_id=place_2.id, user_id=user_santos.id, text="Ugly Loud dog")
review_5.save()

review_6 = Review(place_id=place_1.id, user_id=user_steven.id, text="Disgusting Dildo was used when arraived it\
                  had a horrible taste and odor.... still used it had needs")
review_6.save()

# link place_1 with 2 amenities
place_1.amenities.append(amenity_1)
place_1.amenities.append(amenity_2)
place_1.amenities.append(amenity_6)

# link place_2 with 3 amenities
place_2.amenities.append(amenity_1)
place_2.amenities.append(amenity_2)
place_2.amenities.append(amenity_3)

# link place_3 with 6 amenities
place_3.amenities.append(amenity_1)
place_3.amenities.append(amenity_2)
place_3.amenities.append(amenity_3)
place_3.amenities.append(amenity_4)
place_3.amenities.append(amenity_5)

storage.save()

print("OK")