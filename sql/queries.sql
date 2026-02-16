-- Total Revenue
SELECT SUM(price * quantity) AS total_revenue FROM sales;

-- Revenue by Category
SELECT category,
       SUM(price * quantity) AS revenue
FROM sales
GROUP BY category;

-- Top Selling Products
SELECT product,
       SUM(quantity) AS units_sold
FROM sales
GROUP BY product
ORDER BY units_sold DESC;

-- Regional Revenue
SELECT region,
       SUM(price * quantity) AS revenue
FROM sales
GROUP BY region;
