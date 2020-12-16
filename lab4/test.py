from srp import Client, Server

if __name__ == '__main__':
    client = Client()
    serv = Server()

    I = 'alice'
    P = 'password123'
    print(f'I = {I}, P = {P}')

    print('Клиент: рассчитывает верификатор')
    salt, verifier = client.compute_verifier(I, P)
    print(f'Соль: {salt}')
    print(f'Верификатор: {verifier}')

    print('Клиент передаёт I, s, v на сервер')
    print('Клиент: рассчитывает частные и публичные значения')
    A = client.compute_client_values()
    print(f'Клиент A: {A}')

    print('Клиент передаёт A на сервер')
    print('Сервер: рассчитывает частные и публичные значения')
    B = serv.compute_server_values(I, verifier)
    print(f'Сервер B: {B}')

    print('Сервер передаёт B клиенту')
    print('Клиент: рассчитывает скремблер и сессионный ключ')
    client.compute_premaster_secret(salt, B)
    M = client.compute_session_key(salt, B)

    print('Сервер: рассчитывает скремблер и сессионный ключ')
    serv.compute_premaster_secret(I, salt, verifier, A)
    serv.compute_session_key(I, salt, A)

    print(f'Сообщение существования клиента: {M}')
    print(f'Сообщение существования сервера: {serv.M}')

    print('Клиент передаёт M на сервер')
    print('Сервер: верифицирует сессию')
    hashed_M = serv.verify_session(M)
    print(f'Сервер: захешированный M: {hashed_M}')

    print('Сервер передаёт захешированный M Клиенту')
    print('Клиент: Верифицирует сессию')
    hashed_M = client.verify_session(hashed_M)
    print(f'Клиент: захешированный M: {hashed_M}')

    print(f'Сессионный ключ клиента: {client.session_key}')
    print(f'Сессионный ключ сервера: {serv.session_key}')

    assert client.authenticated
    assert serv.authenticated

    print('Удача')
