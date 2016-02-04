<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
<link rel="shortcut icon" href="favicon.ico">
</head>
<body>
<form action="index.php" method="post">
<br>

  Search for bike on cz/sk bike bazars<br>
  <input type="radio" name="search" value="enduro"> Search for enduro.<br>
  <input type="radio" name="search" value="onone"> Search for on-one.<br>
  <input type="radio" name="search" value="ragley"> Search for ragley.<br>
  <input type="radio" name="search" value="mongoose"> Search for mongoose.<br>
  <input type="radio" name="search" value="dartmoor"> Search for dartmoor.<br>
  <input type="radio" name="search" value="nsbike"> Search for nsbike.<br>
  <input type="radio" name="search" value="charge"> Search for charge.<br>
  <input type="radio" name="search" value="caprnka"> Search for caprnka.<br> 
  <input type="radio" name="search" value="devilwork"> Search for devilwork.<br> 
  <input type="radio" name="search" value="duratec"> Search for duratec.<br>
  <input type="radio" name="search" value="mrazek"> Search for mrazek.<br>
  <input type="radio" name="search" value="franta"> Search for franta.<br>
  <input type="radio" name="search" value="nukeproof"> Search for nukeproof.<br>
  <input type="radio" name="search" value="banshee"> Search for banshee.<br>
  <input type="radio" name="search" value="commencal"> Search for commencal.<br>
  <input type="radio" name="search" value="agang"> Search for agang.<br>





 <input type="submit" name="submit" value="Submit"><br>

</form>

<?
header('charset=utf-8');

$date = date('d-m-Y');
$file = 'searches';


if (isset($_POST['submit'])) {
 if ($_POST['search']=="enduro") {
  $command = "python bikesearch.py enduro 2>&1";
 }
 if ($_POST['search']=="nsbike") {
  $command = "python bikesearch.py ns+bike 2>&1";
 }
 if ($_POST['search']=="devilwork") {
  $command = "python bikesearch.py devilwork 2>&1";
 }
 if ($_POST['search']=="duratec") {
  $command = "python bikesearch.py duratec 2>&1";
 }       
 if ($_POST['search']=="onone") {
  $command = "python bikesearch.py on-one 2>&1";
 }
 if ($_POST['search']=="mongoose") {
  $command = "python bikesearch.py mongoose 2>&1";
 }
 if ($_POST['search']=="dartmoor") {
  $command = "python bikesearch.py dartmoor 2>&1";
 }   
 if ($_POST['search']=="ragley") {
  $command = "python bikesearch.py ragley 2>&1";
 }
 if ($_POST['search']=="banshee") {
  $command = "python bikesearch.py banshee  2>&1";
 }
 if ($_POST['search']=="caprnka") {
  $command = "python bikesearch.py caprnka 2>&1";
 }
 if ($_POST['search']=="charge") {
   print "If you find black charge blender with bomber fork somewhere on net, please contact me on bike@synapsia.sk"; 
   # Ak si nasiel charge blender niekde na predaj, prosim kontaktuj mna na bike@synapsia.sk
   # If you find black charge blender with bomber fork somewhere on net, please contact me on bike@synapsia.sk
# $command = "python bikesearch.py charge 2>&1";
 }
 if ($_POST['search']=="mrazek") {
  $command = "python bikesearch.py mrazek 2>&1";
 }
 if ($_POST['search']=="franta") {
  $command = "python bikesearch.py franta 2>&1";
 }
 if ($_POST['search']=="nukeproof") {
  $command = "python bikesearch.py nukeproof 2>&1";
 }
 if ($_POST['search']=="commencal") {
  $command = "python bikesearch.py commencal 2>&1";
 }
 if ($_POST['search']=="agang") {
  $command = "python bikesearch.py agang 2>&1";
 }
 


 $client = $_SERVER['REMOTE_ADDR'];
 $logdate = date('d.m.Y H:i:s', time());
 $openf = file_get_contents($file);
 $l = $client." - - ".$logdate." Search: ".$_POST['search']."\n"; 
 $openf .= $l;
 file_put_contents($file, $openf);

#  $command = "python bikesearch.py mongoose 2>&1";
  $pid = popen( $command,"r");
  while( !feof( $pid ) )
  {
   echo fread($pid, 256);
   flush();
   ob_flush();
   usleep(10000);
  }
  pclose($pid);

 } 
  
?>
</html>
