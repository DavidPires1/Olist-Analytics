SELECT *,
        PERCENT_RANK() OVER (PARTITION BY product_category_name ORDER BY days_no_sale) AS PCT_ACUM

FROM(

    SELECT *,
            julianday(DATE(order_approved_at)) - julianday(DATE(last_sale)) AS days_no_sale

    FROM(

        SELECT T2.seller_id,
                T3.product_category_name,
                T1.order_approved_at,
                LAG(T1.order_approved_at) OVER ( PARTITION BY T2.seller_id, 
                T3.product_category_name ORDER BY T1.order_approved_at) AS last_sale
            

        FROM
                        
        tb_orders AS T1
        LEFT JOIN
        tb_order_items AS T2 ON T1.order_id = T2.order_id
        LEFT JOIN
        tb_products AS T3 ON T2.product_id = T3.product_id 

        WHERE T2.seller_id IS NOT NULL
        AND T3.product_category_name IS NOT NULL

        ORDER BY T2.seller_id, T1.order_approved_at

    ) AS T1

    WHERE T1.last_sale IS NOt NULL
    AND days_no_sale >= 1

)AS T1