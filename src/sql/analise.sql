SELECT

    T2.seller_id,
    SUM( T2.price) as receita_total,
    COUNT( DISTINCT T1.order_id) AS qtde_pedidos,
    COUNT( T2.product_id) AS qtde_produtos,
    COUNT( DISTINCT T2.product_id) as qtd_prod_dist,
    MIN( CAST( julianday('2018-06-01') - julianday( T1.order_approved_at) AS INT)) AS qtde_dias_ult_venda,
    MAX( CAST( julianday('2018-06-01') - julianday( dt_inicio ) AS INT ) ) AS qtde_dias_base

FROM
    
    tb_orders AS T1
        LEFT JOIN
    tb_order_items AS T2 ON T1.order_id = T2.order_id

LEFT JOIN (
    SELECT 
        T2.seller_id,
        MIN( DATE( T1.order_approved_at ) ) AS dt_inicio
    FROM tb_orders as T1
    LEFT JOIN tb_order_items AS T2
    ON T1.order_id = T2.order_id
    GROUP BY T2.seller_id
) AS T3

ON T2.seller_id = T3.seller_id

WHERE
    
    T1.order_approved_at BETWEEN '2017-06-01' AND '2018-06-01'

GROUP BY T2.seller_id