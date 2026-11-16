# This code was largely based on the example found on
# https://canvas.oregonstate.edu/courses/2061221/files/119919807?verifier=vjTCpERH2OSOBbwnKxV5zmPCTElCsbTPxbkhRVSN&wrap=1
# by Luis Flores for CS 361
# (c) 2024 Luis Flores

import json
import zmq # For ZeroMQ


def start_microservice():
    context = zmq.Context()
# user socket, reply to connect
    user_socket = context.socket(zmq.REP)
    user_socket.bind("tcp://localhost:5555")
    print("User on 5555 confirmed")
# server socket
    server_socket = context.socket(zmq.REQ)
    server_socket.connect("tcp://localhost:5556")
    print("server on 5556 confirmed")
# receive user input, send to server, receive report from server, return to user
    while True:
        user_input = user_socket.recv_json()
        print("data received confirmed")
        server_socket.send_json(user_input)
        microserver_report = server_socket.recv_string()
        print("report received confirmed")
        user_socket.send_string(microserver_report)
        
if __name__ == "__main__":
    start_microservice()