SELECT 
    COUNT(DISTINCT seller_id) AS qtd_vendedores
FROM
    olist.tb_orders AS T1
        LEFT JOIN
    olist.tb_order_items AS T2 ON T1.order_id = T2.order_id
WHERE
    T1.order_approved_at BETWEEN '2017-06-01' AND '2018-06-01'