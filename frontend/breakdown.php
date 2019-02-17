<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Orders</title>
  </head>
  <body>
    <h1> Order Breakdown </h1>
    <div class = "search-form">
        <form action="hack.php" method="POST">
            <strong>Who ordered [item name placeholder]? </strong><br>
            <input type="text" name="names_list"><br><br>
            <input type="submit" value="Next item" class="submit-search">
        </form><br>
    </div>

    <?php
        $names_list = $_POST["names_list"];
        echo $names_list;

        $result = json_decode(exec('python myscript.py'), true);
        echo $result['BJS FRITOS NACHOS'];
    ?>
  </body>
</html>