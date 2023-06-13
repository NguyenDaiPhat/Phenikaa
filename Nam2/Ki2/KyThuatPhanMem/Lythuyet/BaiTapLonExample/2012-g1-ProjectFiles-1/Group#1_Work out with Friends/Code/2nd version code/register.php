<?php
	$DBHOST = "localhost:3306";
	$DBUSER = "root";
	$DBPWD = "Xbdd136816";
	$DBNAME = "dbweb";
	
	// Connect to MySQL Database
	$connection = @mysql_connect( $DBHOST, $DBUSER, $DBPWD ) or die("Can't connect to Database!");
	//printf("Database connected!\n");


	@mysql_select_db($DBNAME) or die("Read database error: can't find the database!");	
	$query = "SELECT * FROM user";
	$result = @mysql_query( $query, $connection ) or die("Data query error:");
	//echo $result;
	printf("\n\n");
	$row = @mysql_num_rows($result);
	echo $row;  printf("\n\n");
	
	// Creat database for all users, with table Perfor/ Friends
	$row_for = $row-1;
	for($i=1; $i<=$row_for; $i++){
		echo $i;		
		$i2= $i+1;
		@mysql_select_db($DBNAME, $connection);
		$query = "SELECT * FROM user limit $i,$i2";
		echo $query; printf("\n\n");
		$result = @mysql_query( $query, $connection );// or die("Data query error:");
		$row = @mysql_fetch_row($result);
		echo $row[0]; printf("\n\n\n\n");
		
		$dbName=$row[1];
		$query ="CREATE DATABASE $dbName";
		echo $query; printf("\n\n");
		$result = @mysql_query( $query, $connection ); // or die("Database creation error:");
		
		@mysql_select_db($dbName, $connection);
		$query = "CREATE TABLE Perfor(id int, tz4 double, tz5 double, eng double, scoreSum double)";	
		$result = @mysql_query($query, $connection);//or die("Table create error");
		
		$query = "CREATE TABLE Friends(id int,uid VARCHAR(10))";	
		$result = @mysql_query($query, $connection);//or die("Table create error");		
	}
	

	
/*	
	$row=2;
	$query = "SELECT * FROM employees limit 1,2";
	echo $query;
	$result = @mysql_query( $query, $connection ) or die("Data query error:");
	echo $result;

	$row = @mysql_fetch_row($result);
	echo $row[1]; 
	*/	


	/*
	$dbName = "uid";
	$query = "CREATE DATABASE $dbName";
	echo $query;
	printf("\n\r");
	//$result = @mysql_query( $query, $connection ); // or die("Database creation error:");
	//@mysql_select_db($dbName, $connection)or die("Can't use database");
	$query = "CREATE TABLE Perfor(id int,tz4 double)";	
	//$result = @mysql_query($query, $connection)or die("Table create error"); 
	*/

?>
