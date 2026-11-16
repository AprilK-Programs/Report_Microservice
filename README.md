# Report_Microservice
What it does: 
This microservice works by sending data from the user to the client in the form of JSON objects which then send it (as a JSON object still) to the server that converts it into a report. The report is then returned as a string and printed on the user's end. 
To REQUEST and RECEIVE: 
1. To operate this microservice the user would download all three .py into one folder. Then you can open them in an IDE (the devs used Visual Studio Code 3). 
2. Open THREE terminals (cmd \ on Mac). In the first terminal run python3 server.py, to start the server. In the second terminal run python3 client.py, to start the client. Then finally in the third terminal run test_program.py.
<img width="1155" height="134" alt="Screenshot 2026-11-16 at 10 51 30 AM" src="https://github.com/user-attachments/assets/232cbccd-b64c-4bc1-9f15-3ff1843642e7" />
3. In the test_program terminal the user will then be prompted to enter the name, cost and quantity of the item and this prompt will loop until the user enters 'E'.
4. After the test_program will send the JSON to the client which will send it to the service that converts it to a report and returns the string to the client which will then send the string to the test_program and print the string report in the the test_program terminal. 

<img width="1106" height="304" alt="Screenshot 2026-11-16 at 10 52 52 AM" src="https://github.com/user-attachments/assets/182aa5c3-1baa-4ca5-9e02-c848119a7f1d" />
UML Sequence Diagram:
<img width="409" height="376" alt="Screenshot 2026-11-16 at 11 20 48 AM" src="https://github.com/user-attachments/assets/201b2f80-9c9d-4eb5-b093-fe3a10321e75" />
