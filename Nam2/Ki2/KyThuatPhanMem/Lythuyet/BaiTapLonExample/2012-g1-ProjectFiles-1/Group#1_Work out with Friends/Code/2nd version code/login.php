<?php
	echo $msg;
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Work Out with Friend</title>
<link href="css_login.css" rel="stylesheet" type="text/css" />
<link rel="icon" href="images/icon.ico" />
</head>

	<script language="javascript">
		function jcud(){
			var cds1=window.frm.userid.value;
			var cds2=window.frm.password.value;
			if( cds1=="" ){
				window.alert("User ID can't be empty");
				window.frm.userid.focus();
			}
			else if( cds2==""){
				window.alert("Password can't be empty");
				window.frm.password.focus();
			}
		}
	</script>

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
        
	  <div id="loginPanel">
   	  	<h2>Member Login</h2>
	<div id="bd" class="tdl"><hr/>
		<form method="post" name="frm" action="login_varify.php">
		  <table width="100%" border="0">
		    <tr><td align="right">User ID</td>
			  <td><input type="text" name="userid" size="30" />*</td></tr>
			<tr><td align="right">Password</td>
			  <td><input type="password" name="password" size="21" />*</td></tr>
			
			<tr><td align="right">
			  <td><input type="submit" name="subm" value="Login" onMouseDown="jcud()"/>
			  <a href="#"> Forget the password ? </a></p>
			  <td></tr>
			  
		  </table>
		 </form>
	 </div>
  	  </div>
      
        <div id="special">Work out with friends </div>
        <div id="year">2012</div>
		
        <div id="searchblank">
      
        </div>
      </div>
      
        
      </div>
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
