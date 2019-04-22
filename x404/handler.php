<?php

# 
$lookupkey = trim($_SERVER['REQUEST_URI'],'/');

# query URLS.db
$dir = 'sqlite:URLs.db';
$dbh  = new PDO($dir) or die("cannot open the database");
$query =  $dbh->prepare("SELECT long_url from URLS where short_url = :short_url");
$query->bindParam(':short_url', $lookupkey);
$query->execute();
$result = $query->fetchAll();

# see if there's a URL
if (count($result) > 0 && substr($result[0]['long_url'], 0, strlen("http")) === "http") {
  $newURL = $result[0]['long_url'];
  header("Location:$newURL");
  exit;
}

http_response_code(404);
print "404 Not Found";

?>
