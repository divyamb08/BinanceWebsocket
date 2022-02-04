import websocket, json

cc = 'btcusdt'
interval = '1m'
socket = f'wss://stream.binance.com:9443/ws/{cc}@kline_{interval}'

closes, highs, lows = [] , [] , []

def on_message(ws, message):
    json_message = json.loads(message)
    candle = json_message['k']
    is_candle_closed = candle['x']
    close = candle['c']
    high = candle['h']
    low = candle['l']
    volume = candle['v']
    open = candle['o']
    
    if is_candle_closed:
        closes.append(float(close))
        highs.append(float(high))
        lows.append(float(low))
        
        print(closes)
        print(highs)
        print(lows)
            

def on_close(ws):
    print("### closed ###")

ws = websocket.WebSocketApp(socket, on_message=on_message, on_close=on_close)

ws.run_forever()

