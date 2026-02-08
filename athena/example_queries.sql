SELECT * FROM onboarding_db.orders;

SELECT order_status, COUNT(*)
FROM onboarding_db.orders
GROUP BY order_status;
