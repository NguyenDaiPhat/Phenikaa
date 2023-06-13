<?php
	session_start();
	$userid = $_POST["userid"];
	$password = $_POST["password"];
	$sub = $_POST["subm"];
	session_register("userid");
	
	//include("sys_conf.inc");
	$DBHOST = "localhost:3306";
	$DBUSER = "root";
	$DBPWD = "Xbdd136816";
	$DBNAME = "dbweb";

	
	if($sub == "Login"){
		// Connect to MySQL Database
		$connection = @mysql_connect( $DBHOST, $DBUSER, $DBPWD ) or die("Can't connect to Database!");
	
		@mysql_select_db($DBNAME) or die("Read database error: can't find the database!");
		$query = "SELECT * FROM user WHERE uid='$userid' ";
		$result = @mysql_query($query, $connection) or die("Data query error:");
	
		if( $row = mysql_fetch_row($result) ){
			if( $row[1] == $password ){ // Id_varify success
				// record uid			
				$cf=fopen("uid.dat","w+");
				fputs($cf, $userid); fclose($cf);
			
				$cf= fopen("flagFile_upload.dat","w+");
				fputs($cf,0);
				fclose($cf);
				
				$cf=fopen("flgaFile_analyse.dat", "w+");
				fputs($cf,0);
				fclose($cf);
				
				$cf=fopen("flagFile_resultsave.dat","w+");
				fputs($cf,0); fclose($cf);
				
				echo "<meta http-equiv='Refresh' content='0; url = user_main.php ?'>";
			}
			else{
				printf("Wrong Password");
				$msg="Wrong Password";
				echo "<meta http-equiv='Refresh' content='0; url=login.php?msg=$msg'>";
			}
		}
		else{// user doesn't exit
			printf("User doesn't exit");
		}
	
	}// END_if_login	

?>