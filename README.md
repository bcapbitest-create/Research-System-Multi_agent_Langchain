# Research-System-Multi_agent_Langchain

The Multi_Agengent researh system is built using langchain.
Here multiple agents are built and brought together to perform a research tasks like;
-Gathering information
-Analyzing the data 
-Developing reports

# step 1 Create the environment Setup and Folder Structure

-create the virtual environments;
uv venv (using cmd)

-Activate the virtual environment;
.venv\Scripts\Activate

-Install the requirements
create the requirements.txt file 
put all he necessary requiremts in it
(llms, tools)

run; "uv pip install -r requirements.txt"

-create the .env file

# step 2; cretae the tools folder
contains: '__init__.py' and 'tools.py' file
write all the tools in here

# step 3; create the pipelines folder
contains : '__init__.py' and 'pipeline.py' file
write all the pipelines in here

# step 4; create the agents folder
contains : '__init__.py' and 'agent.py' file
write all the agents in here.

# step 5; create the 'main.py' file
this is used to test the agent, then later into the user interface, 'app.py'

... Commit these changes 

save the created API credentials in your '.env' file

# create the tools
create the necessary functions.
add the tool decorator'@tool' to transform the functions into tools