# Write your MySQL query statement below
SELECT
  ROUND(
    SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0
    / COUNT(*),
    2
  ) AS immediate_percentage
FROM (
  SELECT *,
         ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date ASC) AS rn
  FROM Delivery
) t
WHERE rn = 1;
