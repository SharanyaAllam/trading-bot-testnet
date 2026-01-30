from .validators import validate_inputs

def place_order(client, symbol, side, order_type, quantity, price=None):
    validate_inputs(symbol, side, order_type, quantity, price)

    if order_type == "MARKET":
        return client.client.create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

    if order_type == "LIMIT":
        return client.client.create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )
