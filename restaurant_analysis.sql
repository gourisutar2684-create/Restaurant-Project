CREATE TABLE restaurants (
    restaurant_id VARCHAR(10),
    area VARCHAR(50),
    cuisine VARCHAR(50),
    food_category VARCHAR(50),
    menu_item VARCHAR(100),
    price NUMERIC(10,2),
    rating NUMERIC(3,1),
    reviews INTEGER,
    offers VARCHAR(10),
    delivery VARCHAR(10),
    website VARCHAR(10),
    online_order VARCHAR(10),
    social_presence VARCHAR(20)
);

INSERT INTO restaurants
(restaurant_id, area, cuisine, food_category, menu_item,
 price, rating, reviews, offers, delivery,
 website, online_order, social_presence)
VALUES
('R001','Area A','Indian','Main Course','Biryani',250,4.4,1250,'Yes','Yes','Yes','Yes','High'),
('R002','Area B','Chinese','Main Course','Noodles',180,4.1,730,'No','Yes','No','No','Medium'),
('R003','Area A','Italian','Pizza','Pizza',320,4.5,980,'Yes','Yes','Yes','Yes','High'),
('R004','Area C','Indian','Snacks','Samosa',80,3.9,450,'No','No','No','No','Low'),
('R005','Area B','Mexican','Main Course','Tacos',220,4.2,620,'Yes','Yes','Yes','Yes','Medium');

SELECT * FROM restaurants;

SELECT COUNT(*) AS total_restaurants
FROM restaurants;

SELECT cuisine, COUNT(*) AS restaurant_count
FROM restaurants
GROUP BY cuisine
ORDER BY restaurant_count DESC;

SELECT ROUND(AVG(price), 2) AS average_price
FROM restaurants;

SELECT ROUND(AVG(rating), 2) AS average_rating
FROM restaurants;

SELECT restaurant_id, cuisine, rating
FROM restaurants
ORDER BY rating DESC;

SELECT area, COUNT(*) AS restaurant_count
FROM restaurants
GROUP BY area
ORDER BY restaurant_count DESC;

SELECT online_order, COUNT(*) AS total
FROM restaurants
GROUP BY online_order;

SELECT delivery, COUNT(*) AS total
FROM restaurants
GROUP BY delivery;

SELECT social_presence, COUNT(*) AS total
FROM restaurants
GROUP BY social_presence;

SELECT cuisine,
       ROUND(AVG(rating), 2) AS average_rating
FROM restaurants
GROUP BY cuisine
ORDER BY average_rating DESC;

SELECT cuisine,
       ROUND(AVG(price), 2) AS average_price
FROM restaurants
GROUP BY cuisine
ORDER BY average_price DESC;

SELECT area,
       ROUND(AVG(price), 2) AS average_price
FROM restaurants
GROUP BY area
ORDER BY average_price DESC;

SELECT restaurant_id, cuisine, rating
FROM restaurants
WHERE rating > 4.0
ORDER BY rating DESC;

SELECT restaurant_id, menu_item, price
FROM restaurants
WHERE price > (
    SELECT AVG(price)
    FROM restaurants
)
ORDER BY price DESC;

SELECT restaurant_id, cuisine, online_order
FROM restaurants
WHERE online_order = 'Yes';

SELECT restaurant_id, area, website, social_presence
FROM restaurants
WHERE website = 'No'
   OR social_presence = 'Low';

SELECT restaurant_id, cuisine, delivery
FROM restaurants
WHERE delivery = 'Yes';

SELECT restaurant_id, reviews
FROM restaurants
ORDER BY reviews DESC;

SELECT restaurant_id, cuisine, offers
FROM restaurants
WHERE offers = 'Yes';

SELECT
    COUNT(*) AS total_restaurants,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(AVG(rating), 2) AS average_rating,
    SUM(reviews) AS total_reviews
FROM restaurants;

SELECT CORR(price, rating) AS price_rating_correlation
FROM restaurants;

SELECT * FROM restaurants;