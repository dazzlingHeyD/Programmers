SELECT 
    PRODUCT_CODE, sum(p.PRICE * o.SALES_AMOUNT) SALES    
FROM
    PRODUCT p, OFFLINE_SALE o
WHERE
    p.PRODUCT_ID = o.PRODUCT_ID
GROUP BY p.PRODUCT_ID

ORDER BY
    SALES desc ,PRODUCT_CODE asc