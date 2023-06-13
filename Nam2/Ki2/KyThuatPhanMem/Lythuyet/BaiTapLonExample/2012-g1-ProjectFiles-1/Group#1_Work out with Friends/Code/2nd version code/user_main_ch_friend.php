<?php		
		$max_len=8;
		$tz4File="tz4.dat"; $tz5File="tz5.dat"; $engFile="eng.dat"; $scoreSumFile="scoreSum.dat";
				
		// Check if data uploaded
		$cf=fopen( "flagFile_upload.dat", "r+" );
		$flag_upload=fgets($cf);
		fclose( $cf );
		
		$cf=fopen("flgaFile_analyse.dat", "r+");
		$flag_analyse = fgets($cf);
		fclose($cf);
		
		if( !file_exists("flagFile_resultsave.dat") )
		{ // No counterfile exist
			$flag_resultsave=0;
			$cf=fopen( "flagFile_resultsave.dat","w+" );
			fputs( $cf, 0 ); fclose( $cf );
		}
		else{
			$cf=fopen( "flagFile_resultsave.dat","r" );
			$flag_resultsave=fgets($cf); fclose($cf);
		}

		if($flag_resultsave == 1){
			$resultsave = "Results saved."; }
		else{
			$resultsave = "Not saved yet.";}
		
		
		if( $flag_analyse == 1 && $flag_upload==1 ){
			$cf=fopen( "FileName_upload.dat", "r+" );
			$FileName = fgets($cf);
			
		
		if( !file_exists($tz4File) )
		{ // No counterfile exist
			$tz4=0;
			$cf=fopen( $tz4File,"w" );
			fputs( $cf, "0" );
			fclose( $cf );
		}
		else{
			$cf=fopen( $tz4File,"r" );
			$tz4= trim( fgets($cf, $max_len) );
			fclose($cf);
		}
		
		if( !file_exists($tz5File) )
		{ // No counterfile exist
			$tz5=0;
			$cf=fopen( $tz5File,"w" );
			fputs( $cf, "0" );
			fclose( $cf );
		}
		else{
			$cf=fopen( $tz5File,"r" );
			$tz5= trim( fgets($cf, $max_len) );
			fclose($cf);
		}
		$FileName="";
		
		if( !file_exists($engFile) )
		{ // No counterfile exist
			$eng=0;
			$cf=fopen( $engFile,"w" );
			fputs( $cf, "0" );
			fclose( $cf );
		}
		else{
			$cf=fopen( $engFile,"r" );
			$eng= trim( fgets($cf, $max_len) );
			fclose($cf);
		}
		
		if( !file_exists($scoreSumFile) )
		{ // No counterfile exist
			$scoreSum=0;
			$cf=fopen( $scoreSumFile,"w" );
			fputs( $cf, "0" );
			fclose( $cf );
		}
		else{
			$cf=fopen( $scoreSumFile,"r" );
			$scoreSum= trim( fgets($cf, $max_len) );
			fclose($cf);
		}		
	
		}
		else{
		$tz4=0; $tz5=0; $eng=0; $scoreSum=0;
		}
		
		
		if( !file_exists("flagFile_chwin.dat") )
		{ // No counterfile exist
			$flag_chwin=-2;
			$cf=fopen( "flagFile_chwin.dat","w" );
			fputs( $cf, "0" );
			fclose( $cf );
		}
		else{
			$cf=fopen( "flagFile_chwin.dat","r" );
			$flag_chwin= trim( fgets($cf, $max_len) );
			fclose($cf);
		}
		
		$cf=fopen("flagFile_ch.dat","r"); $flag_ch=fgets($cf); fclose($cf);
		if($flag_ch==1){
		
		if( !file_exists("chMax.dat") )
		{ // No counterfile exist
			$chMax=0;
			$cf=fopen( "chMax.dat","w" );
			fputs( $cf, "0" );
			fclose( $cf );
		}
		else{
			$cf=fopen( "chMax.dat","r" );
			$chMax= trim( fgets($cf, $max_len) );
			fclose($cf);
		}
	}
		else
	{
		$chMax=0; $flag_chwin=-2;
	}

		
		// Connect to Database- update friend info
		$DBHOST = "localhost:3306";
		$DBUSER = "root";
		$DBPWD = "Xbdd136816";
		$DBNAME = "dbweb";
	
	// Connect to MySQL Database
		$connection = @mysql_connect( $DBHOST, $DBUSER, $DBPWD ) or die("Can't connect to Database!");
	//printf("Database connected!\n");
	
	$cf=fopen("uid.dat","r"); $dbName=fgets($cf); fclose($cf);
	
	@mysql_select_db($dbName) or die("Read database error: can't find the database!");	
	
	$query = "SELECT * FROM friends";
	$result = @mysql_query( $query, $connection ) or die("Data query error:");
	//echo $result;
	//printf("\n\n");
	$row = @mysql_num_rows($result);
	//echo $row;  printf("\n\n");	
	
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Work Out with Friend</title>
	<link href="css_user_main_ch_friend.css" rel="stylesheet" type="text/css" />
	<link rel="icon" href="images/icon.ico" />
