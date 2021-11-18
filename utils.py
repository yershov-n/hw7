def get_revenue(records):
    revenue = {}
    for t_id, quantity, unitprice in records:
        if t_id in revenue:
            revenue[t_id] += quantity * unitprice
        else:
            revenue[t_id] = quantity * unitprice

    return revenue
