SELECT DT_SGMNT,
        COUNT( DISTINCT seller_id)
FROM tb_sellers_sgmnt
GROUP BY DT_SGMNT