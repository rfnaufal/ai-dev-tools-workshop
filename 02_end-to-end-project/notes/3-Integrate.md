## Integrating Frontend and backend

### 1. Integrating Frontend and Backend

Prompt:
> make frontend use backend. use openapispec for guidance and follow the guideline in AGENTS.md

<br>
Connected frontend to backend by configuring Vite proxy to forward /api requests to localhost:8000 and refactoring api.ts. 
<br>

Prompt:
> create a makefile for running backend

**Content of Makefile:**
```
.PHONY: install-backend run-backend

install-backend:
	cd backend && uv sync

run-backend:
	cd backend && uv run uvicorn main:app --reload --port 8000
```
**Explanation:** <br>
A Makefile is a special file used by the make build automation tool. In this project, I created it to act as a task runner or shortcut manager.<br>

Instead of typing long, complex commands or manually changing directories, you can just run simple make commands.<br>
Here is what the specific commands in your Makefile do: <br>

make install-backend: <br>
What it does: Runs cd backend && uv sync <br>
Why use it: Installs or updates all the Python dependencies for your backend without you needing to cd into the folder first. <br>
make run-backend: <br>
What it does: Runs cd backend && uv run uvicorn main:app --reload --port 8000 <br>
Why use it: Starts your backend server with one short command. <br>
It handles the directory switching and specific flags (like --reload for development) automatically.<br>
It's essentially a way to save you time and keystrokes! <br>

Since the result still not as expcted then i added prompt:<br>
I expected in the package.json they command will use the makefile that we created.  <br>
> for test backend can we use make test? <br>

Prompt:<br>
>then i also find that when access backend http://127.0.0.1:8000/ it's show {"detail":"Not Found"}<br>
>I want to have mesage such as welcome to backend snake game<br>

Prompt: <br>
>I want to add node_modules to gitignore, so ensure you add install:all to install required package the package.json 

So here is the result: <br><br>
<img src="images/Last setup integrate.png" width="75%"> <br><br>
<img src="images/Leaderboard.png" width="75%"> <br><br>
<img src="images/Leaderboard-api.png" width="75%">