INSERT INTO wells (well, ngdu, cdng, kust, mest)
SELECT DISTINCT wh.well, 0, 0, 0, 0
FROM well_day_histories wh
LEFT JOIN well_day_plans wp ON wh.well = wp.well
WHERE wp.well IS NULL;