<?php

	//printf("dataanalyse.php\n");
	
	$cf=fopen("FileName_upload.dat","r+");
	$FileName = fgets($cf);
	
	$cf=fopen("$FileName", "r+");
	//$data = fgets($cf);
	//echo $data;
	
	$content = file_get_contents("$FileName");
	//echo $content;
	$array = explode("\n", $content);
	//print_r($array);
	
	/*
	for($i=0; $i<count($array); $i++){
    	echo $array[$i].'<br />';
	}*/
	printf("\n%d",count($array));
	
	
	$DBHOST = "localhost:3306";
	$DBUSER = "root";
	$DBPWD = "Xbdd136816";
	$DBNAME = "dbweb";
	
	$cf = fopen('uid.dat','r'); $userid = fgets($cf); fclose($cf);	
	echo $userid;
	
	$connection = @mysql_connect( $DBHOST, $DBUSER, $DBPWD ) or die("Can't connect to Database!");
	@mysql_select_db($DBNAME) or die("Read database error: can't find the database!");
	$query = "SELECT * FROM user WHERE uid='$userid' ";
	$result = @mysql_query($query, $connection) or die("Data query error:");
	$row = mysql_fetch_row($result);
	echo $row[3]; 
	echo $row[4];
	
	$gender=$row[3]; 
	$age=$row[4];
	
	// Data Analysis //////////////////////////////////////////////////
	$cf = fopen("weight_upload.dat","r+");
	$weight = fgets($cf);
	
	// Find maxHR
	$maxHR  = max( $array );
	$aveHR = array_sum($array)/count($array);
	printf("\n\n%d", $maxHR);
	printf("Count: %d\r\n", count($array));
	printf("Sum: %d\r\n", array_sum($array));
	printf("Ave: %d\r\n", array_sum($array)/count($array) );
	$time=count($array)/60/60;
	echo $time;
	
	//
	// Male: C =  ((-55.0969 + (0.6309 x HR) + (0.1988 x W) + (0.2017 x A))/4.184) x 60 x T 
    // Female: C = ((-20.4022 + (0.4472 x HR) - (0.1263 x W) + (0.074 x A))/4.184) x 60 x T 
	if( $gender =="F" ){
		//printf("Female");
		$C =((-20.4022 + (0.4472 * $aveHR) - (0.1263 * $weight) + (0.074 * $age))/4.184) * 60 * $time ;
	}
	else{
		$C = ((-55.0969 + (0.6309 * $aveHR) + (0.1988 * $weight) + (0.2017 * $age))/4.184) * 60 * $time;
	}
	
	
	// 
	$tz4=0; $tz5=0; $eng=0; 
	for($i=0; $i<count($array); $i++){
		if($array[$i]>0.9*$maxHR && $array[$i]<=$maxHR ){
			$tz5++;
		}
		elseif( $array[$i]>0.8*$maxHR && $array[$i]<=0.9*$maxHR ){
			$tz4++;
		}
	}
	//$tz4=$tz4/2; $tz5=$tz5/2;
	printf("tz4=%d\n", $tz4);
	printf("tz5=%d\n", $tz5); 
	
	$score1= $tz5 * 10 * 0.4;
	$score3= $tz4 * 0.35;
	$score2= $C * 0.25;
	$scoreSum= $score1 + $score2 + $score3;	
	
	// Write back analysed results	
	$cf4 = fopen("tz4.dat", "w+"); $cf5 = fopen("tz5.dat", "w+"); $cfeng = fopen("eng.dat", "w+"); $cfsum = fopen("scoreSum.dat","w+");	
	fputs($cf4, $tz4); fputs($cf5, $tz5); fputs($cfsum, $scoreSum);	 fputs($cfeng, $C);
	fclose($cf4); fclose($cf5); fclose($cfsum); fclose($cfeng);
	
	/*
	// Draw pChart
	// Standard inclusions     
include("pChart/pData.class");  
include("pChart/pChart.class");  
  
// Dataset definition   
$DataSet = new pData; 
for($i=0; $i<count($array); $i++){
	$DataSet->AddPoint($array[$i]);
}   
$DataSet->AddSerie();  
$DataSet->SetSerieName("Sample data","Serie1");  
  
// Initialise the graph  
$Test = new pChart(700,230);  
$Test->setFontProperties("Fonts/tahoma.ttf",10);  
$Test->setGraphArea(40,30,680,200);  
$Test->drawGraphArea(252,252,252);  
$Test->drawScale($DataSet->GetData(),$DataSet->GetDataDescription(),SCALE_NORMAL,150,150,150,TRUE,0,2);  
$Test->drawGrid(4,TRUE,230,230,230,255);  
  
// Draw the line graph  
$Test->drawLineGraph($DataSet->GetData(),$DataSet->GetDataDescription());  
$Test->drawPlotGraph($DataSet->GetData(),$DataSet->GetDataDescription(),3,2,255,255,255);  
  
// Finish the graph  
$Test->setFontProperties("Fonts/tahoma.ttf",8);  
$Test->drawLegend(45,35,$DataSet->GetDataDescription(),255,255,255);  
$Test->setFontProperties("Fonts/tahoma.ttf",10);  
$Test->drawTitle(60,22,"My pretty graph",50,50,50,585);  
$Test->Render("Naked.png"); */
	
	
	
	
	// signal data analysed
	$cf=fopen("flgaFile_analyse.dat", "w+");
	fputs($cf,1); fclose($cf);
	echo "<meta http-equiv='Refresh' content='0; url = user_main.php ?'>";
?>



