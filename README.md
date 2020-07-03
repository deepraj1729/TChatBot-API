# TChatBot-API
A `Flask REST API` to serve trained `ChatBots` using `Tensorflow Serving` and `Docker containers`

# Architecture of the Application:
![architecture](architecture.png)

# Usage:
- Create a virtual environment
- Activate the environment
- Clone the repository inside the environment: 
      
      git clone https://github.com/deepraj1729/TChatBot-API.git
- Navigate to the directory `TChatBot-API`
- Install the requirements with this command:

      pip install -r requirements.txt
- To run the API from both server side and client side:
  - Open `2 terminals` from the current location (from inside `TChatBot-API folder`)
   - One for `Server-Side`
   - One for `Client-Side`
  - Run this command in terminal 1 (`Server-Side`) to run the Flask server
      
        python app.py
  - Run this command in terminal 2 (`Client-Side`) to run the chat session 
        
        python main.py
  
- To `end/quit` Chat session in the `client-side` terminal, type `quit` and `enter`
- To `end/quit` Server session in the `server-side` terminal, use `ctrl + c`
     
