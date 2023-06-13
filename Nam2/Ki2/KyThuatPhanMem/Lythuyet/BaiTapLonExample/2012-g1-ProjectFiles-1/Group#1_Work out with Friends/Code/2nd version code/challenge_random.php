<?php
	printf("challenge.php");
	$friendSelect = $_POST['friendSelect'];
	echo $friendSelect;
	
	// Connect to Database- update friend info
		$DBHOST = "localhost:3306";
		$DBUSER = "root";
		$DBPWD = "Xbdd136816";
		$DBNAME = "dbweb";
	
	// Connect to MySQL Database
		$connection = @mysql_connect( $DBHOST, $DBUSER, $DBPWD ) or die("Can't connect to Database!");
	//printf("Database connected!\n");
	
	
	$cf=fopen("uid.dat","r"); $dbName=fgets($cf); fclose($cf);
	@mysql_select_db($DBNAME) or die("Read database error: can't find the database!");	
	$query = "SELECT * FROM user";
	$result = @mysql_query( $query, $connection ) or die("Data query error:");
	//echo $result;
	//printf("\n\n");
	
	$i=$friendSelect-1; $i2=$friendSelect;
	$query = "SELECT * FROM user limit $i,$i2";
	echo $query; printf("\n\n");
	$result = @mysql_query( $query, $connection );// or die("Data query error:");
	$row = @mysql_fetch_row($result);
	echo $row[0]; printf("\n\n\n\n");
	
	// check chName database
	$chName= $row[0];
	@mysql_select_db($chName) or die("Read database error: can't find the database!");	
	$query = "SELECT * FROM perfor";
	$result = @mysql_query( $query, $connection ) or die("Data query error:");
	//echo $result;
	//printf("\n\n");
	$row = @mysql_num_rows($result);
	//echo $row;  printf("\n\n");	
	
	//Select the max performance
	$chMax=0;
	$row_for=$row-1;
	for($i=0; $i<=$row_for; $i++){
		$i2=$i+1;
		$query = "SELECT * FROM perfor limit $i,$i2";
		echo $query; printf("\n\n");
		$result = @mysql_query( $query, $connection );// or die("Data query error:");
		$row = @mysql_fetch_row($result);
		echo $row[4]; printf("\n\n\n\n");
		
		if($row[4]>$chMax)
			$chMax=$row[4];
	}
	echo $chMax;
	$cf=fopen("chMax.dat","w+"); fputs($cf,$chMax); fclose($cf);
	
	$cf=fopen("scoreSum.dat","r"); $scoreSum=fgets($cf); fclose($cf);
	if($scoreSum>$chMax)
		$flag_chwin=1;
	elseif($scoreSum==$chMax)
		$flag_chwin=0;
	else
		$flag_chwin=-1;
	
	$cf=fopen("flagFile_chwin.dat","w+"); fputs($cf,$flag_chwin); fclose($cf);
	
	$cf=fopen("flagFile_ch.dat","w+"); fputs($cf,1); fclose($cf);
	
	echo "<meta http-equiv='Refresh' content='0; url = user_main_ch_random.php ?'>";

?>







