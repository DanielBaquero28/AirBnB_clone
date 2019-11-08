<html>
<head>
<h1>AirBnB_clone Command Interpreter</h1>
</head>
<body>
<img src="/Users/usuario/Downloads/HBnB%20Console.png" alt="HBnB Logo Part Clone" width="200" height="80">
<br>
<br>
<h2>Project Description</h2>
<p><strong>In this project we will do the first part of the AirBnB clone final project. In this part we will create the console, where we will create our own data model, manage(create, update, destroy, etc) objects via the console/ command interpreter, and finally store and persist objects to a file (JSON file).</strong></p>
<h2>Command Interpreter Description</h2>
<p>The console allows you to manage your objects with the following commands:</p>
<table>
<tr>
<th>Command</th>
<th>Description</th>
<th>Example</th>
</tr>
<tr>
<td>create</td>
<td>Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id</td>
<td>$ create BaseModel</td>
</tr>
<tr>
<td>show</td>
<td>Prints the string representation of an instance based on the class name and id</td>
<td>$ show BaseModel 1234-1234-1234</td>
</tr>
<tr>
<td>destroy</td>
<td>Deletes an instance based on the class name and id</td>
<td>$ destroy BaseModel 1234-1234-1234</td>
</tr>
<tr>
<td>all</td>
<td>Prints all string representation of all instances based or not on the class name</td>
<td>$ all BaseModel or $ all</td>
</tr>
<tr>
<td>update</td>
<td>Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file)</td>
<td>$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"</td>
</tr>
</table>
<h3>How to start it</h3>
<p>First you have to clone the rep, so you have to execute the following command:</p>
<p>``` https://github.com/DanielBaquero28/AirBnB_clone.git ```</p>
<p>Then access the repo by changing your directory to "AirBnB_clone":</p>
<p>``` cd AirBnB_clone ```</p>
<p>Now execute the file named "console.py":</p>
<p>``` ./console.py ```</p>
<h3>How to use it</h3>
<h4>Interactive Mode</h4>
<p>To enter the interative mode you must execute the following command</p>
<p>``` ./console.py
(hbnb) ```
</p>
<h4>Non Interactive Mode</h4>
<p>To use the non-interactive mode you must use the echo command with the instructions you want to execute, then pipe it executing the name of the file "console.py"</p>
<p>``` echo "create BaseModel" | ./console ```</p>
<h4>Examples</h4>
<h2>Managing Classes</h2>
<p>We will manage the following classes:</p>
<ul>
<li>User</li>
<li>State</li>
<li>City</li>
<li>Amenity</li>
<li>Place</li>
<li>Review</li>
</ul>
</body>
<footer>
Made by: <strong>Giovanny Andres Ortegon Espitia, Daniel Baquero</strong>
</footer>
</html>