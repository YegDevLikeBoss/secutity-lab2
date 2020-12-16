# Лаборатоные по Информационной безопасности Егоян А.А.

## Лабораторная 1 "Шифр цезаря":

```bash
python lab1/caesar.py <message:str> <key:(int|str)>
```

## Лабораторная 2 "Протокол Диффи — Хеллмана":

```bash
python lab2/dh.py
```

## Лабораторная 3 "RSA":

генерация ключей
```bash
python lab3/main.py -g
```
шифрование сообщения
```bash
python lab3/main.py -e -i <input filename> -k <public key filename>
```
дешифровка сообщения
```bash
python lab3/main.py -d -i <input filename> -k <private key filename>
```

## Лабораторная 4 "SRP-6":
```bash
python lab3/test.py
```