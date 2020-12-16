sharedPrime = 23
sharedBase = 5

aliceSecret = 6
bobSecret = 15

A = (sharedBase**aliceSecret) % sharedPrime
B = (sharedBase ** bobSecret) % sharedPrime

aliceSharedSecret = (B ** aliceSecret) % sharedPrime
bobSharedSecret = (A**bobSecret) % sharedPrime

print( f"""Публичное простое число: {sharedPrime}
Публичный простой корень по модулю: {sharedBase}

Публичный ключ Алисы: {A}
Публичный ключ Боба: {B}

Общий секретный ключ вычисленный Алисой: {aliceSharedSecret}
Общий секретный ключ вычисленный Бобом: {bobSharedSecret}""")