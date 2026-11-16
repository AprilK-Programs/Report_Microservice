
# This code was largely based on the example found on
# https://canvas.oregonstate.edu/courses/2061221/files/119919807?verifier=vjTCpERH2OSOBbwnKxV5zmPCTElCsbTPxbkhRVSN&wrap=1
# by Luis Flores for CS 361
# (c) 2024 Luis Flores
import datetime
import time
import zmq 


# create a mock report from input data 
def report_microservice(data):
    report = [
    "Report Summary:",
    f"Report Date/Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "Current Inventory:",
    f"{'Item':<30} {'Count':>10} {'Cost':>10}",
    ("-"*60)
    ]
    total_item = 0
    total_cost = 0
    for i in data.get("inventory",[]):
        name = i.get("name","None")
        cost = i.get("cost",0)
# work around to get $ next to amount instead of off to side
        str_cost = f"${i['cost']:.2f}"
        count = i.get("count",0)
        total_item +=count
        total_cost += (cost*count)
# name with left aligned test and padding, cost and count right aligned 
        report.append(f" {name:<30} {count:>10} {str_cost:>10}")
    report.append(f"Total Items:{total_item} Total Cost:$ {total_cost:.2f}")
    return "\n".join(report)

 # set up sockets and return report to client
def run_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
# socket 5555 for user and 5556 for client/server
    socket.bind("tcp://*:5556")
    while True:
        client_data = socket.recv_json()
        print(f"Received data from the client")
        if len(client_data) > 0:
            if client_data == 'Q':
                break
#sleep for 3 seconds to give time for client to send request
            time.sleep(3)

            report = report_microservice(client_data)
# Send string reply back to client program 
            socket.send_string(report)
#close the program 
    context.destroy()
    
if __name__ == "__main__":
    run_server()