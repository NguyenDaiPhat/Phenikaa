<?php	
	$tz4File="tz4.dat"; $tz5File="tz5.dat"; $engFile="eng.dat"; $scoreSumFile="scoreSum.dat";
	$cf4=fopen($tz4File,"r+"); $cf5=fopen($tz5File,"r+"); $cfeng=fopen($engFile,"r+"); $cfsum=fopen($scoreSumFile,"r+");
	$tz4=fgets($cf4); $tz5=fgets($cf5); $eng=fgets($cfeng); $scoreSum=fgets($cfsum);
	
	echo $tz4;
	echo $tz5;
	echo $eng;
	echo $scoreSum;	
	
	// save file data to database
	$DBHOST = "localhost:3306";
	$DBUSER = "root";
	$DBPWD = "Xbdd136816";
	$DBNAME = "dbweb";
	
	// Connect to MySQL Database
	$connection = @mysql_connect( $DBHOST, $DBUSER, $DBPWD ) or die("Can't connect to Database!");
//	printf("Database connected!\n");
	
	$cf=fopen("uid.dat","r");
	$uid = fgets($cf); fclose($cf);
//	echo $uid;
	
	@mysql_select_db($uid)or die("Read database error: can't find the database!");	
	
	$query = "SELECT * FROM perfor";
	$result = @mysql_query( $query, $connection ) or die("Data query error:");
	$row = @mysql_num_rows($result);
//	echo $row; 
	if($row ==0 ){
		$query = "INSERT INTO perfor VALUES(1, $tz4, $tz5, $eng, $scoreSum )";
		$result = @mysql_query( $query, $connection );
	}
	else{
		$i=$row; $i1=$row-1;
		$query = "SELECT * FROM perfor limit $i1,$i";
//		echo $query; printf("\n\n");
		$result = @mysql_query( $query, $connection );// or die("Data query error:");
		$row = @mysql_fetch_row($result);
		$id = $row[0]+1;
		
		$query = "INSERT INTO perfor VALUES($id, $tz4, $tz5, $eng, $scoreSum )";
		$result = @mysql_query( $query, $connection );
	}
	
	$cf=fopen("flagFile_resultsave.dat","w+");
	fputs($cf,1); fclose($cf);
	
	$cf=fopen("flagFile_ch.dat","w+"); fputs($cf,0); fclose($cf);
	
	echo "<meta http-equiv='Refresh' content='0; url = user_main.php ?'>";	
	
?>