</head>

<body>
<div id="headerbg">
  <div id="headerblank">
    <div id="header">
	<div id="menublank">
      <div id="menu">
        <ul>
          <li><a href="index.php" class="menu">Home </a></li>
          <li><a href="whysharing_how.php" class="menu">Why sharing & How </a></li>
          <li><a href="#" class="menu"> Top List </a></li>
          <li><a href="support.php" class="menu">Support</a></li>
        </ul>
      </div>
	  </div>
      <div id="headerrightblank">
	 
      
        <div id="special">Work out with friends </div>
        <div id="year">2012</div>
      </div>
	    
		<div id="headernav">
          <ul>
            <li><a href="#" class="register">My Results </a></li>
            <li><a href="#" class="login">Challenge History</a></li>
			<li><a href="user_main.php" class="login">Quit</a></li>

          </ul>
        </div>
		
		
	  <div id="bd" class="tdl">
	 
	  <h2>CHALLENGE FRIEND </h2>
			<hr/>
			<div id="result">
			
				<li>Your current total score: <a style="color: #33FFFF"><?php echo $scoreSum; ?> </a> points <br /></li> <hr/>
				Choose a Friend: <a style="color: #33FFFF">

				 <form action="challenge_friend.php" method="post">
				<select id="friendSelect" name="friendSelect" >
				<?php
					// Creat database for all users, with table Perfor/ Friends
					$row_for=$row-1;
					for($i=0; $i<=$row_for; $i++){
						echo $i;		
						$i2= $i+1;
						@mysql_select_db($dbName, $connection);
						$query = "SELECT * FROM friends limit $i,$i2";
						echo $query; printf("\n\n");
						$result = @mysql_query( $query, $connection );// or die("Data query error:");
						$row = @mysql_fetch_row($result);
						echo $row[1]; printf("\n\n\n\n");
		
						$index=$i+1; $value=$row[1];
						echo "<option value='$index' selected>$value</option>";	
					}		
				?>
				</select> 
				
	    	<input type="submit" name="submit_challengedata" value="Challenge" />
		</form>
			</div> 
			
			<div id="challenge">
				<li>FRIEND 1 highest total score: <a style="color: #33FFFF"><?php echo $chMax; ?> </a> points <br /></li> <br  />
				<li>Your current total score: <a style="color: #33FFFF"><?php echo $scoreSum; ?> </a> points <br /></li> <hr />	  
				<?php
					if($flag_chwin==-2)
						echo "No challenge results yet.";
					elseif($flag_chwin==0)
						echo "There's A Tie.";
					elseif($flag_chwin==1)
						echo "You win.";
					else
						echo "You lose.";
				?>
			</div>				
					  
      </div>
  </div>

<div id="contentbg">
  <div id="contentblank">
  
  

<div id="footerbg">
  <div id="footerblank">
    <div id="footer">
      <div id="footerlinks"><a href="#" class="footerlinks">Home</a> | <a href="#" class="footerlinks">About Our Company</a> | <a href="#" class="footerlinks">Blog</a> | <a href="#" class="footerlinks">Support</a> | <a href="#" class="footerlinks">Services Overview</a> | <a href="#" class="footerlinks">Testimonials</a> | <a href="#" class="footerlinks">Why Choose Us</a> | <a href="#" class="footerlinks">Contact Us</a></div>
      <div id="copyrights">© Copyright Information Goes Here. All Rights Reserved.</div>
      

    </div>
  </div>
</div>
</body>
</html>
