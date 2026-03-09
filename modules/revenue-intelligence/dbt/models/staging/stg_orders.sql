select
    cast(order_id as {{ dbt.type_string() }}) as order_id,
    cast(customer_id as {{ dbt.type_int() }}) as customer_id,
    cast(order_date as date) as order_date,
    cast(order_value as {{ dbt.type_numeric() }}) as order_value
from {{ source('raw', 'orders') }}
