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
?>


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<title>Work Out with Friend</title>
	<link href="css_user_main.css" rel="stylesheet" type="text/css" />
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
	  
	  
		<div class="row-2">
					<ul>
						<li class="m1"><a href="home.html">Home</a></li>
						<li class="m2"><a href="about-us.html" class="active">About</a></li>
						<li class="m3"><a href="services.html">Services</a></li>
						<li class="m4"><a href="support.html">Support</a></li>
						<li class="m5"><a href="contact-us.html">contacts</a></li>
						<li class="m6"><a href="sitemap.html">Sitemap</a></li>
					</ul>
		</div>
	  
	  
	  
      <div id="headerrightblank">
        
	  <div id="loginPanel">
   	  	<h2>Welcome, <br/><br/><br/> </h2> <div class="blank"></div> <div class="blank"></div>
		
		<form action="uploadmanager.php" enctype="multipart/form-data" method="post">
   		<h3>- Input your weight -</h3> 
		<input type="text" name="weight" value="" size="15" /> kg
		
		<h3>- Upload your monitoring data -</h3> 
     	<input type="file" name="uploaded_datafile" value="" size="15" />
     	<input type="submit" name="submit" value="Upload" onMouseDown="test()" />
		
		<div id="FileName">
			File Uploaded:<br/>
			 <a style="color: #33FFFF"><?php
			 $length = strlen($FileName);
			 $N = $length/50;
			 //echo $N;
			 //echo ceil($N);
			 //echo substr("abcdef", 1, 3); 
			 for($i=1; $i<=$N+1; $i++){
			 	echo substr($FileName, 50*($i-1), 50);
				echo "  "; 
			 }
			 //echo $FileName ?> </a> <br />
		</div>	
 	  </form>
	  
	    <form action="dataanalyse.php" method="post">
	    	<input type="submit" name="submit_analyzedata" value="Analyze Data" />
		</form>
    </div>
      
        <div id="special">Work out with friends </div>
        <div id="year">2012</div>
      </div>
	    
		<div id="headernav">
          <ul>
            <li><a href="#" class="register">My Results </a></li>
            <li><a href="#" class="login">Challenge History</a></li>
			<li><a href="login.php" class="login">Log Out</a></li>

          </ul>
        </div>
		

		
	  <div id="bd" class="tdl">
	  <h2>	ANALYZE RESULTS </h2>
	  
			<div id="chart">
				<?php
					if($flag_analyse==1){
						//echo "<img src='Naked.png' >"; echo "\r\n";
						//echo "<img src='Naked.png' >";
						}
				?>
							</div>

			<div id="result">
				<br />
          		<li>Time in HR-zone FOUR: <a style="color: #33FFFF"><?php echo $tz4; ?> </a></a></a> sec. <br /></li>
				<li>Time in HR-zone FIVE: <a style="color: #33FFFF"><?php echo $tz5; ?> </a> sec.<br /></li>
				<li>Total Energy Consume: <a style="color: #33FFFF"><?php echo $eng; ?> </a> Calories<br /></li> <p>
				<li>Total Score: <a style="color: #33FFFF"><?php echo $scoreSum; ?> </a> points <br /></li>
		
			</div> <hr/>
			
			<div id="challenge">
				<form action="saveresult.php" method="post">
				  <input type="submit" name="submit_choneself" value="Save results" /> 
				  <a style="color: #0099FF"><?php echo $resultsave ?> <br /><br />
	    			<a href="user_main_ch_oneself.php" > Challenge Yourself / </a> 
					<a href="user_main_ch_friend.php" > Challenge Friend / </a> 
					<a href="user_main_ch_random.php" > Challenge Random </a>
		</form> </div>				
					  
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
