# test program to coordinate user data with client and server sockets to generate
# a report
import zmq

# prompt user in terminal to input data for report
def get_client_data():
    inventory = []
    while True:
        name = input("Please enter an item name or E to exit: ").strip()
        if name == 'E':
            break 
        cost = float(input("Please enter item's cost in dollars: "))
        count = int(input("please enter the quantity of this item: "))
        inventory.append({"name": name, "cost": cost, "count": count})
    return{"inventory":inventory}

# call client, send user data and recieve final report
def run_report_microservice():
    context = zmq.Context()
    print("Client attempting to connect to server...")
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    report_content = get_client_data()
    socket.send_json(report_content)

    returned_report = socket.recv_string()

    print(returned_report)

if __name__ == "__main__":
    run_report_microservice()