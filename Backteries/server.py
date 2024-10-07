import socket
import time

main_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Настраиваем сокет
main_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)  # Отключаем пакетирование
main_socket.bind(("localhost", 10000))  # IP и порт привязываем к порту
main_socket.setblocking(False)  # Непрерывность, не ждём ответа
main_socket.listen(5)  # Прослушка входящих соединений, 5 одновременных подключений
print("Сокет создался")
players = []
while True:
    try:
        # проверяем желающих войти в игру
        new_socket, addr = main_socket.accept()  # принимаем входящие
        print('Подключился', addr)
        new_socket.setblocking(False)
        players.append(new_socket)

    except BlockingIOError:
        pass

    for sock in players:
        try:
            data = sock.recv(1024).decode()  # получаем данные от клиента раскодируем байты в строку
            print("Получил", data)
        except:
            pass

    # Отправка игрокам поля
    for sock in players:
        try:
            sock.send("LOL".encode())
        except:
            players.remove(sock)
            sock.close()
            print("Сокет закрыт")