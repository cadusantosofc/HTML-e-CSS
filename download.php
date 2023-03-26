<?php
if (isset($_POST['submit'])) {
    $url = $_POST['url'];
    $command = "python3 youtube-dl-script.py " . $url;
    shell_exec($command);
    $file = getcwd() . "/downloads/" . basename($url) . ".mp3";
    header("Location: index.php?file=$file");
}
?>
