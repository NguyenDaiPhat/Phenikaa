<?php

	$weight = $_POST['weight'];
	$cf = fopen("weight_upload.dat","w+");
	fputs($cf, $weight);
	fclose($cf);

	/* Set a constant */
	define ("FILEREPOSITORY","D:/Program Files/Apache Group/Apache2/htdocs/wdh/shape/shape/html/upload_files");

	/* Make sure that the file was POSTed. */
	if (is_uploaded_file($_FILES['uploaded_datafile']['tmp_name'])) {
	
    	//File Type
		//printf("%s\n", $_FILES['classnotes']['type']);	
		if ($_FILES['uploaded_datafile']['type'] != "text/plain") {
        	//echo "<p>Upload file must be in txt format.</p>";
			echo "<meta http-equiv='Refresh' content='0; url = user_main.php ?'>";
		} 
		else {
        	/* move uploaded file to final destination. */
        	// $name = $_POST['name'];
			$name = $_FILES['uploaded_datafile']['name'];
			//echo $name;
			
			$result = move_uploaded_file($_FILES['uploaded_datafile']['tmp_name'], FILEREPOSITORY."/$name");
			if( $result ==1 ){
					echo "<p>File successfully uploaded. </p>";
					$flagFile_upload="flagFile_upload.dat";
					$cf=fopen( $flagFile_upload,"w+" );
					fputs( $cf, "1" );
					fclose( $cf );
					
					$FileName_upload="FileName_upload.dat";
					$cf=fopen( $FileName_upload,"w+" );
					fputs( $cf, FILEREPOSITORY."/$name" );
					fclose( $cf );
					
					$cf=fopen( $FileName_upload,"r+" );
					$name_test=fgets($cf);
					fclose( $cf );
					echo $name_test;
					
					echo "<meta http-equiv='Refresh' content='0; url = user_main.php ?'>";
				}
			else{
					echo "<p>There was a problem uploading the file. </p>";
					$flagFile_upload="flagFile_upload.dat";
					$cf=fopen( $flagFile_upload,"w+" );
					fputs( $cf, "0" );
					fclose( $cf );
				}
			}
		}

?>