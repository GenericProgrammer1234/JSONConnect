# JSONConnect
A way to superpower JSON using basic commands!
<br>
**Notice: this is work in progress and many more commands will be added in the future**

## Documentation
### Installation
Download this repo by
`git clone https://github.com/GenericProgrammer1234/JSONConnect.git`
<br>
Then run the file by `python jsonconnect.py` or `python3 jsonconnect.py`
<br>
**Notice: More installation steps may be added in the future**
### Commands
You need to type in commands to do things
#### Create
**The create command creates JSON files. File creation will fail if the file already exists, the condition returns false or no name is provided**
<br>
##### **Arguments**
**name: The name of the JSON file you want to create**
##### **Examples**
`create`
<br>Result: Error<br>
`create hello`
<br>Result: The creation of a JSON file named `hello`<br>
`create alreadyexistingfile`
<br>Result: Error<br>
#### Delete
**The delete command deletes JSON files. File deletion will fail if the file doesn't exist, the condition returns false or no name is provided**
<br>
##### **Arguments**
**name: The name of the JSON file you want to delete**
##### **Examples**
`delete`
<br>Result: Error<br>
`delete hello`
<br>Result: The deletion of a JSON file named `hello`<br>
`delete notexistingfile`
<br>Result: Error<br>
### Conditions
Conditions are expressions that return true or false
<br>
A condition starts with `if`, currently only the `exists` condition is implemented
<br>
#### Examples
`if hello exists`
<br>Result: true<br>
`if nonexistentfile exists`
<br>Result: false<br>
