# Flint-terminal
Flint terminal is a terminal verion of Flint, which uses `json` files as a database.

## Todo's
![[TOdo's]]

## Commands
- [[#create-project]] 
- [[#cd or project]]
- [[#cd .. or <]]
- [[#list-p or list-projects]]
- [[#root]]
- [[#open]]
- [[#Asset Level Commands]]
	- [[#create-asset]]
- [[#Quick Command]]
	- [[#k1 k2 k3 k4]]
	- [[#l1 l2 l3 l4]]


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
 
 ### list-p or list-projects
*Type: #list* 
*Level: #root #any*
*Return: List of all the projects*
Prints out a table containing the list of alll the project including project id and date it is created on.

### root
*Type: #move*
*Level: #any*
*Return: Moves to the root level.*

### open
*Type: #open*
*Level: #any*
*Return: Opens the file explorer of the current level.*

## Asset Level Commands
### create-asset
*Type: #create*
*Level: #project *
*Return: Creates an asset under the project in the correspoding directory*
Creates an asset under the given project directory.

`create-asset` : Main command
`Asset Type` from ['char', 'prop', 'envi', 'matte']
`Asset Name`: Name of the asset
`Asset Discription`: About the asset.

## Quick Command
###  k1, k2, k3, k4
*Type: #qucik*
*Level: #any *
Save the location of the corresponding key.

### l1, l2, l3, l4
*Type: #quick*
*Level: #any*
Set the location of the corresponding key.
