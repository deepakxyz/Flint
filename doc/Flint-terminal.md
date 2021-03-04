# Flint-terminal
Flint terminal is a terminal verion of Flint, which uses `json` files as a database.

## Todo's
- `set shortcut for a directory`

## Commands
- [[#create-project]] 
- [[#cd or project]]
- [[#cd .. or <]]
- [[#list-p]]


### create-project
*Type: #create*
*Level: #root*
*Return: Project directory with [[assets]], [[sequences]] and [[detail.json]]*
 Create a new project under the base directory. Root directory is set under the `db > db.py`. `ROOT_DIR = "path"`
 
 ### cd or project
 *Type: #move*
 *Level: #root*
 *Return: None*
 Moves into a given project name or project level.
 ```bash
 cd project-name 
 project project-name
 ```
 
 ### cd .. or <
 *Type: #move*
 *Level: #project*
 *Return: None*
 Move one level back.
 
 ### list-p
*Type: #list* 
*Level: #root #any*
*Return: List of all the projects*
Prints out a table containing the list of alll the project including project id and date it is created on.
