Suyash Sharma; NETID: ss2967 
Mohit Pavecha; NETID: mp1379

1. Briefly discuss how you implemented your recursive client functionality.

Ans) Unlike the name, the code was implemented iteratively. Firstly, both the servers are initialized to preprocess the data into a hashmap which enables constant lookup time. Then the client reads its input text file line by line and sends the domain name to Root level server to check in its records for an IP address. This is where HashMap helps the most as you don't have to iterate through any data structure to find required IP address. If the entry was not found in the HashMap(At root level server), the the client gets a response with another Hostname where the user could potentially look at. If the required IP is not found even in the top level server, then the client writes Error:HOST NOT FOUND into the resolved textfile.

2. Are there known issues or functions that aren't working currently in your attached code? If so, explain.

Ans) I did this Project to the best of my ability and believe to be bug free as the output matches as provided in RESOLVED.txt

3. What problems did you face developing code for this project?

Ans) Implementation of code in Python was certainly one as I am new to Python. Also without receiving a sent string, the command line interface would pause as either the client or the server would be expecting an input and neither would receive one. I figured it out, but only towards later stages of completing this project.

4. What did you learn by working on this project?

Ans) I learnt a lot about Python and the tedious nature of work when an output should exactly match line to line with the required format which requires extra precision. I also learnt more about Sockets and how they can be used to maintain a connection.
