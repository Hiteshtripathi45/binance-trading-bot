import logging

def place_order(client, args):
    order_type = args.type.upper()

    if order_type == "MARKET":
        logging.info(f"Placing MARKET order: {args.symbol}, {args.side}, {args.quantity}")

        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side.upper(),
            type="MARKET",
            quantity=args.quantity
        )

    elif order_type == "LIMIT":
        logging.info(f"Placing LIMIT order: {args.symbol}, {args.side}, {args.quantity}, price={args.price}")

        order = client.futures_create_order(
            symbol=args.symbol,
            side=args.side.upper(),
            type="LIMIT",
            quantity=args.quantity,
            price=args.price,
            timeInForce="GTC"
        )

    else:
        raise ValueError("Invalid order type")

    logging.info(f"Order Response: {order}")
    return order