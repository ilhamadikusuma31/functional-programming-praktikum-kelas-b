buah = [
        {"nama": "apel", "harga": 20},
        {"nama": "mangga", "harga": 20},
        {"nama": "jambu", "harga": 19}
    ]
print("sorted berdasarkan harga: ")
print(sorted(buah, key=lambda i: i['harga']))
 