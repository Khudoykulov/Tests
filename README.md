1. python main.py sample.csv --where "brand=apple"
Result:
name	brand	price	rating
iphone 15 pro	apple	999	4.9

2. python main.py sample.csv --where "price>1000"
Result:
name	brand	price	rating
galaxy s23 ultra	samsung	1199	4.8

3. python main.py sample.csv --where "price<300"
Result:
name	brand	price	rating
redmi note 12	xiaomi	199	4.6
poco x5 pro	xiaomi	299	4.4

4. python main.py sample.csv --where "rating<4.5"
Result:
name	brand	price	rating
poco x5 pro	xiaomi	299	4.4

5. python main.py sample.csv --where "brand=xiaomi"
Result:
name	brand	price	rating
redmi note 12	xiaomi	199	4.6
poco x5 pro	xiaomi	299	4.4