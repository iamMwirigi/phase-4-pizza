from app import app, db
from models import Restaurant, Pizza, RestaurantPizza
from faker import Faker

fake = Faker()

def seed_data():
    with app.app_context():
        db.create_all()

        # Create Restaurants
        restaurants = []
        for _ in range(5):
            restaurant = Restaurant(name=fake.company(), address=fake.address())
            restaurants.append(restaurant)
            db.session.add(restaurant)
        db.session.commit()

        # Create Pizzas and RestaurantPizzas
        for restaurant in restaurants:
            for _ in range(3):
                pizza = Pizza(name=fake.word(), ingredients=fake.word(), restaurant=restaurant)
                db.session.add(pizza)
                db.session.commit()
                restaurant_pizza = RestaurantPizza(restaurant=restaurant, pizza=pizza, price=fake.random_int(min=5, max=20))
                db.session.add(restaurant_pizza)
        db.session.commit()

if __name__ == '__main__':
    seed_data()