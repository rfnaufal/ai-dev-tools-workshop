## Create Frontend for Snake Game Application

### 1. Development using Lovable

Prompt:
> create the snake game with two models: pass-through and walls. prepare to make it multiplayers - we will have this functionality: leaderboard and watching (me following other players that currently play). add mockups for that and also for log in. everything should be interactive - I can log in, sign up, see my username when I'm logged in, see leaderboard, see other people play (in this case just implement some playing logic yourself as if somebody is playing) make sure that all the logic is covered with tests
>
> don't implement backend, so everything is mocked. But centralize all the calls to the backend in one place

I also added from the original result with prompt:
> Update the fonts to a clean, modern look and change the color scheme from green to a soft, eye-friendly blue.

<img src="images/result.png" width="75%"> <br><br>

the next thing is we need to connect lovable with github and then from the repository created set visibility to public. 


##### 🚀 Built With

<p align="left">
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white" />
  <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black" />
  <img src="https://img.shields.io/badge/shadcn--ui-000000?style=for-the-badge&logo=shadcnui&logoColor=white" />
  <img src="https://img.shields.io/badge/TailwindCSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" />
</p>

### 2. Connect to codespace

#### 2.1 Preparation

As preparation we need to install the following tools:
1. Google Antigravity 
2. Github CLI

```sh
gh auth login
```

There will some questions such as below: <br>
Where do you use GitHub? GitHub.com <br>
? What is your preferred protocol for Git operations on this host? SSH <br>
? Generate a new SSH key to add to your GitHub account? Yes <br>
? Enter a passphrase for your new SSH key (Optional): ************ <br>
? Title for your SSH key: GitHub CLI <br>
? How would you like to authenticate GitHub CLI? Login with a web browser <br>
<br>
then will show code that we need to input in the browser to authorize device. <br>

To create codespace we need admin right in the repository, run:

```sh
gh auth refresh -h github.com -s codespace
```

follow the procedure to grant the permission.

#### 2.2 Create Codespace

Create codespace using github cli:

```sh
gh cs create
```

enter the repository: {accountname/repo-name} <br>
Machine Type: 2 cores, 8 GB RAM, 32 GB Storage <br>
keep the name for example: bug-free-halibut-7x75wp4j75xfxgvg <br>

Run the command to ssh to the machine:

```sh
gh cs ssh -c bug-free-halibut-7x75wp4j75xfxgvg
```

#### 2.3 setup SSH for Antigravity

we need to setup ssh so we can ssh easier to connect to codespace. 

```sh
gh cs ssh --config -c bug-free-halibut-7x75wp4j75xfxgvg
```

it will generate like this: <br>
```
Host cs.bug-free-halibut-7x75wp4j75xfxgvg.main 
    User codespace 
	ProxyCommand /opt/homebrew/bin/gh cs ssh -c bug-free-halibut-7x75wp4j75xfxgvg --stdio -- -i /Users/rfnaufal/.ssh/codespaces.auto 
	UserKnownHostsFile=/dev/null 
	StrictHostKeyChecking no 
	LogLevel quiet 
	ControlMaster auto 
	IdentityFile /Users/rfnaufal/.ssh/codespaces.auto
```

then added the lines into ~/.ssh/config. <br>
save it and run this command to ssh to codespace:

```sh
ssh cs.bug-free-halibut-7x75wp4j75xfxgvg.main
```

<img src="images/ssh.png" width="55%"> <br><br>

#### 2.4 Connect Antigravity to Codespace

Click from bottom left of Antigravity then choose **Connect to SSH Host**  You will use last SSH configuration <br><br>
<img src="images/Agy to SSH.png" width="75%"> <br>

once login open the terminal and go to /workspaces, or click open folder and find workspaces. <br>you will find your repo. <br> <br>
<img src="images/workspace in Agy.png" width="75%"> <br>

click open folder and find /workspaces then click ok, so the window will be like this:
<img src="images/snake-spec.png" width="75%">

create two folder named frontend and backend. <br>
Move all the files to frontend <br><br>
<img src="images/move files.png" width="75%">

Create .gitignore file under backend. <br> You can check the guide in the README.md <br>
open the terminal and run the command to Install dependencies and start the development server

```sh
npm i
```

<img src="images/npm-i.png" width=75%>

```sh
npm run dev
```

<img src="images/npm-run-dev.png" width=75%> <br> <br>

Result: <br>
<img src="images/localhost-snakegame.png" width=75%>

#### 2.4 Verify Frontend Apps

Prompt:
>I have some tests for my frontend applicatoin but i dont know how to run them. help me figure it out <br>
>here is the example: <br>
>frontend/src/tests/gameLogic.test.ts <br>

it's not a single correction, so we need to test several time until it get fixed. <br>
if test failed, to capture the error to the agent, I run the command below in the chat.<br>

```sh
@terminal:bash 
```

then try again in the terminal

```sh
npm test
```

Result:

<img src="images/verify-frontend.png" width=75%>
