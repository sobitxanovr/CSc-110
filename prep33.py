def get_ok_items(carry_n, personal, restricted):
    overall = carry_n.union(personal)
    allowed = overall.difference(restricted)
    return allowed
