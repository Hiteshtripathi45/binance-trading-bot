def validate_inputs(args):
    if args.type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Invalid order type. Use MARKET or LIMIT")

    if args.side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Invalid side. Use BUY or SELL")

    if args.quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if args.type.upper() == "LIMIT" and args.price is None:
        raise ValueError("Price is required for LIMIT orders")