(
  SELECT name AS results
  FROM Users
  WHERE user_id IN (
    SELECT user_id FROM (
      SELECT user_id, COUNT(*) AS cnt
      FROM MovieRating
      GROUP BY user_id
    ) AS t
    WHERE cnt = (
      SELECT MAX(cnt) FROM (
        SELECT COUNT(*) AS cnt
        FROM MovieRating
        GROUP BY user_id
      ) AS s
    )
  )
  ORDER BY name
  LIMIT 1
)
UNION ALL
(
  SELECT title AS results
  FROM Movies
  WHERE movie_id IN (
    SELECT movie_id FROM (
      SELECT movie_id, AVG(rating) AS avg_r
      FROM MovieRating
      WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
      GROUP BY movie_id
    ) AS t
    WHERE avg_r = (
      SELECT MAX(avg_r) FROM (
        SELECT AVG(rating) AS avg_r
        FROM MovieRating
        WHERE created_at BETWEEN '2020-02-01' AND '2020-02-29'
        GROUP BY movie_id
      ) AS s
    )
  )
  ORDER BY title
  LIMIT 1
);
