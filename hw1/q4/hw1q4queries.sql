SELECT 
  Date,
  (COALESCE(S1, 0) + COALESCE(S2, 0) + COALESCE(S3, 0) + COALESCE(S4, 0) +
  COALESCE(S5, 0) + COALESCE(S6, 0) + COALESCE(S7, 0) + COALESCE(S8, 0) +
  COALESCE(S9, 0) + COALESCE(S10, 0)) AS TotalSales
FROM p2
WHERE strftime('%w', substr(Date, 7, 4) || '-' || substr(Date, 1, 2) || '-' || substr(Date, 4, 2)) = '0';

SELECT 
  Date,
  (COALESCE(S1, 0) + COALESCE(S2, 0) + COALESCE(S3, 0) + COALESCE(S4, 0) +
  COALESCE(S5, 0) + COALESCE(S6, 0) + COALESCE(S7, 0) + COALESCE(S8, 0) +
  COALESCE(S9, 0) + COALESCE(S10, 0)) AS TotalSales
FROM p2
WHERE strftime('%w', substr(Date, 7, 4) || '-' || substr(Date, 0, 2) || '-' || substr(Date, 3, 2)) = '0'
ORDER BY TotalSales DESC
LIMIT 1;






SELECT
  SUM(S1) AS TotalS1,
  SUM(S2) AS TotalS2,
  SUM(S3) AS TotalS3,
  SUM(S4) AS TotalS4,
  SUM(S5) AS TotalS5,
  SUM(S6) AS TotalS6,
  SUM(S7) AS TotalS7,
  SUM(S8) AS TotalS8,
  SUM(S9) AS TotalS9,
  SUM(S10) AS TotalS10,
  SUM(
    COALESCE(S1, 0) + COALESCE(S2, 0) + COALESCE(S3, 0) + COALESCE(S4, 0) +
    COALESCE(S5, 0) + COALESCE(S6, 0) + COALESCE(S7, 0) + COALESCE(S8, 0) +
    COALESCE(S9, 0) + COALESCE(S10, 0)
  ) AS TotalDecemberSales,
  CASE
    WHEN SUM(S1) < SUM(S5) THEN 'S1'
    ELSE NULL
  END AS HighlightS1,
  CASE
    WHEN SUM(S2) < SUM(S5) THEN 'S2'
    ELSE NULL
  END AS HighlightS2,
  CASE
    WHEN SUM(S3) < SUM(S5) THEN 'S3'
    ELSE NULL
  END AS HighlightS3,
  CASE
    WHEN SUM(S4) < SUM(S5) THEN 'S4'
    ELSE NULL
  END AS HighlightS4,
  -- Skipping S5 since we are comparing against it
  CASE
    WHEN SUM(S6) < SUM(S5) THEN 'S6'
    ELSE NULL
  END AS HighlightS6,
  CASE
    WHEN SUM(S7) < SUM(S5) THEN 'S7'
    ELSE NULL
  END AS HighlightS7,
  CASE
    WHEN SUM(S8) < SUM(S5) THEN 'S8'
    ELSE NULL
  END AS HighlightS8,
  CASE
    WHEN SUM(S9) < SUM(S5) THEN 'S9'
    ELSE NULL
  END AS HighlightS9,
  CASE
    WHEN SUM(S10) < SUM(S5) THEN 'S10'
    ELSE NULL
  END AS HighlightS10
FROM p1
WHERE strftime('%m', Date) = '12'
AND strftime('%Y', Date) IN ('2017', '2018', '2019');
S1-6 is less than S5

WITH SalesRank AS (
  SELECT
    Date,
    'S1' AS HighestSaleColumn,
    S1 AS HighestSale
  FROM p2
  UNION ALL
  SELECT
    Date,
    'S2',
    S2
  FROM p2
  UNION ALL
  SELECT
    Date,
    'S3',
    S3
  FROM p2
  -- Repeat the above for S4 through S10
),
Ranked AS (
  SELECT Date, HighestSaleColumn, HighestSale,
         RANK() OVER (PARTITION BY Date ORDER BY HighestSale DESC) AS rank
  FROM SalesRank
)
SELECT HighestSaleColumn, COUNT(*) AS DaysWithHighestSales
FROM Ranked
WHERE rank = 1
GROUP BY HighestSaleColumn
ORDER BY DaysWithHighestSales DESC
LIMIT 1;
Store 2 with the highest records of sales of 922 with the largest day.



SELECT
  strftime('%W', Date) AS WeekNumber,
  strftime('%Y', Date) AS Year,
  SUM(COALESCE(S1, 0) + COALESCE(S2, 0) + COALESCE(S3, 0) + COALESCE(S4, 0) +
      COALESCE(S5, 0) + COALESCE(S6, 0) + COALESCE(S7, 0) + COALESCE(S8, 0) +
      COALESCE(S9, 0) + COALESCE(S10, 0)) AS TotalWeeklySales
FROM p2
WHERE strftime('%Y', Date) = '2019'
GROUP BY WeekNumber
ORDER BY TotalWeeklySales DESC
LIMIT 1;

Week 37 of 2019 has the highest sale of all 3 years with 4038