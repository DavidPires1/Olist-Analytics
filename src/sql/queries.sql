SELECT DT_SGMNT,
        COUNT( DISTINCT seller_id)
FROM tb_sellers_sgmnt
GROUP BY DT_SGMNT

SELECT * 

FROM tb_sellers_sgmnt

WHERE seller_id = '53243585a1d6dc2643021fd1853d8905'

ORDER BY DT_SGMNT